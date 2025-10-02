from cets_data_model.models.models import (
    ProjectionImage,
    CoordinateSystem,
    CTFMetadata,
    Axis,
    Affine,
    Translation,
)

RESULT = [
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[34.845611, 108.499417],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-56.9985,
        accumulated_dose=105.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39527.78125,
            defocus_v=39418.410156,
            defocus_angle=44.527622,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_038_-57_0.mrc",
        section="0",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[20.667906, 93.169012],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-53.9989,
        accumulated_dose=96.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38593.777344,
            defocus_v=38453.007812,
            defocus_angle=-77.46074,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_035_-54_0.mrc",
        section="1",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[28.684076, 116.360156],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-50.9988,
        accumulated_dose=93.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39716.988281,
            defocus_v=39676.960938,
            defocus_angle=-89.50993,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_034_-51_0.mrc",
        section="2",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[18.826563, 97.635815],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-47.9986,
        accumulated_dose=84.0,
        ctf_metadata=CTFMetadata(
            defocus_u=40543.109375,
            defocus_v=40288.300781,
            defocus_angle=34.091747,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_031_-48_0.mrc",
        section="3",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[29.472386, 116.098643],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-44.999,
        accumulated_dose=81.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39621.261719,
            defocus_v=39378.523438,
            defocus_angle=-51.37516,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_030_-45_0.mrc",
        section="4",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[19.003113, 94.890557],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-41.9989,
        accumulated_dose=72.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39632.832031,
            defocus_v=39503.171875,
            defocus_angle=-73.60011,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_027_-42_0.mrc",
        section="5",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[21.761036, 116.891845],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-38.9987,
        accumulated_dose=69.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39656.90625,
            defocus_v=39248.902344,
            defocus_angle=44.287949,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_026_-39_0.mrc",
        section="6",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[12.780535, 90.255066],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-35.9986,
        accumulated_dose=60.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39759.144531,
            defocus_v=39368.929688,
            defocus_angle=18.869625,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_023_-36_0.mrc",
        section="7",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[17.908609, 112.196687],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
        ],
        nominal_tilt_angle=-32.999,
        accumulated_dose=57.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39546.019531,
            defocus_v=39414.261719,
            defocus_angle=-48.23753,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_022_-33_0.mrc",
        section="8",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[6.62473, 83.144477],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
        ],
        nominal_tilt_angle=-29.9988,
        accumulated_dose=48.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39621.554688,
            defocus_v=39219.816406,
            defocus_angle=25.755552,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_019_-30_0.mrc",
        section="9",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[9.257857, 104.734463],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-26.9992,
        accumulated_dose=45.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39395.929688,
            defocus_v=38934.125,
            defocus_angle=70.461578,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_018_-27_0.mrc",
        section="10",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[1.454121, 74.985005],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-23.9986,
        accumulated_dose=36.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39957.90625,
            defocus_v=39131.46875,
            defocus_angle=44.914368,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_015_-24_0.mrc",
        section="11",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[8.57864, 100.746389],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
        ],
        nominal_tilt_angle=-20.9989,
        accumulated_dose=33.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39191.355469,
            defocus_v=38752.570312,
            defocus_angle=41.521111,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_014_-21_0.mrc",
        section="12",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[3.762442, 70.426216],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-17.9988,
        accumulated_dose=24.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39367.917969,
            defocus_v=38797.90625,
            defocus_angle=69.937973,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_011_-18_0.mrc",
        section="13",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[7.969166, 77.680473],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-14.9987,
        accumulated_dose=21.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39371.125,
            defocus_v=39312.433594,
            defocus_angle=43.634537,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_010_-15_0.mrc",
        section="14",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[3.958798, 71.251783],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
        ],
        nominal_tilt_angle=-11.9985,
        accumulated_dose=12.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39587.886719,
            defocus_v=39267.863281,
            defocus_angle=16.908651,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_007_-12_0.mrc",
        section="15",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[7.246304, 46.122795],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-8.9989,
        accumulated_dose=9.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39666.992188,
            defocus_v=38692.070312,
            defocus_angle=67.526459,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_006_-9_0.mrc",
        section="16",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[4.056802, 43.530523],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-5.99876,
        accumulated_dose=0.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38916.207031,
            defocus_v=38578.90625,
            defocus_angle=-42.83319,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_003_-6_0.mrc",
        section="17",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-0.664505, 14.789812],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=-2.99863,
        accumulated_dose=-3.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39039.273438,
            defocus_v=38788.375,
            defocus_angle=48.905102,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_002_-3_0.mrc",
        section="18",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[0.610515, -9.180914],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=0.001,
        accumulated_dose=-9.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38855.828125,
            defocus_v=38750.828125,
            defocus_angle=35.154533,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_000_0_0.mrc",
        section="19",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-3.254469, -41.716951],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=3.00113,
        accumulated_dose=-6.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39181.238281,
            defocus_v=39140.960938,
            defocus_angle=12.550397,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_001_3_0.mrc",
        section="20",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-7.638392, -65.149493],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=6.00126,
        accumulated_dose=3.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38871.554688,
            defocus_v=38659.703125,
            defocus_angle=-86.54452,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_004_6_0.mrc",
        section="21",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-8.105922, -58.018655],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=9.0014,
        accumulated_dose=6.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39463.386719,
            defocus_v=38568.289062,
            defocus_angle=40.258121,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_005_9_0.mrc",
        section="22",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-9.168774, -87.453127],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=12.0005,
        accumulated_dose=15.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38949.433594,
            defocus_v=38699.5625,
            defocus_angle=25.551586,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_008_12_0.mrc",
        section="23",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-11.018162, -74.036338],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=15.0007,
        accumulated_dose=18.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39014.972656,
            defocus_v=38768.765625,
            defocus_angle=-0.90581,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_009_15_0.mrc",
        section="24",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-15.055541, -105.101393],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=18.0008,
        accumulated_dose=27.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38690.386719,
            defocus_v=38564.035156,
            defocus_angle=5.383391,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_012_18_0.mrc",
        section="25",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-14.136312, -105.00574],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=21.0009,
        accumulated_dose=30.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39183.546875,
            defocus_v=38977.851562,
            defocus_angle=-75.17061,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_013_21_0.mrc",
        section="26",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-19.906444, -125.451695],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=24.0006,
        accumulated_dose=39.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39091.230469,
            defocus_v=38781.570312,
            defocus_angle=76.682976,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_016_24_0.mrc",
        section="27",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-15.166403, -130.853929],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=27.0007,
        accumulated_dose=42.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38935.335938,
            defocus_v=38806.46875,
            defocus_angle=-83.8278,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_017_27_0.mrc",
        section="28",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-24.585325, -142.198395],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=30.0008,
        accumulated_dose=51.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38910.875,
            defocus_v=38214.078125,
            defocus_angle=55.941147,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_020_30_0.mrc",
        section="29",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-20.100055, -128.847136],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=33.001,
        accumulated_dose=54.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38949.035156,
            defocus_v=38796.992188,
            defocus_angle=45.229416,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_021_33_0.mrc",
        section="30",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-22.668676, -156.078011],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=36.0006,
        accumulated_dose=63.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38909.515625,
            defocus_v=38473.996094,
            defocus_angle=34.372036,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_024_36_0.mrc",
        section="31",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-8.901784, -138.030123],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=39.0007,
        accumulated_dose=66.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39229.929688,
            defocus_v=38722.871094,
            defocus_angle=40.212944,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_025_39_0.mrc",
        section="32",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-25.537779, -165.243161],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=42.0009,
        accumulated_dose=75.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38625.375,
            defocus_v=38329.550781,
            defocus_angle=38.231094,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_028_42_0.mrc",
        section="33",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-10.783477, -146.425472],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=45.001,
        accumulated_dose=78.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38758.140625,
            defocus_v=38564.382812,
            defocus_angle=53.667973,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_029_45_0.mrc",
        section="34",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-28.227257, -169.437971],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=48.0006,
        accumulated_dose=87.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38438.015625,
            defocus_v=38173.0625,
            defocus_angle=63.245338,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_032_48_0.mrc",
        section="35",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-8.804052, -143.820056],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=51.0008,
        accumulated_dose=90.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38861.210938,
            defocus_v=38739.855469,
            defocus_angle=21.330759,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_033_51_0.mrc",
        section="36",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-29.571601, -162.395054],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=54.0009,
        accumulated_dose=99.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38656.089844,
            defocus_v=38493.3125,
            defocus_angle=-8.29779,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_036_54_0.mrc",
        section="37",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-11.98729, -137.537965],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
        ],
        nominal_tilt_angle=57.0,
        accumulated_dose=102.0,
        ctf_metadata=CTFMetadata(
            defocus_u=37450.847656,
            defocus_v=37448.03125,
            defocus_angle=-35.11659,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_037_57_0.mrc",
        section="38",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
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
            )
        ],
        coordinate_transformations=[
            Translation(
                name="Tilt image alignment translation",
                input=None,
                output=None,
                translation=[-27.89235, -156.675694],
            ),
            Affine(
                name="Tilt image alignment x tilt",
                input=None,
                output=None,
                affine=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            ),
            Affine(
                name="Tilt image alignment y tilt",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            ),
            Affine(
                name="Tilt image alignment x rotation",
                input=None,
                output=None,
                affine=[[0, 0, 0], [0, 0, 0], [0, 0, 1]],
            ),
        ],
        nominal_tilt_angle=60.0006,
        accumulated_dose=111.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38544.476562,
            defocus_v=38449.148438,
            defocus_angle=-10.13496,
            defocus_handedness=-1,
        ),
        path="MotionCorr/job002/frames/TS_01_040_60_0.mrc",
        section="39",
    ),
]
