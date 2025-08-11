from src.cets_relion.tilt_series import RelionTiltSeriesStarfile
from src.cets_relion.relion_reader import RelionPipeline
import warnings


class RelionMotionCorrStarFile(RelionTiltSeriesStarfile):
    def __init__(self, file_name: str):
        super().__init__(file_name=file_name)

    def get_gain_file(self):
        return self.get_joboptions().get("fn_gain_ref")

    def get_defect_file(self):
        return self.get_joboptions().get("fn_defect")


def get_tilt_series_main_mocorr_starfile(
    file_name: str, ts_name: str, pipeline_name: str = "default_pipeline.star"
) -> str:
    """
    Given a file and the name of a tilt series find the MotionCorr job used to determine
    generate its corrected images and get the main results file from that job.

    Args:
         file_name (str): The file to start the search backward from
         ts_name (str): Name of the tilt series
         pipeline_name(str): Name of the pipeline file

    Returns:
        str: Path of the global results file from the appropriate CtfFind job
    """

    # find the global ctffind file(s)
    pipeline = RelionPipeline(pipeline_name)
    mc_files = pipeline.last_upstream_file_of_type(
        start=file_name, relion_type=["TomogramGroupMetadata"], kwds=["motioncorr"]
    )

    # get the tomogram file(s)
    tomo_starfile = []
    for mc_file in mc_files:
        ts_file = RelionMotionCorrStarFile(mc_file).get_tilt_series_star_file(
            ts_name=ts_name
        )
        if ts_file:
            tomo_starfile.append(ts_file)

    # there should only be one tomogram file for the TS_name
    if len(tomo_starfile) > 1:
        warnings.warn(
            "Multiple tilt series starfiles were found. This should not happen! Using"
            " the first file found"
        )
    return tomo_starfile[0]
