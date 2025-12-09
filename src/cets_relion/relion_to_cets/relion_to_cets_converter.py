"""Script to convert CryoET data from RELION to TomoBabel CETS format"""

from pathlib import Path
from typing import List, Dict, Union, Optional

from cets_data_model.models.models import GainFile, DefectFile
from cets_data_model.utils.image_utils import get_mrc_dims
from gemmi import cif

from cets_relion.relion_to_cets.motion_corr import RelionMotionCorrStarFile
from cets_relion.relion_to_cets.movies import RelionMoviesStarFile
from cets_relion.relion_to_cets.particle_coords import (
    RelionCoordsStarFile,
    RelionParticlesStarFile,
    parse_particles_file,
)
from cets_relion.relion_to_cets.relion_reader import RelionPipeline
from cets_relion.relion_to_cets.subtomo_averages import RelionSubtomoAverage
from cets_relion.relion_to_cets.tilt_series import RelionTiltSeriesStarfile
from cets_relion.relion_to_cets.tomograms import RelionTomosStarfile
from cets_relion.job_utils import get_job_type
from tmp_transformations import logical_coords

# cets converters for specific jobtypes
# {job_type: (file_to_use, converter_class, attr to set)}
converters = {
    "relion.importtomo": ("tilt_series.star", RelionMoviesStarFile, "movies"),
    "relion.motioncorr.own": (
        "corrected_tilt_series.star",
        RelionMotionCorrStarFile,
        "mocorr",
    ),
    "relion.ctffind.ctffind4": (
        "tilt_series_ctf.star",
        RelionTiltSeriesStarfile,
        "ctf",
    ),
    "relion.excludetilts": (
        "selected_tilt_series.star",
        RelionTiltSeriesStarfile,
        "tilt_series",
    ),
    "relion.aligntiltseries": (
        "aligned_tilt_series.star",
        RelionTiltSeriesStarfile,
        "tilt_series",
    ),
    "relion.reconstructtomograms": ("tomograms.star", RelionTomosStarfile, "tomos"),
    "relion.denoisetomo": ("tomograms.star", RelionTomosStarfile, "tomos"),
}


def parse_optimisation_set(
    opt_set_file: Path,
) -> Dict[
    str, Union[RelionParticlesStarFile, RelionCoordsStarFile, RelionTomosStarfile]
]:
    """Parse an optimisation_set file to get tomogram and particles/coords

    Depending on what job the file came from it will return either extracted particles
    or raw particle coordinates

    Args:
        opt_set_file (Path): Path to the optimisation_set file
    Returns:
        Dict[
            str,
            Union[RelionParticlesStarFile, RelionCoordsStarFile, RelionTomosStarfile]
        ]: Dictionary of tomogram and particles/coords
    """
    opt_block = cif.read_file(str(opt_set_file)).sole_block()

    # it might have pairs
    parts = opt_block.find_pair("_rlnTomoParticlesFile")
    tomos = opt_block.find_pair("_rlnTomoTomogramsFile")
    vals_dict: Dict[
        str, Union[RelionParticlesStarFile, RelionCoordsStarFile, RelionTomosStarfile]
    ] = {}
    if parts is not None and tomos is not None:
        part_attr, part_obj = parse_particles_file(parts[1])
        vals_dict[part_attr] = part_obj
        vals_dict["tomos"] = RelionTomosStarfile(tomos[1])

    # or it might have a loop
    else:
        loop = opt_block.find(
            prefix="_rln", tags=["TomoParticlesFile", "TomoTomogramsFile"]
        )
        if loop is not None:
            vals_dict["tomos"] = RelionTomosStarfile(loop[0][1])
            # get the correct object and attr for the files with particles
            parts_value, parts_obj = parse_particles_file(loop[0][0])
            vals_dict[parts_value] = parts_obj

    return vals_dict


