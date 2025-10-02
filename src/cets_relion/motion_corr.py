import os
from typing import Optional, Union, Dict

from cets_data_model.models.models import CTFMetadata

from cets_relion.tilt_series import RelionTiltSeriesStarfile


class RelionMotionCorrStarFile(RelionTiltSeriesStarfile):
    """Subclass for handling results from RELION motion corr jobs"""

    def __init__(self, file_name: Union[str, os.PathLike]) -> None:
        """Instantiate a RelionMotionCorrStarFile"""
        super().__init__(file_name=file_name)

    def get_gain_file(self) -> Optional[str]:
        """Get the name of the gain reference file

        Returns:
            str: Path to the file, relative to the project
        """
        joval = self.get_joboptions().get("fn_gain_ref")
        if joval in ("''", '""'):
            return None
        return joval

    def get_defect_file(self) -> Optional[str]:
        """Get the name of the defect file

        Returns:
            str: Path to the file, relative to the project
        """
        joval = self.get_joboptions().get("fn_defect")
        if joval in ('""', "''"):
            return None
        return joval

    def get_tilt_image_ctfs(self, ts_name: str) -> Dict[str, CTFMetadata]:
        raise NotImplementedError("Motion corr starfiles have no ctf information")

    def get_motioncorr_cets_for_tilt_series(self) -> None:
        """This object has not been added to the model yet"""
        return None
