from unittest.mock import patch, MagicMock

from pytest import fixture

from cets_relion.tilt_series import RelionTiltSeriesStarfile
from cets_relion.movies import RelionMoviesStarFile
from cets_relion.relion_reader import RelionPipeline
from cets_data_model.models.models import (
    CTFMetadata,
    MovieFrame,
    MovieStackSeries,
    MovieStack,
    CoordinateSystem,
    Axis,
    Scale,
)
from tests.testing_tools import CetsRelionTest


@fixture(autouse=True)
def mock_get_image_size():
    with patch("cets_relion.movies.get_image_dims") as mock:
        mock.return_value = (2000, 2000, 8)
        yield mock


@fixture(autouse=True)
def mock_get_ctf_data():
    with patch("cets_relion.movies.RelionTiltSeriesStarfile") as MockClass:
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
        assert msf.name == "Import/job001/tilt_series.star"
        assert msf.mocorr_files == []
        assert msf.ctf_files == []

    def test_get_movies_starfile(self):
        self.setup_dirs(3)
        msf = RelionMoviesStarFile("Import/job001/tilt_series.star")
        assert msf.get_tilt_movies_starfile("TS_01") == (
            "Import/job001/tilt_series/TS_01.star"
        )

    def test_make_movie_cets_for_tilt_series_with_ctf(self):
        self.setup_dirs(3)
        msf = RelionMoviesStarFile(
            "Import/job001/tilt_series.star",
            ctf_files=[RelionTiltSeriesStarfile("CtfFind/job003/tilt_series_ctf.star")],
        )
        result = msf.make_movie_cets_for_tilt_series("TS_01")
        assert isinstance(result, MovieStackSeries)
        assert len(result.stacks) == 41
        assert result.stacks[0].path == "frames/TS_01_000_0.0.mrc"
        assert isinstance(result.stacks[0], MovieStack)
        assert len(result.stacks[0].images) == 8
        assert result.stacks[0].images[0] == MovieFrame(
            width=2000,
            height=2000,
            coordinate_systems=[
                CoordinateSystem(
                    name="logical coordinates",
                    axes=[
                        Axis(
                            name="logical coordinates x axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                        Axis(
                            name="logical coordinates y axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                        Axis(
                            name="logical coordinates z axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                    ],
                ),
                CoordinateSystem(
                    name="physical coordinates",
                    axes=[
                        Axis(
                            name="physical coordinates x axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates y axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates z axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                    ],
                ),
            ],
            coordinate_transformations=[
                Scale(
                    type="scale",
                    name="pixel size",
                    input="logical coordinates",
                    output="physical_coordinates",
                    scale=[0.675, 0.675],
                )
            ],
            nominal_tilt_angle=0.001,
            accumulated_dose=0.375,
            ctf_metadata=CTFMetadata(
                defocus_u=38855.828125, defocus_v=38750.828125, defocus_angle=35.154533
            ),
            path="00001@frames/TS_01_000_0.0.mrc",
            section="0",
        )
        assert result.stacks[0].images[-1] == MovieFrame(
            width=2000,
            height=2000,
            coordinate_systems=[
                CoordinateSystem(
                    name="logical coordinates",
                    axes=[
                        Axis(
                            name="logical coordinates x axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                        Axis(
                            name="logical coordinates y axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                        Axis(
                            name="logical coordinates z axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                    ],
                ),
                CoordinateSystem(
                    name="physical coordinates",
                    axes=[
                        Axis(
                            name="physical coordinates x axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates y axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates z axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                    ],
                ),
            ],
            coordinate_transformations=[
                Scale(
                    type="scale",
                    name="pixel size",
                    input="logical coordinates",
                    output="physical_coordinates",
                    scale=[0.675, 0.675],
                )
            ],
            nominal_tilt_angle=0.001,
            accumulated_dose=3.0,
            ctf_metadata=CTFMetadata(
                defocus_u=38855.828125, defocus_v=38750.828125, defocus_angle=35.154533
            ),
            path="00008@frames/TS_01_000_0.0.mrc",
            section="7",
        )
        assert result.stacks[-1].images[-1] == MovieFrame(
            width=2000,
            height=2000,
            coordinate_systems=[
                CoordinateSystem(
                    name="logical coordinates",
                    axes=[
                        Axis(
                            name="logical coordinates x axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                        Axis(
                            name="logical coordinates y axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                        Axis(
                            name="logical coordinates z axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                    ],
                ),
                CoordinateSystem(
                    name="physical coordinates",
                    axes=[
                        Axis(
                            name="physical coordinates x axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates y axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates z axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                    ],
                ),
            ],
            coordinate_transformations=[
                Scale(
                    type="scale",
                    name="pixel size",
                    input="logical coordinates",
                    output="physical_coordinates",
                    scale=[0.675, 0.675],
                )
            ],
            nominal_tilt_angle=60.0006,
            accumulated_dose=123.0,
            ctf_metadata=CTFMetadata(
                defocus_u=38544.476562, defocus_v=38449.148438, defocus_angle=-10.13496
            ),
            path="00008@frames/TS_01_040_60.0.mrc",
            section="7",
        )

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
            width=2000,
            height=2000,
            coordinate_systems=[
                CoordinateSystem(
                    name="logical coordinates",
                    axes=[
                        Axis(
                            name="logical coordinates x axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                        Axis(
                            name="logical coordinates y axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                        Axis(
                            name="logical coordinates z axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                    ],
                ),
                CoordinateSystem(
                    name="physical coordinates",
                    axes=[
                        Axis(
                            name="physical coordinates x axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates y axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates z axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                    ],
                ),
            ],
            coordinate_transformations=[
                Scale(
                    type="scale",
                    name="pixel size",
                    input="logical coordinates",
                    output="physical_coordinates",
                    scale=[0.675, 0.675],
                )
            ],
            nominal_tilt_angle=0.001,
            accumulated_dose=0.375,
            ctf_metadata=None,
            path="00001@frames/TS_01_000_0.0.mrc",
            section="0",
        )
        assert result.stacks[0].images[-1] == MovieFrame(
            width=2000,
            height=2000,
            coordinate_systems=[
                CoordinateSystem(
                    name="logical coordinates",
                    axes=[
                        Axis(
                            name="logical coordinates x axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                        Axis(
                            name="logical coordinates y axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                        Axis(
                            name="logical coordinates z axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                    ],
                ),
                CoordinateSystem(
                    name="physical coordinates",
                    axes=[
                        Axis(
                            name="physical coordinates x axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates y axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates z axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                    ],
                ),
            ],
            coordinate_transformations=[
                Scale(
                    type="scale",
                    name="pixel size",
                    input="logical coordinates",
                    output="physical_coordinates",
                    scale=[0.675, 0.675],
                )
            ],
            nominal_tilt_angle=0.001,
            accumulated_dose=3.0,
            ctf_metadata=None,
            path="00008@frames/TS_01_000_0.0.mrc",
            section="7",
        )
        assert result.stacks[-1].images[-1] == MovieFrame(
            width=2000,
            height=2000,
            coordinate_systems=[
                CoordinateSystem(
                    name="logical coordinates",
                    axes=[
                        Axis(
                            name="logical coordinates x axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                        Axis(
                            name="logical coordinates y axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                        Axis(
                            name="logical coordinates z axis",
                            axis_unit="pixel/voxel",
                            axis_type=None,
                        ),
                    ],
                ),
                CoordinateSystem(
                    name="physical coordinates",
                    axes=[
                        Axis(
                            name="physical coordinates x axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates y axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates z axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                    ],
                ),
            ],
            coordinate_transformations=[
                Scale(
                    type="scale",
                    name="pixel size",
                    input="logical coordinates",
                    output="physical_coordinates",
                    scale=[0.675, 0.675],
                )
            ],
            nominal_tilt_angle=60.0006,
            accumulated_dose=123.0,
            ctf_metadata=None,
            path="00008@frames/TS_01_040_60.0.mrc",
            section="7",
        )

    def test_get_all_tomo_names(self):
        self.setup_dirs(1)
        mf = RelionMoviesStarFile("Import/job001/tilt_series.star")
        assert mf.get_all_tomo_names() == ["TS_01", "TS_03", "TS_43", "TS_45", "TS_54"]

    def test_get_all_tomo_pixel_sizes(self):
        self.setup_dirs(1)
        mf = RelionMoviesStarFile("Import/job001/tilt_series.star")
        assert mf.get_all_pixel_sizes() == {
            "TS_01": "0.675000",
            "TS_03": "0.675000",
            "TS_43": "0.675000",
            "TS_45": "0.675000",
            "TS_54": "0.675000",
        }
