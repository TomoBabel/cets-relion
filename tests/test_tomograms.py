from tests.testing_tools import CetsRelionTest
from src.cets_relion.tomograms import RelionTomosStarfile


class TomogramsTests(CetsRelionTest):
    def test_get_tomogram_halfset(self):
        self.setup_dirs(jobs_to=6)
        tomos = RelionTomosStarfile(file_name="Tomograms/job006/tomograms.star")
        assert tomos.get_reconstructed_tomo("TS_01") == (
            "Tomograms/job006/tomograms/rec_TS_01_half1.mrc",
            False,
        )

    def test_get_tomgram_merged(self):
        self.setup_dirs(jobs_to=8)
        tomos = RelionTomosStarfile(file_name="Denoise/job008/tomograms.star")
        assert tomos.get_reconstructed_tomo("TS_01") == (
            "Denoise/job008/tomograms/rec_TS_01.mrc",
            True,
        )
