from pytest import fixture
from unittest.mock import patch, MagicMock
from src.cets_relion.movies import RelionMoviesStarFile
from tests.testing_tools import CetsRelionTest
from src.models.models import (
    CTFMetadata,
    MovieFrame,
    MovieStackSeries,
    MovieStack,
    MovieStackCollection,
    GainFile,
)
from src.cets_relion.relion_reader import RelionPipeline


@fixture(autouse=True)
def mock_get_image_size():
    with patch("src.cets_relion.movies.get_image_dims") as mock:
        mock.return_value = (2000, 2000, 8)
        yield mock


@fixture(autouse=True)
def mock_get_ctf_data():
    with patch("src.cets_relion.movies.RelionCtfStarFile") as MockClass:
        mock_instance = MagicMock()
        mock_instance.get_tilt_image_ctf.return_value = CTFMetadata(
            defocus_u=1111, defocus_v=2222, defocus_angle=33
        )
        MockClass.return_value = mock_instance
        yield mock_instance


class RelionCetsMoviesTests(CetsRelionTest):
    def test_instantiate_RelionMoviesStarFile(self):
        self.setup_dirs(3)
        msf = RelionMoviesStarFile("Import/job001/tilt_series.star")
        assert isinstance(msf.pipeline, RelionPipeline)
        assert msf.movies_file == "Import/job001/tilt_series.star"
        assert msf.mocorr_files == ["MotionCorr/job002/corrected_tilt_series.star"]
        assert msf.ctf_files == ["CtfFind/job003/tilt_series_ctf.star"]

    def test_get_movies_starfile(self):
        self.setup_dirs(3)
        msf = RelionMoviesStarFile("Import/job001/tilt_series.star")
        assert msf.get_tilt_movies_starfile("TS_01") == (
            "Import/job001/tilt_series/TS_01.star"
        )

    def test_make_movie_cets_for_tilt_series(self):
        self.setup_dirs(3)
        msf = RelionMoviesStarFile("Import/job001/tilt_series.star")
        result = msf.make_movie_cets_for_tilt_series("TS_01")
        assert isinstance(result, MovieStackSeries)
        assert len(result.stacks) == 41
        assert result.stacks[0].path == "frames/TS_01_000_0.0.mrc"
        assert isinstance(result.stacks[0], MovieStack)
        assert len(result.stacks[0].images) == 8
        assert result.stacks[0].images[0] == MovieFrame(
            accumulated_dose=0.375,
            coordinate_systems=None,
            coordinate_transformations=None,
            ctf_metadata=CTFMetadata(
                defocus_u=1111.0,
                defocus_v=2222.0,
                defocus_angle=33.0,
            ),
            height=2000,
            nominal_tilt_angle=0.001,
            path="00001@frames/TS_01_000_0.0.mrc",
            section="0",
            width=2000,
        )
        assert result.stacks[0].images[-1] == MovieFrame(
            accumulated_dose=3.0,
            coordinate_systems=None,
            coordinate_transformations=None,
            ctf_metadata=CTFMetadata(
                defocus_u=1111.0,
                defocus_v=2222.0,
                defocus_angle=33.0,
            ),
            height=2000,
            nominal_tilt_angle=0.001,
            path="00008@frames/TS_01_000_0.0.mrc",
            section="7",
            width=2000,
        )
        assert result.stacks[-1].images[-1] == MovieFrame(
            accumulated_dose=123.0,
            coordinate_systems=None,
            coordinate_transformations=None,
            ctf_metadata=CTFMetadata(
                defocus_u=1111.0,
                defocus_v=2222.0,
                defocus_angle=33.0,
            ),
            height=2000,
            nominal_tilt_angle=60.0006,
            path="00008@frames/TS_01_040_60.0.mrc",
            section="7",
            width=2000,
        )

    def test_get_all_movies_stack_series(self):
        self.setup_dirs(3)
        msf = RelionMoviesStarFile("Import/job001/tilt_series.star")
        result = msf.get_all_movies_stack_series()
        assert all([isinstance(x, MovieStackCollection) for x in result])
        assert len(result) == 5
        assert result[0].defect_file is None
        assert isinstance(result[0].gain_file, GainFile)
        assert result[0].gain_file.path == "gain_reference.mrc"

    def test_make_movie_cets_for_tilt_series_no_ctf_available(self):
        self.setup_dirs(1, pipeline="single_import_pipeline.star")
        msf = RelionMoviesStarFile("Import/job001/tilt_series.star")
        result = msf.make_movie_cets_for_tilt_series("TS_01")
        assert isinstance(result, MovieStackSeries)
        assert len(result.stacks) == 41
        assert result.stacks[0].path == "frames/TS_01_000_0.0.mrc"
        assert isinstance(result.stacks[0], MovieStack)
        assert len(result.stacks[0].images) == 8
        assert result.stacks[0].images[0] == MovieFrame(
            accumulated_dose=0.375,
            coordinate_systems=None,
            coordinate_transformations=None,
            ctf_metadata=None,
            height=2000,
            nominal_tilt_angle=0.001,
            path="00001@frames/TS_01_000_0.0.mrc",
            section="0",
            width=2000,
        )
        assert result.stacks[0].images[-1] == MovieFrame(
            accumulated_dose=3.0,
            coordinate_systems=None,
            coordinate_transformations=None,
            ctf_metadata=None,
            height=2000,
            nominal_tilt_angle=0.001,
            path="00008@frames/TS_01_000_0.0.mrc",
            section="7",
            width=2000,
        )
        assert result.stacks[-1].images[-1] == MovieFrame(
            accumulated_dose=123.0,
            coordinate_systems=None,
            coordinate_transformations=None,
            ctf_metadata=None,
            height=2000,
            nominal_tilt_angle=60.0006,
            path="00008@frames/TS_01_040_60.0.mrc",
            section="7",
            width=2000,
        )
