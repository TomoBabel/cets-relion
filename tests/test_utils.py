from cets_relion.utils import (
    get_job_name,
    joboptions_from_job,
    get_job_number,
    get_job_type,
    affine_to_eulers,
    relion_eulers_to_matrix,
    rotation_to_matrix_3d,
    rotation_to_matrix_2d,
    matrix_2d_to_angle,
)
from tests.testing_tools import CetsRelionTest


class UtilsTests(CetsRelionTest):
    def test_joboptions_from_jobstar(self):
        jobstar = self.test_data / "skeleton_project/Import/job001/"
        jobops = joboptions_from_job(jobstar)
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


def test_euler_to_matrix():
    # testing with values from first subtomo in TS_03
    rot, tilt, psi = (-1.40135, 97.396086, 4.337919)
    m = relion_eulers_to_matrix(rot, tilt, psi)
    assert m == [
        [-0.1264708962411244, -0.07875515190078805, 0.988839086228417],
        [-0.03411956457485091, 0.9965989433656185, 0.07500934205654208],
        [-0.9913833606215051, -0.024252260340359096, -0.12872785305128842],
    ]


def test_matrix_to_eulers():
    rtp = affine_to_eulers(
        [
            [-0.1264708962411244, -0.07875515190078805, 0.988839086228417],
            [-0.03411956457485091, 0.9965989433656185, 0.07500934205654208],
            [-0.9913833606215051, -0.024252260340359096, -0.12872785305128842],
        ]
    )
    assert [round(x, 6) for x in rtp] == [-1.40135, 97.396086, 4.337919]


def test_rotation_to_matrix3d():
    r = rotation_to_matrix_3d(45, "x")
    assert r == [
        [1.0, 0.0, 0.0],
        [0.0, 0.7071067811865475, -0.7071067811865476],
        [0.0, 0.7071067811865476, 0.7071067811865475],
    ]
    r = rotation_to_matrix_3d(45, "y")
    assert r == [
        [0.7071067811865475, 0.0, 0.7071067811865476],
        [0.0, 1.0, 0.0],
        [-0.7071067811865476, 0.0, 0.7071067811865475],
    ]
    r = rotation_to_matrix_3d(45, "z")
    assert r == [
        [0.7071067811865475, -0.7071067811865476, 0.0],
        [0.7071067811865476, 0.7071067811865475, 0.0],
        [0.0, 0.0, 1.0],
    ]


def test_rotations_to_matrix_2d():
    r = rotation_to_matrix_2d(45)
    assert r == [
        [0.7071067811865476, -0.7071067811865475],
        [0.7071067811865475, 0.7071067811865476],
    ]


def test_matrix_to_angle_2d():
    r = [
        [0.7071067811865476, -0.7071067811865475],
        [0.7071067811865475, 0.7071067811865476],
    ]
    assert round(matrix_2d_to_angle(r), 6) == 45.0
