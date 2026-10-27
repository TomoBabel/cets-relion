from unittest.mock import patch


from cets_relion.relion_to_cets import tilt_series
from cets_data_model.models.models import CTFMetadata, TiltImage
from tests.testing_tools import CetsRelionTest, load_result
from cets_relion.relion_to_cets.tilt_series import RelionTiltSeriesStarfile


class TiltSeriesStarTest(CetsRelionTest):
    """Exclude is the first job without a specific subclass"""

    def setUp(self):
        super().setUp()

        self.get_mrc_dims_patch = patch.object(
            tilt_series,
            "get_mrc_dims",
            return_value=(2000, 2000, 1),
        )
        self.get_mrc_dims_patch.start()
        self.addCleanup(self.get_mrc_dims_patch.stop)

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
        assert ctf.get_tilt_image_ctfs(ts_name="TS_01") == {
            k: CTFMetadata.model_validate(v)
            for k, v in load_result("ctfs.json").items()
        }

    def test_get_tilt_image_dose_dict(self):
        self.setup_dirs(jobs_to=3)
        ts = RelionTiltSeriesStarfile("CtfFind/job003/tilt_series_ctf.star")
        assert ts.get_tilt_image_doses("TS_01") == load_result("ts_01_doses.json")

    def test_get_tilt_projections_cets_objs_no_alignments(self):
        self.setup_dirs(jobs_to=3)
        ts = RelionTiltSeriesStarfile("CtfFind/job003/tilt_series_ctf.star")
        assert ts.get_cets_tilt_images("TS_01") == [
            TiltImage.model_validate(x) for x in load_result("proj.json")
        ]

    def test_make_cets_projection_image_object_with_alignments(self):
        self.setup_dirs(jobs_to=5)
        ts = RelionTiltSeriesStarfile("AlignTiltSeries/job005/aligned_tilt_series.star")
        assert ts.get_cets_tilt_images("TS_01") == [
            TiltImage.model_validate(x) for x in load_result("proj_aligned.json")
        ]

    def test_get_all_tomo_names(self):
        self.setup_dirs(5)
        mf = RelionTiltSeriesStarfile("AlignTiltSeries/job005/aligned_tilt_series.star")
        assert mf.get_all_tomo_names() == ["TS_01", "TS_03", "TS_43", "TS_45", "TS_54"]
