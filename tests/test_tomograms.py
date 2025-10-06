from cets_relion.tomograms import RelionTomosStarfile
from tests.testing_tools import CetsRelionTest
from pathlib import Path
from pytest import fixture
from cets_data_model.models.models import Tomogram
from cets_relion.objs.coordinate_systems import RELION_COORDS_LOGICAL


class TestRelionParticlesStarFile(CetsRelionTest):
    @fixture(autouse=True)
    def _mock_get_mrc_dims(self, monkeypatch):
        monkeypatch.setattr(
            "cets_relion.tomograms.get_mrc_dims",
            lambda *args, **kwargs: (1, 2, 3),
        )


class TomogramsTests(CetsRelionTest):
    def test_instantiate_subtomos_object(self):
        self.setup_dirs(jobs_to=10)
        tomos = RelionTomosStarfile(file_name="Tomograms/job006/tomograms.star")
        assert tomos.name == "Tomograms/job006/tomograms.star"
        assert tomos.file == Path("Tomograms/job006/tomograms.star")

    def test_get_tomogram_halfset(self):
        self.setup_dirs(jobs_to=6)
        tomos = RelionTomosStarfile(file_name="Tomograms/job006/tomograms.star")
        assert tomos.get_reconstructed_tomo("TS_01") is None

    def test_get_tomgram_merged(self):
        self.setup_dirs(jobs_to=8)
        tomos = RelionTomosStarfile(file_name="Denoise/job008/tomograms.star")
        assert tomos.get_reconstructed_tomo("TS_01") == (
            "Denoise/job008/tomograms/rec_TS_01.mrc"
        )

    def test_get_cets_from_denoise_job(self):
        self.setup_dirs(jobs_to=8)
        tomos = RelionTomosStarfile(file_name="Denoise/job008/tomograms.star")
        assert tomos.get_cets_tomo("TS_01") == Tomogram(
            width=4000,
            height=4000,
            depth=2000,
            coordinate_systems=[RELION_COORDS_LOGICAL],
            coordinate_transformations=None,
            path="Denoise/job008/tomograms/rec_TS_01.mrc",
        )

    def test_get_all_tomo_names(self):
        self.setup_dirs(8)
        mf = RelionTomosStarfile("Denoise/job008/tomograms.star")
        assert mf.get_all_tomo_names() == ["TS_01", "TS_03", "TS_43", "TS_45", "TS_54"]
