from cets_relion.subtomograms import RelionSubTomosStarfile
from tests.testing_tools import CetsRelionTest
from pathlib import Path
from cets_relion.relion_reader import RelionPipeline
from unittest.mock import patch


class SubTomogramsTests(CetsRelionTest):
    def test_instantiate_subtomos_object(self):
        self.setup_dirs(jobs_to=10)
        sub = RelionSubTomosStarfile("Extract/job010/particles.star")
        assert sub.name == "Extract/job010/particles.star"
        assert isinstance(sub.file, Path)
        assert str(sub.file) == "Extract/job010/particles.star"
        assert isinstance(sub.pipeline, RelionPipeline)
        assert len(sub.subtomos) == 30596
        assert sub.subtomos[0] == [
            "Extract/job010/Subtomograms/TS_01/1_stack2d.mrcs",
            1,
            "TS_01/1",
            1771.079893,
            -846.9901,
            1176.862669,
        ]
        assert len(sub.subtomo_orientations) == 30596
        assert sub.subtomo_orientations[0] == [
            "Extract/job010/Subtomograms/TS_01/1_stack2d.mrcs",
            -177.41074,
            90.33369,
            -97.33852,
        ]
        assert len(sub.subtomo_alignments) == 30596
        assert sub.subtomo_alignments[0] == [
            "Extract/job010/Subtomograms/TS_01/1_stack2d.mrcs",
            90.0,
            0.0,
            0.0,
        ]

    # mocking the return of matrix until type is fixed in cets-model
    @patch("cets_relion.subtomograms.relion_eulers_to_matrix")
    def test_get_subtomo(self, matrix_mock):
        matrix_mock.return_value = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.setup_dirs(jobs_to=10)
        sub = RelionSubTomosStarfile("Extract/job010/particles.star")
        subtomo = sub.get_subtomo("Extract/job010/Subtomograms/TS_01/1_stack2d.mrcs")
        print(subtomo.__dict__)
