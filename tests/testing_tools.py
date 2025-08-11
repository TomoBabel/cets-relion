import os
import shutil
import tempfile
import unittest
from pathlib import Path


class CetsRelionTest(unittest.TestCase):
    def setUp(self):
        """
        Setup test data and output directories.
        """
        self.test_dir = Path(tempfile.mkdtemp(prefix="cets_relion_test"))
        # Change to test directory
        self._orig_dir = os.getcwd()
        os.chdir(self.test_dir)
        self.test_data = Path(__file__).parent / "test_data"

    def tearDown(self):
        os.chdir(self._orig_dir)
        if self.test_dir.is_dir():
            shutil.rmtree(self.test_dir)

    def setup_dirs(self, jobs_to: int = 80, pipeline: str = "default_pipeline.star"):
        skele = self.test_data / "skeleton_project"
        shutil.copy(self.test_data / f"pipelines/{pipeline}", "default_pipeline.star")
        jobs = list(skele.glob("*/job*"))
        jobs.sort(key=lambda x: int(str(x)[-3:]))
        for n in range(jobs_to):
            shutil.copytree(jobs[n], jobs[n].relative_to(skele))
