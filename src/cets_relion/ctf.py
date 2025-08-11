from typing import Optional
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

    def __init__(self, file_name: str) -> None:
        super().__init__(file_name=file_name)

    def get_tilt_image_ctf(self, image_name: str) -> Optional[CTFMetadata]:
        """Get CTF  info for a tilt image from a tilt series

        Args:
            image_name (str): The name of the movie frame image

        Returns:
            Optional[CTFMetadata]: CETS CTFMetadata object or None if tilt image not found
        """
        # read the starfile
        try:
            tsstar = cif.read_file(self.get_tilt_series_star_file(image_name))
            data_block = tsstar.find_block("global")
            data = data_block.find(
                prefix="_rln",
                tags=[
                    "MicrographMovieNameDefocusU",
                    "DefocusU",
                    "DefocusAngle",
                ],
            )
            line = [x for x in data if x[0] == image_name]
            if not line:
                return None
            vals = line[0][1:]
            return CTFMetadata(
                defocus_u=vals[0], defocus_v=vals[1], defocus_angle=vals[2]
            )
        except Exception:
            return None
