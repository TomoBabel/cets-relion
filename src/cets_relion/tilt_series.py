from __future__ import annotations

from typing import List, Dict
from pathlib import Path
from src.cets_relion.relion_reader import RelionPipeline
from src.cets_relion.utils import joboptions_from_jobstar_file
from gemmi import cif


class RelionTiltSeriesStarfile(object):
    """Class for handling a global tilt series data file from RELION


    can be subclassed for job-specific variants of this type of file

    Many jobs create this type of file, this object should enable tracing back to the
    original movies and making the necessary objects
    """

    def __init__(self, file_name: str, pipeline: str = "default_pipeline.star") -> None:
        self.name = file_name
        self.pipeline = RelionPipeline(pipeline)

    def get_raw_files(
        self,
    ) -> List[str]:
        upstream = self.pipeline.upstream_critical_path(start=self.name)
        import_files = []
        for unode in upstream.nodes:
            if (
                upstream.nodes[unode].get("relion_type") == "TomogramGroupMetadata"
                and upstream.nodes[unode].get("file_type") == "star"
                and "import" in upstream.nodes[unode].get("kwds")
            ):
                import_files.append(unode)
        raw_data_files = []
        for file in import_files:
            # get the job the file came from
            importjob = list(self.pipeline.graph.predecessors(file))[0]
            # determine if was import of movies or merged tomos
            jobfile = str(Path(importjob) / "job.star")
            jobops = joboptions_from_jobstar_file(jobfile)
            if jobops["images_are_motion_corrected"] == "No":
                raw_data_files.append(file)
            else:
                raw_data_files.append(file)

        return raw_data_files

    def get_joboptions(self) -> Dict[str, str]:
        jobfile = Path(self.name).parent / "job.star"
        return joboptions_from_jobstar_file(str(jobfile))

    def tilt_series_in_file(self, ts_name: str) -> bool:
        """Check if a specific tilt series is in this file

        Args:
            ts_name (str): Tilt series name to check

        Returns:
            bool: Is the tilt series present in this file
        """
        data = cif.read_file(self.name).sole_block()
        names = data.find(prefix="_rln", tags=["TomoName"])
        return ts_name in [x[0] for x in names]

    def get_tilt_series_star_file(self, ts_name: str) -> str:
        """Get the path of star file containing info on a single tilt series image set

        Args:
            ts_name (str): The tilt series name

        Returns:
            str: Path of the starfile for that individual tilt series images
        """
        cifdata = (
            cif.read_file(self.name)
            .sole_block()
            .find(prefix="_rln", tags=["TomoName", "TomoTiltSeriesStarFile"])
        )
        for line in cifdata:
            if line[0] == ts_name:
                return line[1]
        return ""

    def find_tomograms_in_self(self, ts_name: str) -> List[str]:
        """
        Find a tomograms that have been generated from this tilt series by upstream or
        down stream jobs.

        ts_name (str): Name of the tomogram/tilt series EG: TS_01

        Returns:
              List[str]: Path(s) to the tomogram(s), relative to the project
        """

        # fist look in this file itself, only valid for TomoReconstruct jobs
        # which aren't used for much in relion
        data = cif.read_file(self.name).sole_block()
        tomos = data.find(
            prefix="_rln", tags=["TomoName", "TomoReconstructedTomogramDenoised"]
        )
        tomo = dict(list(tomos)).get(ts_name)
        if tomo is not None:
            return [tomo]
        else:
            return []

    def find_tomograms_in_other_jobs(self, ts_name: str) -> List[str]:
        # next search upstream for reconstruction jobs that might have generated tomos
        upstream = self.pipeline.upstream_critical_path(start=self.name)
        tomo_files, found_tomos = [], []
        reconstruct_jobs = [
            x
            for x in upstream
            if upstream.nodes[x]["relion_type"] == "relion.denoisetomo"
        ]
        if reconstruct_jobs:
            for rec_job in reconstruct_jobs:
                tomo_files.extend(
                    self.pipeline.next_downstream_file_of_type(
                        start=rec_job,
                        relion_type="TomogramGroupMetadata",
                        kwds=["denoise"],
                    )
                )
        for tomo_file in tomo_files:
            tf = RelionTiltSeriesStarfile(tomo_file)
            tomo = tf.find_tomograms_in_self(ts_name)
            if tomo:
                found_tomos.extend(tomo)

        # next search downstream for reconstruction jobs that might have generated tomos
        downstream = self.pipeline.downstream_critical_path(start=self.name)
        reconstruct_jobs = [
            x
            for x in downstream
            if downstream.nodes[x]["relion_type"] == "relion.denoisetomo"
        ]
        if reconstruct_jobs:
            for rec_job in reconstruct_jobs:
                tomo_files.extend(
                    self.pipeline.next_downstream_file_of_type(
                        start=rec_job,
                        relion_type="TomogramGroupMetadata",
                        kwds=["denoise"],
                    )
                )

        for f in tomo_files:
            found_tomos.extend(
                RelionTiltSeriesStarfile(f).find_tomograms_in_self(ts_name)
            )
        return found_tomos

    def find_tomgrams(self, ts_name: str) -> List[str]:
        """
        Find any tomograms that have been generated from this tilt series

        ts_name (str): Name of the tomogram/tilt series EG: TS_01

        Returns:
              List[str]: Path(s) to the tomogram(s), relative to the project. If the job
              itself generated tomos those are returned otherwise tomos derived from
              other jobs are returned if they are present
        """
        from_self = self.find_tomograms_in_self(ts_name)
        if from_self:
            return from_self
        return self.find_tomograms_in_other_jobs(ts_name)
