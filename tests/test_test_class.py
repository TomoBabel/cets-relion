import os
from tests.testing_tools import CetsRelionTest
from pathlib import Path


class RelionCetsMoviesTests(CetsRelionTest):
    def test_setup_dirs_through_job10(self):
        self.setup_dirs(10)
        jobs = Path(os.getcwd()).glob("*/job*")
        exp = [f"job{n + 1:03d}" for n in range(10)]
        exp.sort()
        actual = [str(x).split("/")[-1] for x in jobs]
        actual.sort()
        assert exp == actual
        assert Path("default_pipeline.star").is_file()

    def test_setup_dirs_all(self):
        self.setup_dirs()
        jobs = Path(os.getcwd()).glob("*/job*")
        exp = [f"job{n + 1:03d}" for n in range(80)]
        exp.sort()
        actual = [str(x).split("/")[-1] for x in jobs]
        actual.sort()
        assert exp == actual
        assert Path("default_pipeline.star").is_file()
