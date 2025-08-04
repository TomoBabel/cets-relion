from src.cets_relion.relion_reader import RelionPipeline
from tests.testing_tools import CetsRelionTest


class PipelineReaderTests(CetsRelionTest):
    def test_instatiate_RelionPipeline_obj(self):
        rp = RelionPipeline(self.test_data / "short_pipeline.star")
        assert list(rp.graph.nodes()) == [
            "Import/job001/",
            "MotionCorr/job002/",
            "CtfFind/job003/",
            "ExcludeTiltImages/job004/",
            "AlignTiltSeries/job005/",
            "Tomograms/job006/",
            "Denoise/job007/",
            "Denoise/job008/",
            "Import/job001/tilt_series.star",
            "MotionCorr/job002/corrected_tilt_series.star",
            "MotionCorr/job002/logfile.pdf",
            "CtfFind/job003/tilt_series_ctf.star",
            "CtfFind/job003/logfile.pdf",
            "ExcludeTiltImages/job004/selected_tilt_series.star",
            "AlignTiltSeries/job005/aligned_tilt_series.star",
            "Tomograms/job006/tomograms.star",
            "Denoise/job007/tomograms.star",
            "Denoise/job008/tomograms.star",
        ]
        assert list(rp.graph.edges()) == [
            ("Import/job001/", "Import/job001/tilt_series.star"),
            ("MotionCorr/job002/", "MotionCorr/job002/corrected_tilt_series.star"),
            ("MotionCorr/job002/", "MotionCorr/job002/logfile.pdf"),
            ("CtfFind/job003/", "CtfFind/job003/tilt_series_ctf.star"),
            ("CtfFind/job003/", "CtfFind/job003/logfile.pdf"),
            (
                "ExcludeTiltImages/job004/",
                "ExcludeTiltImages/job004/selected_tilt_series.star",
            ),
            (
                "AlignTiltSeries/job005/",
                "AlignTiltSeries/job005/aligned_tilt_series.star",
            ),
            ("Tomograms/job006/", "Tomograms/job006/tomograms.star"),
            ("Denoise/job007/", "Denoise/job007/tomograms.star"),
            ("Denoise/job008/", "Denoise/job008/tomograms.star"),
            ("Import/job001/tilt_series.star", "MotionCorr/job002/"),
            ("MotionCorr/job002/corrected_tilt_series.star", "CtfFind/job003/"),
            ("CtfFind/job003/tilt_series_ctf.star", "ExcludeTiltImages/job004/"),
            (
                "ExcludeTiltImages/job004/selected_tilt_series.star",
                "AlignTiltSeries/job005/",
            ),
            ("AlignTiltSeries/job005/aligned_tilt_series.star", "Tomograms/job006/"),
            ("Tomograms/job006/tomograms.star", "Denoise/job007/"),
            ("Tomograms/job006/tomograms.star", "Denoise/job008/"),
        ]
