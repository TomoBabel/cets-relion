from cets_relion.motion_corr import RelionMotionCorrStarFile
from tests.testing_tools import CetsRelionTest
from pathlib import Path
from unittest.mock import patch
from tests.test_data.results.ts_01_doses import DOSES


class TestMotionCorr(CetsRelionTest):
    def test_instantiate_motion_corr(self):
        self.setup_dirs(2)
        mco = RelionMotionCorrStarFile("MotionCorr/job002/corrected_tilt_series.star")
        assert mco.name == "MotionCorr/job002/corrected_tilt_series.star"
        assert mco.file == Path("MotionCorr/job002/corrected_tilt_series.star")

    def test_get_gain_file(self):
        self.setup_dirs(2)
        mco = RelionMotionCorrStarFile("MotionCorr/job002/corrected_tilt_series.star")
        assert mco.get_gain_file() == "gain_reference.mrc"

    def test_get_defect_file_empty(self):
        """No defect file in the test data"""
        self.setup_dirs(2)
        mco = RelionMotionCorrStarFile("MotionCorr/job002/corrected_tilt_series.star")
        assert mco.get_defect_file() is None

    @patch("cets_relion.motion_corr.joboptions_from_job")
    def test_get_defect_file(self, mock_jo):
        """No defect file in the test data"""
        mock_jo.return_value = {"fn_defect": "defect.mrc"}
        self.setup_dirs(2)
        mco = RelionMotionCorrStarFile("MotionCorr/job002/corrected_tilt_series.star")
        assert mco.get_defect_file() == "defect.mrc"

    def test_ctf_not_implemented_error(self):
        self.setup_dirs(2)
        mco = RelionMotionCorrStarFile("MotionCorr/job002/corrected_tilt_series.star")
        with self.assertRaises(NotImplementedError):
            mco.get_tilt_image_ctfs("TS_01")

    def test_get_tilt_image_doses(self):
        self.setup_dirs(2)
        mco = RelionMotionCorrStarFile("MotionCorr/job002/corrected_tilt_series.star")
        assert mco.get_tilt_image_doses("TS_01") == DOSES
