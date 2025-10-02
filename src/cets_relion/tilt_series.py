from __future__ import annotations

from pathlib import Path
from cets_relion.relion_reader import RelionPipeline
import os
from typing import List, Union, Optional, Dict
from logging import getLogger
from cets_data_model.models.models import (
    CTFMetadata,
    ProjectionImage,
    Translation,
    Affine,
)
from cets_data_model.utils.image_utils import get_mrc_dims
from cets_relion.utils import rotation_to_matrix
from cets_relion.utils import joboptions_from_jobstar_file
from gemmi import cif
from cets_relion.objs.coordinate_systems import RELION_COORDS_PHYSICAL

logger = getLogger(__name__)


class RelionTiltSeriesStarfile(object):
    """Class for handling a global tilt series data file from RELION

    The tilt series data file is expected to contain merged single frame micrographs
    for each tilt angle

    can be subclassed for job-specific variants of this type of file

    Many jobs create this type of file, this object should enable tracing back to the
    original movies and making the necessary objects
    """

    def __init__(
        self,
        file_name: Union[str, os.PathLike],
        pipeline: str = "default_pipeline.star",
    ) -> None:
        self.name = str(file_name)
        self.file = Path(str(file_name))
        self.pipeline = RelionPipeline(pipeline)

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

    def get_specific_tilt_series_star_file(self, ts_name: str) -> Optional[Path]:
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
                return Path(line[1])
        return None

    def get_tilt_image_ctfs(self, ts_name: str) -> Dict[str, CTFMetadata]:
        """Get CTF  info for a tilt image from a tilt series

        Uses the movie names as key rather than the merge micrograph names so the
        Movies object can use it for lookup

        Args:
            ts_name: Name of the tilt series
            image_name (str): The name of the movie frame image

        Returns:
            Optional[CTFMetadata]: CETS CTFMetadata object or None if tilt image not found
        """
        # read the starfile
        ctfs_dict = {}
        tsstar = cif.read_file(str(self.get_specific_tilt_series_star_file(ts_name)))
        data_block = tsstar.find_block(ts_name)
        data = data_block.find(
            prefix="_rln",
            tags=[
                "MicrographMovieName",
                "DefocusU",
                "DefocusV",
                "DefocusAngle",
            ],
        )
        for line in data:
            ctfs_dict[cif.as_string(line[0])] = CTFMetadata(
                defocus_u=float(line[1]),
                defocus_v=float(line[2]),
                defocus_angle=float(line[3]),
            )
        return ctfs_dict

    def get_tilt_image_doses(self, ts_name: str) -> Dict[str, float]:
        """Get CTF  info for a tilt image from a tilt series

        Args:
            ts_name: Name of the tilt series
            image_name (str): The name of the movie frame image

        Returns:
            float: The total accumulated dose for the tilt angle image
        """
        tsstar = cif.read_file(str(self.get_specific_tilt_series_star_file(ts_name)))
        data_block = tsstar.find_block(ts_name)
        data = data_block.find(
            prefix="_rln",
            tags=[
                "MicrographName",
                "MicrographPreExposure",
            ],
        )
        mic_vals = {cif.as_string(x[0]): float(x[1]) for x in data}
        dose_rate = list(mic_vals.values())[1] - list(mic_vals.values())[0]
        dose_dict = {}
        for img, preexp in mic_vals.items():
            dose_dict[img] = preexp + dose_rate
        return dose_dict

    def get_cets_projection_images(
        self, ts_name: str, dose_dict: Optional[Dict[str, float]] = None
    ) -> List[ProjectionImage]:
        """Get cets ProjectionImage objects (merged motion corrected images) for a tilt
        series

        ts_starfile (str): The starfile for the tilt series
        dose_dict (Optional[Dict[str, float]): Dictionary of total accumulated dose for
            each tilt angle image

        Returns:
            List[ProjectionImage]: List of cets ProjectionImage objects
        """
        tiltimgs_file = self.get_specific_tilt_series_star_file(ts_name)
        block = cif.read_file(str(tiltimgs_file)).find_block(ts_name)
        dose_dict = self.get_tilt_image_doses(ts_name)
        data = block.find(
            prefix="_rln",
            tags=[
                "MicrographName",
                "TomoNominalStageTiltAngle",
                "DefocusU",
                "DefocusV",
                "DefocusAngle",
            ],
        )
        alignment_data = block.find(
            prefix="_rln",
            tags=[
                "TomoXTilt",
                "TomoYTilt",
                "TomoZRot",
                "TomoXShiftAngst",
                "TomoYShiftAngst",
            ],
        )
        cets_objects = []
        for n, row in enumerate(data):
            micname = cif.as_string(row[0])
            x_size, y_size, _z_size = get_mrc_dims(micname)
            defocus_u = row[2]
            defocus_v = row[3]
            defocus_angle = row[4]
            nom_tilt = row[1]
            ctf = CTFMetadata(
                defocus_u=defocus_u,
                defocus_v=defocus_v,
                defocus_angle=defocus_angle,
                defocus_handedness=-1,
            )
            cets_obj = ProjectionImage(
                path=micname,
                section=str(n),
                width=x_size,
                height=y_size,
                coordinate_systems=[RELION_COORDS_PHYSICAL],
                nominal_tilt_angle=nom_tilt,
                ctf_metadata=ctf,
                accumulated_dose=dose_dict[micname],
            )
            try:
                xtilt, ytilt, zrot, xshift, yshift = [
                    float(x) for x in alignment_data[n]
                ]
                translation = Translation(
                    name="Tilt image alignment translation",
                    translation=[xshift, yshift],
                )
                x_affine = Affine(
                    name="Tilt image alignment x tilt",
                    affine=rotation_to_matrix(xtilt, "x"),
                )
                y_affine = Affine(
                    name="Tilt image alignment y tilt",
                    affine=rotation_to_matrix(ytilt, "y"),
                )
                z_affine = Affine(
                    name="Tilt image alignment x rotation",
                    affine=rotation_to_matrix(zrot, "z"),
                )
                cets_obj.coordinate_transformations = [
                    translation,
                    x_affine,
                    y_affine,
                    z_affine,
                ]
            except IndexError:
                pass
            cets_objects.append(cets_obj)

        return cets_objects
