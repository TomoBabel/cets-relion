# from cets_data_model.models.models import Dataset
#
# from tests.testing_tools import CetsRelionTest
# from cets_relion.cets_to_relion.cets_reader import CetsReader
# from tests.test_data.results.TS_03_all_movie_stacks import ALL_MOVIE_STACKS
# from tests.test_data.results.TS_03_all_projection_imgs import ALL_PROJECTION_IMGS
#
#
# class TestCetsReader(CetsRelionTest):
#     def test_instantiate_cets_reader_just_movies(self):
#         con = CetsReader(self.test_data / "results/TS_03_r_to_c_import.json")
#         assert isinstance(con.data, Dataset)
#         assert list(con.movie_stacks.keys()) == ["TS_03"]
#         assert con.movie_stacks["TS_03"] == ALL_MOVIE_STACKS
#         assert con.tilt_angle_images == {}
#
#     def test_instantiate_cets_reader_mocorr(self):
#         "Has tilt angle images but no CTF info"
#         con = CetsReader(self.test_data / "results/TS_03_r_to_c_mocorr.json")
#         assert isinstance(con.data, Dataset)
#         assert list(con.movie_stacks.keys()) == ["TS_03"]
#         assert con.movie_stacks["TS_03"] == ALL_MOVIE_STACKS
#         assert con.tilt_angle_images == ALL_PROJECTION_IMGS
