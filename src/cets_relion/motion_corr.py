import os
from typing import Optional, Union, Dict

from cets_data_model.models.models import CTFMetadata

from cets_relion.tilt_series import RelionTiltSeriesStarfile
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
