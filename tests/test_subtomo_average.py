from tests.test_testing_tools import CetsRelionTest
from tests.test_data.results.particle_map_objs import (
    FROM_REFINE,
    FROM_PP,
    FROM_REC,
)
from cets_relion.subtomo_averages import RelionSubtomoAverage
from pathlib import Path
from unittest.mock import patch
from pytest import fixture


@fixture(autouse=True)
def mock_get_mrc_dims():
    with patch("cets_relion.particle_coords.get_mrc_dims") as mock:
        mock.return_value = (127, 127, 127)
        yield mock


class TestRelionSubtomoAverage(CetsRelionTest):
    def test_instantiate_subtomo_average_from_refine3D(self):
        self.setup_dirs(12)
        sta = RelionSubtomoAverage("Refine3D/job012/run_class001.mrc")
        assert sta.__dict__ == {
            "file_name": "Refine3D/job012/run_class001.mrc",
            "particles": "Refine3D/job012/run_data.star",
            "path": Path("Refine3D/job012/run_class001.mrc"),
            "tomos": "Denoise/job008/tomograms.star",
            "opt_set": Path("Refine3D/job012/run_optimisation_set.star"),
        }

    def test_instantiate_subtomo_average_from_class3D(self):
        self.setup_dirs(17)
        with self.assertRaises(NotImplementedError):
            RelionSubtomoAverage("Class3D/job017/run_it025_class001.mrc")

    def test_instantiate_subtomo_average_from_reconstruct(self):
        self.setup_dirs(21)
        sta = RelionSubtomoAverage("Reconstruct/job021/merged.mrc")
        assert sta.__dict__ == {
            "file_name": "Reconstruct/job021/merged.mrc",
            "particles": "Extract/job020/particles.star",
            "path": Path("Reconstruct/job021/merged.mrc"),
            "tomos": "Denoise/job008/tomograms.star",
            "opt_set": Path("Extract/job020/optimisation_set.star"),
        }

    def test_instantiate_subtomo_average_from_postprocess(self):
        self.setup_dirs(49)
        sta = RelionSubtomoAverage("PostProcess/job049/postprocessed.mrc")
        assert sta.__dict__ == {
            "file_name": "PostProcess/job049/postprocessed.mrc",
            "particles": "Refine3D/job044/run_data.star",
            "path": Path("PostProcess/job049/postprocessed.mrc"),
            "tomos": "Polish/job040/tomograms.star",
            "opt_set": Path("Refine3D/job044/run_optimisation_set.star"),
        }

    def test_get_cets_average_from_refine(self):
        self.setup_dirs(12)
        sta = RelionSubtomoAverage("Refine3D/job012/run_class001.mrc")
        avg = sta.get_cets_average()
        assert avg.name == "Refine3D/job012/run_class001.mrc"
        assert len(avg.particle_maps) == 30596
        assert avg.particle_maps[0] == FROM_REFINE

    def test_get_cets_average_from_class3D(self):
        self.setup_dirs(17)
        with self.assertRaises(NotImplementedError):
            RelionSubtomoAverage("Class3D/job017/run_it025_class001.mrc")

    def test_get_cets_average_from_reconstruct(self):
        self.setup_dirs(21)
        sta = RelionSubtomoAverage("Reconstruct/job021/merged.mrc")
        avg = sta.get_cets_average()
        assert len(avg.particle_maps) == 9442
        assert avg.particle_maps[0] == FROM_REC

    def test_get_cets_average_from_postprocess(self):
        self.setup_dirs(49)
        sta = RelionSubtomoAverage("PostProcess/job049/postprocessed.mrc")
        avg = sta.get_cets_average()
        assert len(avg.particle_maps) == 9053
        assert avg.particle_maps[0] == FROM_PP
