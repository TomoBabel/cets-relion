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

    def setup_dirs(self, jobs_to: int = 80, pipeline: str = "DEFAULT"):
        skele = self.test_data / "skeleton_project"

        if pipeline != "DEFAULT":
            shutil.copy(
                self.test_data / f"pipelines/{pipeline}", "default_pipeline.star"
            )
        else:
            pipeline_file = list(
                skele.glob(f"*/job{jobs_to:03d}/default_pipeline.star")
            )[0]
            shutil.copy(pipeline_file, "default_pipeline.star")

        jobs = list(skele.glob("*/job*"))
        jobs.sort(key=lambda x: int(str(x)[-3:]))
        for n in range(jobs_to):
            shutil.copytree(jobs[n], jobs[n].relative_to(skele))


# for debugging big dicts when IDE fails
def find_differences(actual, expected, path="$"):
    if type(actual) is not type(expected):
        print(
            f"{path}: type mismatch: "
            f"{type(actual).__name__} != {type(expected).__name__}"
        )
        return

    if isinstance(actual, dict):
        for key in actual.keys() | expected.keys():
            if key not in actual:
                print(f"{path}.{key}: missing from actual")
            elif key not in expected:
                print(f"{path}.{key}: missing from expected")
            else:
                find_differences(actual[key], expected[key], f"{path}.{key}")

    elif isinstance(actual, list):
        if len(actual) != len(expected):
            print(f"{path}: length mismatch: {len(actual)} != {len(expected)}")
        for i, (a, e) in enumerate(zip(actual, expected)):
            find_differences(a, e, f"{path}[{i}]")

    elif actual != expected:
        print(f"{path}: {actual!r} != {expected!r}")
