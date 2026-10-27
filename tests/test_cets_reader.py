from cets_data_model.models.models import Dataset

from tests.testing_tools import CetsRelionTest, all_movie_stacks, all_projection_imgs
from cets_relion.cets_to_relion.cets_reader import CetsReader


class TestCetsReader(CetsRelionTest):
    def test_instantiate_cets_reader_just_movies(self):
        con = CetsReader(self.test_data / "results/TS_03_r_to_c_import.json")
        assert isinstance(con.data, Dataset)
        assert list(con.movie_stacks.keys()) == ["TS_03"]
        assert con.movie_stacks["TS_03"] == all_movie_stacks()
        assert con.tilt_angle_images == {}

    def test_instantiate_cets_reader_mocorr(self):
        "Has tilt angle images but no CTF info"
        con = CetsReader(self.test_data / "results/TS_03_r_to_c_mocorr.json")
        assert isinstance(con.data, Dataset)
        assert list(con.movie_stacks.keys()) == ["TS_03"]
        assert con.movie_stacks["TS_03"] == all_movie_stacks()
        assert con.tilt_angle_images == all_projection_imgs()
