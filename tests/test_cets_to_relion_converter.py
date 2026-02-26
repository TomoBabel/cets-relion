# from cets_relion.cets_to_relion.cets_to_relion_converter import CetsToRelionConverter
# from cets_relion.cets_to_relion.cets_reader import CetsReader
# from tests.testing_tools import CetsRelionTest
# from tests.test_data.results.TS_03_all_movie_stacks import ALL_MOVIE_STACKS
# from tests.test_data.results.TS_03_all_projection_imgs import ALL_PROJECTION_IMGS
# from tests.test_data.results.TS_03_ts_file import TS_DATA_IMPORT, TS_DATA_CTF
# from unittest import skip
#
#
# class CetsToRelionConverterTest(CetsRelionTest):
#     def test_instantiate_converter_import_data_only(self):
#         converter = CetsToRelionConverter(
#             self.test_data / "results/TS_03_r_to_c_import.json"
#         )
#         assert isinstance(converter.data, CetsReader)
#         assert converter.data.movie_stacks["TS_03"] == ALL_MOVIE_STACKS
#         assert converter.data.tilt_angle_images == {}
#
#     def test_instantiate_converter_mocorr_data(self):
#         converter = CetsToRelionConverter(
#             self.test_data / "results/TS_03_r_to_c_mocorr.json"
#         )
#         assert isinstance(converter.data, CetsReader)
#         assert converter.data.movie_stacks["TS_03"] == ALL_MOVIE_STACKS
#         assert converter.data.tilt_angle_images == ALL_PROJECTION_IMGS
#
#     def test_get_main_file_data(self):
#         converter = CetsToRelionConverter(
#             self.test_data / "results/TS_03_r_to_c_import.json"
#         )
#         assert converter.ts_master_file_basic_data("TS_03") == [
#             "TS_03",
#             "tilt_series/TS_03.star",
#             "XXX_Voltage",
#             "XXX_SphericalAberration",
#             "XXX_AmplitudeContrast",
#             "XXX_MicrographOriginalPixelSize",
#             "XXX_TomoHand",
#             "Optics1",
#             "XXX_TomoTiltSeriesPixelSize",
#             "XXX_EtomoDirectiveFile",
#         ]
#
#     def test_get_dose_rate(self):
#         converter = CetsToRelionConverter(
#             self.test_data / "results/TS_03_r_to_c_import.json"
#         )
#         frames = converter.data.movie_stacks["TS_03"][0].images
#         assert converter.get_dose_rate(frames) == 0.375
#
#     def test_get_tilt_series_file_data_from_frames_import_from_import_job(self):
#         """Just the basic imfo"""
#         converter = CetsToRelionConverter(
#             self.test_data / "results/TS_03_r_to_c_import.json"
#         )
#         assert converter.ts_file_data_from_frames() == TS_DATA_IMPORT
#
#     def test_get_tilt_series_file_data_from_frames_import_from_ctf_job(self):
#         """Includes ctf info"""
#         converter = CetsToRelionConverter(
#             self.test_data / "results/TS_03_r_to_c_ctf.json"
#         )
#         assert converter.ts_file_data_from_frames() == TS_DATA_CTF
#
#     @skip("This isn't added to the converter code yet")
#     def test_get_tilt_series_file_data_from_frames_import_from_align_job(self):
#         """Includes frame alignment info"""
#         converter = CetsToRelionConverter(
#             self.test_data / "results/TS_03_r_to_c_align.json"
#         )
#         assert converter.ts_file_data_from_frames() == TS_DATA_CTF
#
#     def test_write_main_relion_starfile_import_data(self):
#         converter = CetsToRelionConverter(
#             self.test_data / "results/TS_03_r_to_c_import.json"
#         )
#         converter.write_main_relion_ts_starfile()
#
#     def test_write_ts_starfile_import_data_only(self):
#         converter = CetsToRelionConverter(
#             self.test_data / "results/TS_03_r_to_c_import.json"
#         )
#         converter.write_ts_starfiles()
#         with open(
#             self.test_data / "starfiles/TS_03_tilt_series_from_import.star"
#         ) as exp:
#             expected = exp.read()
#         with open("tilt_series/TS_03.star") as act:
#             actual = act.read()
#         assert actual == expected
#
#     def test_write_ts_starfile_with_ctf_data(self):
#         converter = CetsToRelionConverter(
#             self.test_data / "results/TS_03_r_to_c_ctf.json"
#         )
#         converter.write_ts_starfiles()
#         with open(self.test_data / "starfiles/TS_03_tilt_series_from_ctf.star") as exp:
#             expected = exp.read()
#         with open("tilt_series/TS_03.star") as act:
#             actual = act.read()
#         assert actual == expected
