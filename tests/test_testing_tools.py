from tests.testing_tools import CetsRelionTest


class TestTestingTools(CetsRelionTest):
    def test_setup_dir_with_default_pipeline(self):
        self.setup_dirs(10)
        dirs = sorted([x.parts[-1] for x in self.test_dir.glob("*")])
        assert dirs == [
            "AlignTiltSeries",
            "CtfFind",
            "Denoise",
            "ExcludeTiltImages",
            "Extract",
            "Import",
            "MotionCorr",
            "Picks",
            "Tomograms",
            "default_pipeline.star",
        ]
        with open("Extract/job010/default_pipeline.star") as exp:
            expected = exp.read()
        with open("default_pipeline.star") as act:
            actual = act.read()
        assert expected == actual

    def test_setup_dir_with_custom_pipeline(self):
        self.setup_dirs(10, pipeline="short_pipeline.star")
        with open("default_pipeline.star") as act:
            actual = act.read()
        with open(self.test_data / "pipelines/short_pipeline.star") as exp:
            expected = exp.read()
        assert expected == actual
