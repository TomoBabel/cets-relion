from cets_relion.utils import (
    get_job_name,
    joboptions_from_jobstar_file,
    get_job_number,
    get_job_type,
)
from tests.testing_tools import CetsRelionTest


class UtilsTests(CetsRelionTest):
    def test_joboptions_from_jobstar(self):
        jobstar = self.test_data / "skeleton_project/Import/job001/job.star"
        jobops = joboptions_from_jobstar_file(jobstar)
        assert jobops == {
            "Cs": "2.7",
            "Q0": "0.1",
            "angpix": "0.675",
            "do_queue": "No",
            "dose_is_per_movie_frame": "No",
            "dose_rate": "3",
            "flip_tiltseries_hand": "Yes",
            "images_are_motion_corrected": "No",
            "kV": "300",
            "mdoc_files": "mdoc/*.mdoc",
            "min_dedicated": "24",
            "movie_files": "frames/*.mrc",
            "mtf_file": "",
            "optics_group_name": "optics1",
            "other_args": "",
            "prefix": "",
            "qsub": "sbatch",
            "qsubscript": "/public/EM/RELION/relion-slurm-gpu-4.0.csh",
            "queuename": "openmpi",
            "tilt_axis_angle": "85",
        }

    def test_get_job_type(self):
        job = self.test_data / "skeleton_project/Import/job001"
        assert get_job_type(job) == "relion.importtomo"


def test_get_job_name():
    assert str(get_job_name("Reconstruct/job001/")) == "Reconstruct/job001"
    assert str(get_job_name("Denoise/job008/tomograms.star")) == "Denoise/job008"
    assert str(get_job_name("Denoise/job008/tomograms/ts_01.star")) == "Denoise/job008"
    assert (
        str(get_job_name("Other/Dirs/Denoise/job008/tomograms/ts_01.star"))
        == "Denoise/job008"
    )


def test_get_job_number():
    assert get_job_number("Reconstruct/job001/") == 1
    assert get_job_number("Denoise/job008/tomograms.star") == 8
    assert get_job_number("Denoise/job008/tomograms/ts_01.star") == 8
