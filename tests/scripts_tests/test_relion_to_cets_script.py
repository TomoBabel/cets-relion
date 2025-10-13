from tests.testing_tools import CetsRelionTest
from pytest import fixture
from unittest.mock import patch
from cets_relion.scripts.relion_to_cets import (
    get_raw_movies,
    get_tilt_series,
)
from cets_relion.relion_to_cets_converter import RelionCetsConverter
import json
from tests.test_data.results.tilt_series_objs import (
    MOCORR_0,
    MOCORR_40,
    CTF_0,
    CTF_40,
    GAIN_FILE,
)


@fixture(autouse=True)
def mock_get_image_size_main():
    with patch("cets_relion.relion_to_cets_converter.get_mrc_dims") as mock:
        mock.return_value = (1000, 1000, 8)
        yield mock


class RelionCETSConverterScriptTestRawMovies(CetsRelionTest):
    @staticmethod
    @fixture(autouse=True)
    def mock_get_image_size_movies():
        with patch("cets_relion.movies.get_image_dims") as mock:
            mock.return_value = (2000, 2000, 8)
            yield mock

    def test_get_raw_movies_only_import_dir_available(self):
        self.setup_dirs(1)
        con = RelionCetsConverter("Import/job001/")
        movs = get_raw_movies(con, "TS_01")
        actual = movs[0].model_dump(mode="json")
        with open(self.test_data / "results/raw_movs_no_ctf.json", "w") as f:
            json.dump(actual, f, indent=2)
        with open(self.test_data / "results/raw_movs_no_ctf.json") as f:
            expected = json.load(f)
        assert actual == expected

    def test_get_raw_movies_mocorr(self):
        self.setup_dirs(2)
        con = RelionCetsConverter("MotionCorr/job002/")
        movs = get_raw_movies(con, "TS_01")
        actual = movs[0].model_dump(mode="json")
        with open(self.test_data / "results/raw_movs_no_ctf.json") as f:
            expected = json.load(f)
        assert actual["movie_stacks"] == expected["movie_stacks"]
        assert actual["gain_file"] == GAIN_FILE
        assert actual["defect_file"] is None

    def test_get_raw_movies_gain_and_ctf_available(self):
        self.setup_dirs(3)
        con = RelionCetsConverter("CtfFind/job003/")
        movs = get_raw_movies(con, "TS_01")
        actual = movs[0].model_dump(mode="json")
        with open(self.test_data / "results/raw_movs_ctf.json") as f:
            expected = json.load(f)
        assert actual == expected

    def test_get_raw_movies_from_later_job(self):
        self.setup_dirs(30)
        con = RelionCetsConverter("Polish/job030/")
        movs = get_raw_movies(con, "TS_01")
        actual = movs[0].model_dump(mode="json")
        with open(self.test_data / "results/raw_movs_ctf.json") as f:
            expected = json.load(f)
        assert actual == expected


class RelionCETSConverterScriptTestGetTiltSeries(CetsRelionTest):
    @patch("cets_relion.motion_corr.get_mrc_dims")
    def test_get_tilt_series_from_motioncorr(self, mock_dims):
        """The first job that would generate a tilt series item"""
        mock_dims.return_value = (2000, 2000, 8)
        self.setup_dirs(2)
        con = RelionCetsConverter("MotionCorr/job002/")
        ts = get_tilt_series(con, "TS_01")
        assert ts[0].images[0].model_dump(mode="json") == MOCORR_0
        assert ts[0].images[-1].model_dump(mode="json") == MOCORR_40

    @patch("cets_relion.tilt_series.get_mrc_dims")
    def test_get_tilt_series_from_ctf(self, mock_dims):
        """Tilt series with ctf but no alignment"""
        mock_dims.return_value = (2000, 2000, 8)
        self.setup_dirs(3)
        con = RelionCetsConverter("CtfFind/job003/")
        ts = get_tilt_series(con, "TS_01")
        assert ts[0].images[0].model_dump(mode="json") == CTF_0
        assert ts[0].images[-1].model_dump(mode="json") == CTF_40

    # ToDo: Output of dumping transformation objects to JSON is not correct
    #  fix before adding these tests

    # @patch("cets_relion.tilt_series.get_mrc_dims")
    # def test_get_tilt_series_from_aligned(self, mock_dims):
    #     """First job type with alignments, 1 tilt image has been excluded"""
    #     mock_dims.return_value = (2000, 2000, 8)
    #     self.setup_dirs(5)
    #     con = RelionCetsConverter("AlignTiltSeries/job005/")
    #     ts = get_tilt_series(con, "TS_01")
    #     assert len(ts) == 40
    #     assert ts[0].model_dump(mode="json") == {}
    #     assert ts[-1].model_dump(mode="json") == {}
    #
    # @patch("cets_relion.tilt_series.get_mrc_dims")
    # def test_get_tilt_series_from_late_job(self, mock_dims):
    #     """First job type with alignments, 1 tilt image has been excluded"""
    #     mock_dims.return_value = (2000, 2000, 8)
    #     self.setup_dirs(40)
    #     con = RelionCetsConverter("Polish/job040/")
    #     ts = get_tilt_series(con, "TS_01")
    #     assert len(ts) == 40
    #     assert ts[0].model_dump(mode="json") == {}
    #     assert ts[-1].model_dump(mode="json") == {}
