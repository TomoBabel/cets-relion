from pytest import fixture
from unittest.mock import patch
from tests.testing_tools import CetsRelionTest
from src.cets_relion.tilt_series import RelionTiltSeriesStarfile
from src.cets_relion.relion_reader import RelionPipeline


@fixture(autouse=True)
def mock_get_image_size():
    with patch("src.cets_relion.utils.get_image_dims") as mock:
        mock.return_value = (2000, 2000, 8)
        yield mock


class TiltSeriesStarTest(CetsRelionTest):
    def test_instantiate_RelionTiltSeriesStarfile(self):
        self.setup_dirs(2)
        tssf = RelionTiltSeriesStarfile("MotionCorr/job002/corrected_tilt_series.star")
        assert tssf.name == "MotionCorr/job002/corrected_tilt_series.star"
        assert isinstance(tssf.pipeline, RelionPipeline)

    def test_name_in_ts_file(self):
        self.setup_dirs(2)
        tssf = RelionTiltSeriesStarfile("MotionCorr/job002/corrected_tilt_series.star")
        assert tssf.tilt_series_in_file("TS_01")
        assert not tssf.tilt_series_in_file("NOT THERE")

    def test_get_raw_data_movies_from_motioncorr(self):
        self.setup_dirs(2)
        tssf = RelionTiltSeriesStarfile("MotionCorr/job002/corrected_tilt_series.star")
        result = tssf.get_raw_files()
        assert len(result) == 1
        assert result[0] == "Import/job001/tilt_series.star"

    def test_get_raw_data_movies_from_refine(self):
        self.setup_dirs(74)
        tssf = RelionTiltSeriesStarfile("Refine3D/job074/run_data.star")
        result = tssf.get_raw_files()
        assert len(result) == 1
        assert result[0] == "Import/job001/tilt_series.star"

    def test_get_tomos_from_reconstruct_job(self):
        """This job only has halfmaps, so tomograms are found"""
        self.setup_dirs(6)
        tssf = RelionTiltSeriesStarfile("Tomograms/job006/tomograms.star")
        assert tssf.find_tomograms_in_self("TS_01") == []

    def test_get_tomos_from_denoise_job(self):
        """Shoulf return the tomos from this job"""
        self.setup_dirs(8)
        tssf = RelionTiltSeriesStarfile("Denoise/job008/tomograms.star")
        assert tssf.find_tomograms_in_self("TS_01") == [
            "Denoise/job008/tomograms/rec_TS_01.mrc"
        ]

    def test_get_tomos_from_other_jobs_downstream_job(self):
        """Should find the tomos from downstream denoise tomograms"""
        self.setup_dirs(8)
        tssf = RelionTiltSeriesStarfile("Tomograms/job006/tomograms.star")
        assert tssf.find_tomograms_in_other_jobs("TS_01") == [
            "Denoise/job008/tomograms/rec_TS_01.mrc"
        ]

    def test_general_get_tomos_tomos_are_in_other_job(self):
        self.setup_dirs(8)
        tssf = RelionTiltSeriesStarfile("Tomograms/job006/tomograms.star")
        assert tssf.find_tomgrams("TS_01") == ["Denoise/job008/tomograms/rec_TS_01.mrc"]

    def test_general_get_tomos_tomos_are_in_self(self):
        self.setup_dirs(8)
        tssf = RelionTiltSeriesStarfile("Denoise/job008/tomograms.star")
        assert tssf.find_tomgrams("TS_01") == ["Denoise/job008/tomograms/rec_TS_01.mrc"]
