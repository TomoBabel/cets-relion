from cets_relion.cets_to_relion_converter import CetsToRelionConverter
from cets_relion.cets_reader import CetsReader
from tests.testing_tools import CetsRelionTest
from tests.test_data.results.TS_03_all_movie_stacks import ALL_MOVIE_STACKS
from tests.test_data.results.TS_03_all_projection_imgs import ALL_PROJECTION_IMGS
from tests.test_data.results.TS_03_ts_file import TS_DATA


class CetsToRelionConverterTest(CetsRelionTest):
    def test_instantiate_converter_import_data_only(self):
        converter = CetsToRelionConverter(
            self.test_data / "results/TS_03_r_to_c_import.json"
        )
        assert isinstance(converter.data, CetsReader)
        assert converter.data.movie_stacks["TS_03"] == ALL_MOVIE_STACKS
        assert converter.data.tilt_angle_images == {}

    def test_instantiate_converter_mocorr_data(self):
        converter = CetsToRelionConverter(
            self.test_data / "results/TS_03_r_to_c_mocorr.json"
        )
        assert isinstance(converter.data, CetsReader)
        assert converter.data.movie_stacks["TS_03"] == ALL_MOVIE_STACKS
        assert converter.data.tilt_angle_images == ALL_PROJECTION_IMGS

    def test_get_main_file_data(self):
        converter = CetsToRelionConverter(
            self.test_data / "results/TS_03_r_to_c_import.json"
        )
        assert converter.ts_master_file_basic_data("TS_03") == [
            "TS_03",
            "tilt_series/TS_03.star",
            "VOLTAGE-1",
            "SPHEREABB-1",
            "AMPCON-1",
            "APIX-1",
            "TOMOHAND-1",
            "Optics1",
        ]

    def test_get_dose_rate(self):
        converter = CetsToRelionConverter(
            self.test_data / "results/TS_03_r_to_c_import.json"
        )
        frames = converter.data.movie_stacks["TS_03"][0].images
        assert converter.get_dose_rate(frames) == 0.375

    def test_get_tilt_series_file_data_from_frames(self):
        converter = CetsToRelionConverter(
            self.test_data / "results/TS_03_r_to_c_import.json"
        )
        assert converter.ts_file_data_from_frames() == TS_DATA

    def test_write_main_relion_starfile_import_data(self):
        converter = CetsToRelionConverter(
            self.test_data / "results/TS_03_r_to_c_import.json"
        )
        converter.write_main_relion_ts_starfile()

    def test_write_ts_starfile_import_data_only(self):
        converter = CetsToRelionConverter(
            self.test_data / "results/TS_03_r_to_c_import.json"
        )
        converter.write_ts_starfiles()
        with open(self.test_data / "starfiles/TS_03_tilt_series.star") as exp:
            expected = exp.read()
        with open("tilt_series/TS_03.star") as act:
            actual = act.read()
        assert actual == expected
