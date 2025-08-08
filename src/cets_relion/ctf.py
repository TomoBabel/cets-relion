import warnings
from typing import Optional
from gemmi import cif
from logging import getLogger
from src.cets_relion.relion_reader import RelionPipeline
from src.models.models import CTFMetadata

logger = getLogger(__name__)


class RelionCtfStarFile(object):
    """Object for handling the output file from a CtfFind job

    Attrs:
        name: Relative path for the file
    """

    def __init__(self, file_name: str) -> None:
        self.name = file_name

    def get_tilt_series_ctf_file(self, ts_name: str) -> str:
        """Get the path of star file containing ctfinfo tilt series images

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

    def get_tilt_image_ctf(self, image_name: str) -> Optional[CTFMetadata]:
        """Get CTF  info for a tilt image from a tilt series

        Args:
            image_name (str): The name of the movie frame image

        Returns:
            Optional[CTFMetadata]: CETS CTFMetadata object or None if tilt image not found
        """
        # read the starfile
        tsstar = cif.read_file(self.get_tilt_series_ctf_file(image_name))
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
        return CTFMetadata(defocus_u=vals[0], defocus_v=vals[1], defocus_angle=vals[2])


def get_tilt_series_main_starfile(
    file_name: str, ts_name: str, pipeline_name: str = "default_pipeline.star"
) -> str:
    """
    Given a file and the name of a tilt series find the CtfFind job used to determine
    its ctf and get the main results file from that job.

    Args:
         file_name (str): The file to start the search backward from
         ts_name (str): Name of the tilt series
         pipeliner_name(str): Name of the pipeline file

    Returns:
        str: Path of the global results file from the appropriate CtfFind job
    """

    # find the global ctffind file(s)
    pipeline = RelionPipeline(pipeline_name)
    ctf_files = pipeline.last_upstream_file_of_type(
        start=file_name, relion_type=["TomogramGroupMetadata"], kwds=["ctffind"]
    )

    # get the tomogram file(s)
    tomo_starfile = []
    for ctf_file in ctf_files:
        ts_file = RelionCtfStarFile(ctf_file).get_tilt_series_ctf_file(ts_name=ts_name)
        if ts_file:
            tomo_starfile.append(ts_file)

    # there should only be one tomogram file for the TS_name
    if len(tomo_starfile) > 1:
        warnings.warn(
            "Multiple tilt series starfiles were found. This should not happen! Using"
            " the first file found"
        )
    return tomo_starfile[0]
