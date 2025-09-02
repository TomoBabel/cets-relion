from typing import Optional, Union
import os
from gemmi import cif
from logging import getLogger
from src.models.models import CTFMetadata
from src.cets_relion.tilt_series import RelionTiltSeriesStarfile

logger = getLogger(__name__)


class RelionCtfStarFile(RelionTiltSeriesStarfile):
    """Object for handling the output file from a CtfFind job

    Attrs:
        name: Relative path for the file
    """

    def __init__(self, file_name: Union[str, os.PathLike]) -> None:
        super().__init__(file_name=str(file_name))

    def get_tilt_image_ctf(
        self, ts_name: str, image_name: Union[str, os.PathLike]
    ) -> Optional[CTFMetadata]:
        """Get CTF  info for a tilt image from a tilt series

        Args:
            image_name (str): The name of the movie frame image

        Returns:
            Optional[CTFMetadata]: CETS CTFMetadata object or None if tilt image not found
        """
        # read the starfile
        # try:
        tsstar = cif.read_file(str(self.get_tilt_series_star_file(ts_name)))
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
        line = [x for x in data if x[0] == image_name]
        if not line:
            return None
        print(line)
        vals = list(line[0])[1:]
        return CTFMetadata(defocus_u=vals[0], defocus_v=vals[1], defocus_angle=vals[2])
        # except Exception:
        #     return None
