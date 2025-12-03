import os
from typing import Optional, Union, Dict, List

from cets_data_model.models.models import ProjectionImage, CTFMetadata
from cets_data_model.utils.image_utils import get_mrc_dims
from gemmi import cif

from cets_relion.objs.coordinate_systems import RELION_COORDS_LOGICAL
from cets_relion.relion_to_cets.tilt_series import RelionTiltSeriesStarfile
from cets_relion.utils import joboptions_from_job


class RelionMotionCorrStarFile(RelionTiltSeriesStarfile):
    """Subclass for handling results from RELION motion corr jobs"""

    def __init__(self, file_name: Union[str, os.PathLike]) -> None:
        """Instantiate a RelionMotionCorrStarFile
        Args:
            file_name (Union[str, os.PathLike]): Path to the motioncorr starfile
        """
        super().__init__(file_name=file_name)

    def get_gain_file(self) -> Optional[str]:
        """Get the name of the gain reference file

        Returns:
            str: Path to the file, relative to the project
        """
        joval = joboptions_from_job(self.file.parent).get("fn_gain_ref")
        if joval in ("", ""):
            return None
        return joval

    def get_defect_file(self) -> Optional[str]:
        """Get the name of the defect file

        Returns:
            str: Path to the file, relative to the project
        """
        joval = joboptions_from_job(self.file.parent).get("fn_defect")
        if joval in ("", ""):
            return None
        return joval

    def get_tilt_image_ctfs(self, ts_name: str) -> Dict[str, CTFMetadata]:
        raise NotImplementedError("Motion corr starfiles have no ctf information")

    def get_cets_projection_images(self, ts_name: str) -> List[ProjectionImage]:
        """Get cets ProjectionImage objects (merged motion corrected images) for a tilt
        series

        Has tobe implemented separately in this subclas because much info comes from
        later jobs

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
            prefix="_rln", tags=["MicrographName", "TomoNominalStageTiltAngle"]
        )
        cets_objects = []
        for n, row in enumerate(data):
            micname = cif.as_string(row[0])
            x_size, y_size, _z_size = get_mrc_dims(micname)
            nom_tilt = row[1]
            cets_obj = ProjectionImage(
                path=micname,
                section=str(n),
                width=x_size,
                height=y_size,
                coordinate_systems=[RELION_COORDS_LOGICAL],
                nominal_tilt_angle=nom_tilt,
                accumulated_dose=dose_dict[micname],
            )
            cets_objects.append(cets_obj)
        return cets_objects