class RelionCetsConverter:
    """An object that holds all the data necessary for RELION -> CETS conversion
    Attributes:
        pipeline (RelionPipeline): A Relion pipeline object for the project workflow
        movies (List[RelionMoviesStarFile]): Objects that contains data about the raw
            movies
        mocorr (List[RelionMotionCorrStarFile]): Objects that contains data about the
            motion correction jobs for each tilt series
        ctf (List[RelionTiltSeriesStarfile]): Objects that contains data about the
            ctf determination jobs for each tilt series
        tilt_series (List[RelionTiltSeriesStarfile]): Objects that contains data about
            the final tilt series (after alignment, tilt exclusion & etc...)
        tomos (List[RelionTomosStarfile]): Objects that contains data about the
            tomograms generated from each tilt series
        picks (List[RelionCoordsStarFile]): Objects that contains data about the
            coordinates picked on tomograms
        averages (List[RelionSubtomogramAverage]): Objects that contains data about sub
            tomograms averages generated from the data.
        )



    """

    def __init__(self, terminal_job: str) -> None:
        """Instantiate a Relion CetsConverter object

        Args:
            terminal_job (str): The name of the terminal job
        """
        self.pipeline = RelionPipeline("default_pipeline.star")
        # init empty attrs
        self.movies: List[RelionMoviesStarFile] = []
        self.ctf: List[RelionTiltSeriesStarfile] = []
        self.mocorr: List[RelionMotionCorrStarFile] = []
        self.picks: List[RelionCoordsStarFile] = []
        self.tilt_series: List[RelionTiltSeriesStarfile] = []
        self.tomos: List[RelionTomosStarfile] = []
        self.particles: List[RelionParticlesStarFile] = []
        self.averages: List[RelionSubtomoAverage] = []

        # first try to set attrs based on the terminal job data if it is a type without
        # an optimisation set. Possibly sets any attr, depending on the terminal job
        tjob_type = get_job_type(terminal_job)
        if converters.get(tjob_type) is not None:
            file, obj, attr = converters[tjob_type]
            setattr(self, attr, [obj(Path(terminal_job) / file)])

        # Find and subtomogram averages associated with the terminal job
        pipe = RelionPipeline("default_pipeline.star")
        stas = [
            x
            for x in list(pipe.graph.successors(terminal_job))
            if pipe.graph.nodes()[x]["relion_type"] == "DensityMap"
            and "halfmap" not in pipe.graph.nodes()[x]["kwds"]
        ]
        if stas:
            try:
                self.averages = [RelionSubtomoAverage(x) for x in stas]
            except NotImplementedError:
                pass

        # try to get info from an optimization set if it exists
        # possibly sets picks, particles, and/or tomos attrs
        opt_set = sorted(list(Path(terminal_job).glob("*optimisation_set.star")))
        if opt_set:
            opt_values = parse_optimisation_set(opt_set[-1])
            if opt_values:
                for key, val in opt_values.items():
                    setattr(self, key, [val])
        # of one is not in terminal job see if any associated with averages
        elif self.averages:
            opt_sets = [x.opt_set for x in self.averages]
            for optset in opt_sets:
                opt_values = parse_optimisation_set(optset)
                # ignore type checking here because parse function has multiple return
                # types
                self.tomos.append(opt_values["tomos"])  # type: ignore[arg-type]
                self.particles.append(opt_values["particles"])  # type: ignore[arg-type]

        # if extracted particles have been found get the associated coords
        if self.particles and not self.picks:
            pick_files = []
            for partfile in self.particles:
                pick_files.extend(partfile.get_coords_object())
            self.picks = pick_files

        # if tomograms have been found try to find the aligned tilt series
        if self.tomos and not self.tilt_series:
            ts_files = self.pipeline.next_upstream_files(
                start=terminal_job,
                relion_type=["TomogramGroupMetadata"],
                kwds=["aligntiltseries"],
            )
            for tsfile in ts_files:
                self.tilt_series.append(RelionTiltSeriesStarfile(tsfile))

        # set the ctf attr if not already set
        if not self.ctf:
            ctf_jobs = self.pipeline.next_upstream_jobs(
                terminal_job, jobtypes=["relion.ctffind.ctffind4"]
            )
            for ctf_job in ctf_jobs:
                output = Path(ctf_job) / "tilt_series_ctf.star"
                self.ctf.append(RelionTiltSeriesStarfile(output))

        # find any motion correction jobs
        self.mocorr = []
        mocorr_jobs = self.pipeline.next_upstream_jobs(
            terminal_job, jobtypes=["relion.motioncorr.own"]
        )
        for mocorr_job in mocorr_jobs:
            output = Path(mocorr_job) / "corrected_tilt_series.star"
            self.mocorr.append(RelionMotionCorrStarFile(output))

        # set the movies attr of not already set
        if not self.movies:
            movies_jobs = self.pipeline.next_upstream_jobs(
                terminal_job, jobtypes=["relion.importtomo"]
            )
            # ToDo: add case for merged images import
            for movie_job in movies_jobs:
                output = Path(movie_job) / "tilt_series.star"
                movobj = RelionMoviesStarFile(output)
                movobj.ctf_files = self.ctf
                movobj.mocorr_files = self.mocorr
                self.movies.append(movobj)

    def find_gain_file(self, tomo_name: str) -> Optional[GainFile]:
        """Find the Gain file for the given tomogram.
        Searches all files in self.mocorr in case of multiple mocorr files

        Args:
            tomo_name: The name of the tomogram.
        Returns:
            The path to the Gain file for the given tomogram.
        """
        for mocorrfile in self.mocorr:
            if mocorrfile.tilt_series_in_file(tomo_name):
                gf = mocorrfile.get_gain_file()
                if gf:
                    # ToDo: add gain reference transformations here
                    height, width, _depth = get_mrc_dims(gf)
                    return GainFile(
                        path=gf,
                        width=width,
                        height=height,
                        coordinate_systems=[logical_coords()],
                    )
        return None

    def find_defect_file(self, tomo_name: str) -> Optional[DefectFile]:
        """Find the Gain file for the given tomogram.
        Searches all files in self.mocorr in case of multiple mocorr files

        Args:
            tomo_name: The name of the tomogram.
        Returns:
            The path to the Gain file for the given tomogram.
        """
        for mocorrfile in self.mocorr:
            if mocorrfile.tilt_series_in_file(tomo_name):
                df = mocorrfile.get_defect_file()
                if df:
                    height, width, _depth = get_mrc_dims(df)
                    return DefectFile(
                        path=df,
                        width=width,
                        height=height,
                        coordinate_systems=[logical_coords(tomo_name)],
                    )
        return None

    def get_all_tomo_names(self):
        # get names of all tomos/tilt series in the project
        # start at the movies and work down through the workflow
        all_tomo_names = []
        for movfile in self.movies:
            all_tomo_names.extend(movfile.get_all_tomo_names())
        if all_tomo_names:
            return all_tomo_names
        for ctffile in self.ctf:
            all_tomo_names.extend(ctffile.get_all_tomo_names())
        if all_tomo_names:
            return all_tomo_names
        for ts_file in self.tilt_series:
            all_tomo_names.extend(ts_file.get_all_tomo_names())
        if all_tomo_names:
            return all_tomo_names
        for tomofile in self.tomos:
            all_tomo_names.extend(tomofile.get_all_tomo_names())
        if all_tomo_names:
            return all_tomo_names

        # only default to coords/particles if nothing else in available
        # both should have tomos in mode ceases
        for partfile in self.particles:
            all_tomo_names.extend(partfile.get_all_tomo_names())
        if all_tomo_names:
            return all_tomo_names
        for coordfile in self.picks:
            all_tomo_names.extend(coordfile.get_all_tomo_names())
        if all_tomo_names:
            return all_tomo_names
        raise ValueError("No tomogram names found")
