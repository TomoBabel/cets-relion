from src.cets_relion.subtomograms import RelionSubTomosStarfile
from tests.testing_tools import CetsRelionTest
from pathlib import Path
from src.cets_relion.relion_reader import RelionPipeline


class SubTomogramsTests(CetsRelionTest):
    def test_instantiate_subtomos_object(self):
        self.setup_dirs(jobs_to=10)
        sub = RelionSubTomosStarfile("Extract/job010/particles.star")
        assert sub.name == "Extract/job010/particles.star"
        assert isinstance(sub.file, Path)
        assert str(sub.file) == "Extract/job010/particles.star"
        assert isinstance(sub.pipeline, RelionPipeline)

    def test_get_subtomograms(self):
        self.setup_dirs(jobs_to=10)
        sub = RelionSubTomosStarfile(file_name="Extract/job010/particles.star")
        subtomos = sub.get_all_subtomos("TS_01")
        assert len(subtomos) == 6623
        assert [str(x) for x in subtomos[:3]] == [
            "Extract/job010/Subtomograms/TS_01/1_stack2d.mrcs",
            "Extract/job010/Subtomograms/TS_01/2_stack2d.mrcs",
            "Extract/job010/Subtomograms/TS_01/3_stack2d.mrcs",
        ]
        assert [str(x) for x in subtomos[-3:]] == [
            "Extract/job010/Subtomograms/TS_01/6979_stack2d.mrcs",
            "Extract/job010/Subtomograms/TS_01/6980_stack2d.mrcs",
            "Extract/job010/Subtomograms/TS_01/6981_stack2d.mrcs",
        ]
