from unittest.mock import patch

from pytest import fixture
from tests.testing_tools import CetsRelionTest
from cets_relion.tilt_series import RelionTiltSeriesStarfile
from tests.test_data.results import proj, proj_aligned
from tests.test_data.results.ts_01_doses import DOSES
from tests.test_data.results.ctfs import CTFS


@fixture(autouse=True)
def mock_get_mrc_dims():
    with patch("cets_relion.tilt_series.get_mrc_dims") as mock:
        mock.return_value = (2000, 2000, 8)
        yield mock


class TiltSeriesStarTest(CetsRelionTest):
    """Exclude is the first job without a specific subclass"""

    def test_instantiate_RelionTiltSeriesStarfileBase(self):
        self.setup_dirs(4)
        tssf = RelionTiltSeriesStarfile(
            "ExcludeTiltSeries/job004/selected_tilt_series.star",
        )
        assert tssf.name == "ExcludeTiltSeries/job004/selected_tilt_series.star"

    def test_name_in_ts_file(self):
        self.setup_dirs(2)
        tssf = RelionTiltSeriesStarfile("MotionCorr/job002/corrected_tilt_series.star")
        assert tssf.tilt_series_in_file("TS_01")
        assert not tssf.tilt_series_in_file("NOT THERE")

    def test_instantiate_RelionTiltSeriesStarfile(self):
        self.setup_dirs(4)
        tssf = RelionTiltSeriesStarfile(
            "ExcludeTiltSeries/job004/selected_tilt_series.star",
        )
        assert tssf.name == "ExcludeTiltSeries/job004/selected_tilt_series.star"

    def test_get_tilt_image_ctfs(self):
        self.setup_dirs(jobs_to=3)
        ctf = RelionTiltSeriesStarfile("CtfFind/job003/tilt_series_ctf.star")
        assert ctf.get_tilt_image_ctfs(ts_name="TS_01") == CTFS

    def test_get_tilt_image_dose_dict(self):
        self.setup_dirs(jobs_to=3)
        ts = RelionTiltSeriesStarfile("CtfFind/job003/tilt_series_ctf.star")
        assert ts.get_tilt_image_doses("TS_01") == DOSES

    def test_get_tilt_projections_cets_objs_no_alignments(self):
        self.setup_dirs(jobs_to=3)
        ts = RelionTiltSeriesStarfile("CtfFind/job003/tilt_series_ctf.star")
        assert ts.get_cets_projection_images("TS_01") == proj.RESULT

    def test_make_cets_projection_image_object_1ith_alignments(self):
        self.setup_dirs(jobs_to=5)
        ts = RelionTiltSeriesStarfile("AlignTiltSeries/job005/aligned_tilt_series.star")
        assert ts.get_cets_projection_images("TS_01") == proj_aligned.RESULT

    def test_get_all_tomo_names(self):
        self.setup_dirs(5)
        mf = RelionTiltSeriesStarfile("AlignTiltSeries/job005/aligned_tilt_series.star")
        assert mf.get_all_tomo_names() == ["TS_01", "TS_03", "TS_43", "TS_45", "TS_54"]
