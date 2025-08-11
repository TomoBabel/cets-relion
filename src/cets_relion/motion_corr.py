from typing import Optional
from src.cets_relion.tilt_series import RelionTiltSeriesStarfile


class RelionMotionCorrStarFile(RelionTiltSeriesStarfile):
    """Subclass for handling results from RELION motion corr jobs"""

    def __init__(self, file_name: str) -> None:
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
        if joval in ("''", '""'):
            return None
        return joval
