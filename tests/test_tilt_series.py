from tests.testing_tools import CetsRelionTest
from src.cets_relion.tilt_series import RelionTiltSeriesStarfile
from src.cets_relion.relion_reader import RelionPipeline


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
