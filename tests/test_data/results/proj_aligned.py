from cets_data_model.models.models import (
    ProjectionImage,
    CoordinateSystem,
    CTFMetadata,
    Axis,
    Affine,
    Translation,
    Scale,
)

RESULT = [
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[34.845611, 108.499417],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08658269165227545, -0.9962446674920009, 0.0],
                    [0.9962446674920009, 0.08658269165227545, 0.0],
                    [0.0, 0.0, 1.0000000000000002],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.5446390350150272, -0.0, -0.838670567945424],
                    [0.0, 1.0, -0.0],
                    [0.838670567945424, 0.0, 0.5446390350150272],
                ],
            ),
        ],
        nominal_tilt_angle=-56.9985,
        accumulated_dose=105.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39527.78125, defocus_v=39418.410156, defocus_angle=44.527622
        ),
        path="MotionCorr/job002/frames/TS_01_038_-57_0.mrc",
        section="0",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[20.667906, 93.169012],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08620810125116396, -0.9962771518401238, 0.0],
                    [0.9962771518401238, 0.08620810125116396, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.5877852522924732, -0.0, -0.8090169943749475],
                    [0.0, 1.0000000000000002, -0.0],
                    [0.8090169943749475, 0.0, 0.5877852522924732],
                ],
            ),
        ],
        nominal_tilt_angle=-53.9989,
        accumulated_dose=96.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38593.777344, defocus_v=38453.007812, defocus_angle=-77.46074
        ),
        path="MotionCorr/job002/frames/TS_01_035_-54_0.mrc",
        section="1",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[28.684076, 116.360156],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08587709250518188, -0.9963057387081822, 0.0],
                    [0.9963057387081822, 0.08587709250518188, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.6293203910498375, -0.0, -0.7771459614569709],
                    [0.0, 1.0, -0.0],
                    [0.7771459614569709, 0.0, 0.6293203910498375],
                ],
            ),
        ],
        nominal_tilt_angle=-50.9988,
        accumulated_dose=93.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39716.988281, defocus_v=39676.960938, defocus_angle=-89.50993
        ),
        path="MotionCorr/job002/frames/TS_01_034_-51_0.mrc",
        section="2",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[18.826563, 97.635815],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.0855808006848619, -0.9963312333527129, 0.0],
                    [0.9963312333527129, 0.0855808006848619, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.6691306063588581, -0.0, -0.7431448254773942],
                    [0.0, 0.9999999999999999, -0.0],
                    [0.7431448254773942, 0.0, 0.6691306063588581],
                ],
            ),
        ],
        nominal_tilt_angle=-47.9986,
        accumulated_dose=84.0,
        ctf_metadata=CTFMetadata(
            defocus_u=40543.109375, defocus_v=40288.300781, defocus_angle=34.091747
        ),
        path="MotionCorr/job002/frames/TS_01_031_-48_0.mrc",
        section="3",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[29.472386, 116.098643],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.085312794309717, -0.9963542176992416, 0.0],
                    [0.9963542176992416, 0.085312794309717, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.7071067811865475, -0.0, -0.7071067811865476],
                    [0.0, 1.0, -0.0],
                    [0.7071067811865476, 0.0, 0.7071067811865475],
                ],
            ),
        ],
        nominal_tilt_angle=-44.999,
        accumulated_dose=81.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39621.261719, defocus_v=39378.523438, defocus_angle=-51.37516
        ),
        path="MotionCorr/job002/frames/TS_01_030_-45_0.mrc",
        section="4",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[19.003113, 94.890557],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08506789313057106, -0.9963751570359056, 0.0],
                    [0.9963751570359056, 0.08506789313057106, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.7431448254773942, -0.0, -0.6691306063588582],
                    [0.0, 1.0, -0.0],
                    [0.6691306063588582, 0.0, 0.7431448254773942],
                ],
            ),
        ],
        nominal_tilt_angle=-41.9989,
        accumulated_dose=72.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39632.832031, defocus_v=39503.171875, defocus_angle=-73.60011
        ),
        path="MotionCorr/job002/frames/TS_01_027_-42_0.mrc",
        section="5",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[21.761036, 116.891845],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08484199449450264, -0.9963944178738633, 0.0],
                    [0.9963944178738633, 0.08484199449450264, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.7771459614569709, -0.0, -0.6293203910498374],
                    [0.0, 1.0, -0.0],
                    [0.6293203910498374, 0.0, 0.7771459614569709],
                ],
            ),
        ],
        nominal_tilt_angle=-38.9987,
        accumulated_dose=69.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39656.90625, defocus_v=39248.902344, defocus_angle=44.287949
        ),
        path="MotionCorr/job002/frames/TS_01_026_-39_0.mrc",
        section="6",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[12.780535, 90.255066],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08463170833432643, -0.996412301180798, 0.0],
                    [0.996412301180798, 0.08463170833432643, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.8090169943749473, -0.0, -0.587785252292473],
                    [0.0, 0.9999999999999999, -0.0],
                    [0.587785252292473, 0.0, 0.8090169943749473],
                ],
            ),
        ],
        nominal_tilt_angle=-35.9986,
        accumulated_dose=60.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39759.144531, defocus_v=39368.929688, defocus_angle=18.869625
        ),
        path="MotionCorr/job002/frames/TS_01_023_-36_0.mrc",
        section="7",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[17.908609, 112.196687],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08443489641162427, -0.9964289981067181, 0.0],
                    [0.9964289981067181, 0.08443489641162427, 0.0],
                    [0.0, 0.0, 0.9999999999999999],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.838670567945424, -0.0, -0.5446390350150271],
                    [0.0, 1.0, -0.0],
                    [0.5446390350150271, 0.0, 0.838670567945424],
                ],
            ),
        ],
        nominal_tilt_angle=-32.999,
        accumulated_dose=57.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39546.019531, defocus_v=39414.261719, defocus_angle=-48.23753
        ),
        path="MotionCorr/job002/frames/TS_01_022_-33_0.mrc",
        section="8",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[6.62473, 83.144477],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08424889855201445, -0.9964447416152951, 0.0],
                    [0.9964447416152951, 0.08424889855201445, 0.0],
                    [0.0, 0.0, 0.9999999999999998],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.8660254037844387, -0.0, -0.49999999999999994],
                    [0.0, 1.0, -0.0],
                    [0.49999999999999994, 0.0, 0.8660254037844387],
                ],
            ),
        ],
        nominal_tilt_angle=-29.9988,
        accumulated_dose=48.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39621.554688, defocus_v=39219.816406, defocus_angle=25.755552
        ),
        path="MotionCorr/job002/frames/TS_01_019_-30_0.mrc",
        section="9",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[9.257857, 104.734463],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08407199351613714, -0.9964596830309909, 0.0],
                    [0.9964596830309909, 0.08407199351613714, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.8910065241883678, -0.0, -0.45399049973954675],
                    [0.0, 1.0, -0.0],
                    [0.45399049973954675, 0.0, 0.8910065241883678],
                ],
            ),
        ],
        nominal_tilt_angle=-26.9992,
        accumulated_dose=45.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39395.929688, defocus_v=38934.125, defocus_angle=70.461578
        ),
        path="MotionCorr/job002/frames/TS_01_018_-27_0.mrc",
        section="10",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[1.454121, 74.985005],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08390270341997574, -0.9964739516710006, 0.0],
                    [0.9964739516710006, 0.08390270341997574, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9135454576426011, -0.0, -0.40673664307580026],
                    [0.0, 1.0000000000000002, -0.0],
                    [0.40673664307580026, 0.0, 0.9135454576426011],
                ],
            ),
        ],
        nominal_tilt_angle=-23.9986,
        accumulated_dose=36.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39957.90625, defocus_v=39131.46875, defocus_angle=44.914368
        ),
        path="MotionCorr/job002/frames/TS_01_015_-24_0.mrc",
        section="11",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[8.57864, 100.746389],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.0837396024525009, -0.9964876712639735, 0.0],
                    [0.9964876712639735, 0.0837396024525009, 0.0],
                    [0.0, 0.0, 0.9999999999999999],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9335804264972019, -0.0, -0.3583679495453003],
                    [0.0, 1.0, -0.0],
                    [0.3583679495453003, 0.0, 0.9335804264972019],
                ],
            ),
        ],
        nominal_tilt_angle=-20.9989,
        accumulated_dose=33.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39191.355469, defocus_v=38752.570312, defocus_angle=41.521111
        ),
        path="MotionCorr/job002/frames/TS_01_014_-21_0.mrc",
        section="12",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[3.762442, 70.426216],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08358150820275739, -0.9965009440469952, 0.0],
                    [0.9965009440469952, 0.08358150820275739, 0.0],
                    [0.0, 0.0, 1.0000000000000002],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9510565162951536, -0.0, -0.30901699437494745],
                    [0.0, 1.0, -0.0],
                    [0.30901699437494745, 0.0, 0.9510565162951536],
                ],
            ),
        ],
        nominal_tilt_angle=-17.9988,
        accumulated_dose=24.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39367.917969, defocus_v=38797.90625, defocus_angle=69.937973
        ),
        path="MotionCorr/job002/frames/TS_01_011_-18_0.mrc",
        section="13",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[7.969166, 77.680473],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08342749907518598, -0.9965138495766428, 0.0],
                    [0.9965138495766428, 0.08342749907518598, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9659258262890682, -0.0, -0.25881904510252074],
                    [0.0, 1.0, -0.0],
                    [0.25881904510252074, 0.0, 0.9659258262890682],
                ],
            ),
        ],
        nominal_tilt_angle=-14.9987,
        accumulated_dose=21.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39371.125, defocus_v=39312.433594, defocus_angle=43.634537
        ),
        path="MotionCorr/job002/frames/TS_01_010_-15_0.mrc",
        section="14",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[3.958798, 71.251783],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08327649688688898, -0.9965264798620496, 0.0],
                    [0.9965264798620496, 0.08327649688688898, 0.0],
                    [0.0, 0.0, 0.9999999999999999],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9781476007338056, -0.0, -0.20791169081775931],
                    [0.0, 0.9999999999999999, -0.0],
                    [0.20791169081775931, 0.0, 0.9781476007338056],
                ],
            ),
        ],
        nominal_tilt_angle=-11.9985,
        accumulated_dose=12.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39587.886719, defocus_v=39267.863281, defocus_angle=16.908651
        ),
        path="MotionCorr/job002/frames/TS_01_007_-12_0.mrc",
        section="15",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[7.246304, 46.122795],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08312759732575159, -0.9965389117153669, 0.0],
                    [0.9965389117153669, 0.08312759732575159, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9876883405951378, -0.0, -0.15643446504023087],
                    [0.0, 1.0, -0.0],
                    [0.15643446504023087, 0.0, 0.9876883405951378],
                ],
            ),
        ],
        nominal_tilt_angle=-8.9989,
        accumulated_dose=9.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39666.992188, defocus_v=38692.070312, defocus_angle=67.526459
        ),
        path="MotionCorr/job002/frames/TS_01_006_-9_0.mrc",
        section="16",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[4.056802, 43.530523],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08298000039129666, -0.996551212700612, 0.0],
                    [0.996551212700612, 0.08298000039129666, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9945218953682732, -0.0, -0.10452846326765347],
                    [0.0, 0.9999999999999999, -0.0],
                    [0.10452846326765347, 0.0, 0.9945218953682732],
                ],
            ),
        ],
        nominal_tilt_angle=-5.99876,
        accumulated_dose=0.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38916.207031, defocus_v=38578.90625, defocus_angle=-42.83319
        ),
        path="MotionCorr/job002/frames/TS_01_003_-6_0.mrc",
        section="17",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-0.664505, 14.789812],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08283259296303197, -0.9965634759226433, 0.0],
                    [0.9965634759226433, 0.08283259296303197, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9986295347545738, -0.0, -0.052335956242943835],
                    [0.0, 0.9999999999999999, -0.0],
                    [0.052335956242943835, 0.0, 0.9986295347545738],
                ],
            ),
        ],
        nominal_tilt_angle=-2.99863,
        accumulated_dose=-3.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39039.273438, defocus_v=38788.375, defocus_angle=48.905102
        ),
        path="MotionCorr/job002/frames/TS_01_002_-3_0.mrc",
        section="18",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[0.610515, -9.180914],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08268509675480701, -0.9965757245561664, 0.0],
                    [0.9965757245561664, 0.08268509675480701, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
        ],
        nominal_tilt_angle=0.001,
        accumulated_dose=-9.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38855.828125, defocus_v=38750.828125, defocus_angle=35.154533
        ),
        path="MotionCorr/job002/frames/TS_01_000_0_0.mrc",
        section="19",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-3.254469, -41.716951],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08253639856716083, -0.9965880507569628, 0.0],
                    [0.9965880507569628, 0.08253639856716083, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9986295347545738, 0.0, 0.052335956242943835],
                    [0.0, 0.9999999999999999, 0.0],
                    [-0.052335956242943835, 0.0, 0.9986295347545738],
                ],
            ),
        ],
        nominal_tilt_angle=3.00113,
        accumulated_dose=-6.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39181.238281, defocus_v=39140.960938, defocus_angle=12.550397
        ),
        path="MotionCorr/job002/frames/TS_01_001_3_0.mrc",
        section="20",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-7.638392, -65.149493],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08238559387295591, -0.9966005287587401, 0.0],
                    [0.9966005287587401, 0.08238559387295591, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9945218953682732, 0.0, 0.10452846326765347],
                    [0.0, 0.9999999999999999, 0.0],
                    [-0.10452846326765347, 0.0, 0.9945218953682732],
                ],
            ),
        ],
        nominal_tilt_angle=6.00126,
        accumulated_dose=3.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38871.554688, defocus_v=38659.703125, defocus_angle=-86.54452
        ),
        path="MotionCorr/job002/frames/TS_01_004_6_0.mrc",
        section="21",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-8.105922, -58.018655],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.0822317085224189, -0.996613237978246, 0.0],
                    [0.996613237978246, 0.0822317085224189, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9876883405951378, 0.0, 0.15643446504023087],
                    [0.0, 1.0, 0.0],
                    [-0.15643446504023087, 0.0, 0.9876883405951378],
                ],
            ),
        ],
        nominal_tilt_angle=9.0014,
        accumulated_dose=6.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39463.386719, defocus_v=38568.289062, defocus_angle=40.258121
        ),
        path="MotionCorr/job002/frames/TS_01_005_9_0.mrc",
        section="22",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-9.168774, -87.453127],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08207420317476882, -0.9966262213955775, 0.0],
                    [0.9966262213955775, 0.08207420317476882, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9781476007338056, 0.0, 0.20791169081775931],
                    [0.0, 0.9999999999999999, 0.0],
                    [-0.20791169081775931, 0.0, 0.9781476007338056],
                ],
            ),
        ],
        nominal_tilt_angle=12.0005,
        accumulated_dose=15.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38949.433594, defocus_v=38699.5625, defocus_angle=25.551586
        ),
        path="MotionCorr/job002/frames/TS_01_008_12_0.mrc",
        section="23",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-11.018162, -74.036338],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.0819117035158779, -0.9966395902366747, 0.0],
                    [0.9966395902366747, 0.0819117035158779, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9659258262890682, 0.0, 0.25881904510252074],
                    [0.0, 1.0, 0.0],
                    [-0.25881904510252074, 0.0, 0.9659258262890682],
                ],
            ),
        ],
        nominal_tilt_angle=15.0007,
        accumulated_dose=18.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39014.972656, defocus_v=38768.765625, defocus_angle=-0.90581
        ),
        path="MotionCorr/job002/frames/TS_01_009_15_0.mrc",
        section="24",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-15.055541, -105.101393],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08174309607665553, -0.9966534333677896, 0.0],
                    [0.9966534333677896, 0.08174309607665553, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9510565162951536, 0.0, 0.30901699437494745],
                    [0.0, 1.0, 0.0],
                    [-0.30901699437494745, 0.0, 0.9510565162951536],
                ],
            ),
        ],
        nominal_tilt_angle=18.0008,
        accumulated_dose=27.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38690.386719, defocus_v=38564.035156, defocus_angle=5.383391
        ),
        path="MotionCorr/job002/frames/TS_01_012_18_0.mrc",
        section="25",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-14.136312, -105.00574],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08156709336755857, -0.9966678530380961, 0.0],
                    [0.9966678530380961, 0.08156709336755857, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9335804264972019, 0.0, 0.3583679495453003],
                    [0.0, 1.0, 0.0],
                    [-0.3583679495453003, 0.0, 0.9335804264972019],
                ],
            ),
        ],
        nominal_tilt_angle=21.0009,
        accumulated_dose=30.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39183.546875, defocus_v=38977.851562, defocus_angle=-75.17061
        ),
        path="MotionCorr/job002/frames/TS_01_013_21_0.mrc",
        section="26",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-19.906444, -125.451695],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08138209469655766, -0.9966829760073164, 0.0],
                    [0.9966829760073164, 0.08138209469655766, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.9135454576426011, 0.0, 0.40673664307580026],
                    [0.0, 1.0000000000000002, 0.0],
                    [-0.40673664307580026, 0.0, 0.9135454576426011],
                ],
            ),
        ],
        nominal_tilt_angle=24.0006,
        accumulated_dose=39.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39091.230469, defocus_v=38781.570312, defocus_angle=76.682976
        ),
        path="MotionCorr/job002/frames/TS_01_016_24_0.mrc",
        section="27",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-15.166403, -130.853929],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08118630790594522, -0.9966989432163561, 0.0],
                    [0.9966989432163561, 0.08118630790594522, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.8910065241883678, 0.0, 0.45399049973954675],
                    [0.0, 1.0, 0.0],
                    [-0.45399049973954675, 0.0, 0.8910065241883678],
                ],
            ),
        ],
        nominal_tilt_angle=27.0007,
        accumulated_dose=42.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38935.335938, defocus_v=38806.46875, defocus_angle=-83.8278
        ),
        path="MotionCorr/job002/frames/TS_01_017_27_0.mrc",
        section="28",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-24.585325, -142.198395],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08097769715612912, -0.9967159136701341, 0.0],
                    [0.9967159136701341, 0.08097769715612912, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.8660254037844387, 0.0, 0.49999999999999994],
                    [0.0, 1.0, 0.0],
                    [-0.49999999999999994, 0.0, 0.8660254037844387],
                ],
            ),
        ],
        nominal_tilt_angle=30.0008,
        accumulated_dose=51.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38910.875, defocus_v=38214.078125, defocus_angle=55.941147
        ),
        path="MotionCorr/job002/frames/TS_01_020_30_0.mrc",
        section="29",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-20.100055, -128.847136],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08075360016907701, -0.9967340949620077, 0.0],
                    [0.9967340949620077, 0.08075360016907701, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.838670567945424, 0.0, 0.5446390350150271],
                    [0.0, 1.0, 0.0],
                    [-0.5446390350150271, 0.0, 0.838670567945424],
                ],
            ),
        ],
        nominal_tilt_angle=33.001,
        accumulated_dose=54.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38949.035156, defocus_v=38796.992188, defocus_angle=45.229416
        ),
        path="MotionCorr/job002/frames/TS_01_021_33_0.mrc",
        section="30",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-22.668676, -156.078011],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.08051069335216726, -0.9967537450423516, 0.0],
                    [0.9967537450423516, 0.08051069335216726, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.8090169943749473, 0.0, 0.587785252292473],
                    [0.0, 0.9999999999999999, 0.0],
                    [-0.587785252292473, 0.0, 0.8090169943749473],
                ],
            ),
        ],
        nominal_tilt_angle=36.0006,
        accumulated_dose=63.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38909.515625, defocus_v=38473.996094, defocus_angle=34.372036
        ),
        path="MotionCorr/job002/frames/TS_01_024_36_0.mrc",
        section="31",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-8.901784, -138.030123],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.0802453918245975, -0.9967751386801925, 0.0],
                    [0.9967751386801925, 0.0802453918245975, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.7771459614569709, 0.0, 0.6293203910498374],
                    [0.0, 1.0, 0.0],
                    [-0.6293203910498374, 0.0, 0.7771459614569709],
                ],
            ),
        ],
        nominal_tilt_angle=39.0007,
        accumulated_dose=66.0,
        ctf_metadata=CTFMetadata(
            defocus_u=39229.929688, defocus_v=38722.871094, defocus_angle=40.212944
        ),
        path="MotionCorr/job002/frames/TS_01_025_39_0.mrc",
        section="32",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-25.537779, -165.243161],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.07995209219591515, -0.9967987073393986, 0.0],
                    [0.9967987073393986, 0.07995209219591515, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.7431448254773942, 0.0, 0.6691306063588582],
                    [0.0, 1.0, 0.0],
                    [-0.6691306063588582, 0.0, 0.7431448254773942],
                ],
            ),
        ],
        nominal_tilt_angle=42.0009,
        accumulated_dose=75.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38625.375, defocus_v=38329.550781, defocus_angle=38.231094
        ),
        path="MotionCorr/job002/frames/TS_01_028_42_0.mrc",
        section="33",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-10.783477, -146.425472],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.07962510340203871, -0.9968248807630229, 0.0],
                    [0.9968248807630229, 0.07962510340203871, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.7071067811865475, 0.0, 0.7071067811865476],
                    [0.0, 1.0, 0.0],
                    [-0.7071067811865476, 0.0, 0.7071067811865475],
                ],
            ),
        ],
        nominal_tilt_angle=45.001,
        accumulated_dose=78.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38758.140625, defocus_v=38564.382812, defocus_angle=53.667973
        ),
        path="MotionCorr/job002/frames/TS_01_029_45_0.mrc",
        section="34",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-28.227257, -169.437971],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.07925539306415036, -0.9968543437585288, 0.0],
                    [0.9968543437585288, 0.07925539306415036, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.6691306063588581, 0.0, 0.7431448254773942],
                    [0.0, 0.9999999999999999, 0.0],
                    [-0.7431448254773942, 0.0, 0.6691306063588581],
                ],
            ),
        ],
        nominal_tilt_angle=48.0006,
        accumulated_dose=87.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38438.015625, defocus_v=38173.0625, defocus_angle=63.245338
        ),
        path="MotionCorr/job002/frames/TS_01_032_48_0.mrc",
        section="35",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-8.804052, -143.820056],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.07883189170262078, -0.9968879239165184, 0.0],
                    [0.9968879239165184, 0.07883189170262078, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.6293203910498375, 0.0, 0.7771459614569709],
                    [0.0, 1.0, 0.0],
                    [-0.7771459614569709, 0.0, 0.6293203910498375],
                ],
            ),
        ],
        nominal_tilt_angle=51.0008,
        accumulated_dose=90.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38861.210938, defocus_v=38739.855469, defocus_angle=21.330759
        ),
        path="MotionCorr/job002/frames/TS_01_033_51_0.mrc",
        section="36",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-29.571601, -162.395054],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.0783387950841059, -0.9969267942957349, 0.0],
                    [0.9969267942957349, 0.0783387950841059, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.5877852522924732, 0.0, 0.8090169943749475],
                    [0.0, 1.0000000000000002, 0.0],
                    [-0.8090169943749475, 0.0, 0.5877852522924732],
                ],
            ),
        ],
        nominal_tilt_angle=54.0009,
        accumulated_dose=99.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38656.089844, defocus_v=38493.3125, defocus_angle=-8.29779
        ),
        path="MotionCorr/job002/frames/TS_01_036_54_0.mrc",
        section="37",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-11.98729, -137.537965],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.07775420544186928, -0.9969725590687557, 0.0],
                    [0.9969725590687557, 0.07775420544186928, 0.0],
                    [0.0, 0.0, 0.9999999999999999],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.5446390350150272, 0.0, 0.838670567945424],
                    [0.0, 1.0, 0.0],
                    [-0.838670567945424, 0.0, 0.5446390350150272],
                ],
            ),
        ],
        nominal_tilt_angle=57.0,
        accumulated_dose=102.0,
        ctf_metadata=CTFMetadata(
            defocus_u=37450.847656, defocus_v=37448.03125, defocus_angle=-35.11659
        ),
        path="MotionCorr/job002/frames/TS_01_037_57_0.mrc",
        section="38",
    ),
    ProjectionImage(
        width=2000,
        height=2000,
        coordinate_systems=[
            CoordinateSystem(
                name="alignment y tilt",
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
            CoordinateSystem(
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
                name="alignment y tilt",
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
        ],
        coordinate_transformations=[
            Scale(
                type="scale",
                name="Å/pix",
                input="logical",
                output="physical",
                scale=[1.35],
            ),
            Translation(
                type="translation",
                name="Tilt image alignment translation",
                input="logical",
                output="alignment translation",
                translation=[-27.89235, -156.675694],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x rotation",
                input="alignment translation",
                output="alignment z rotation",
                affine=[
                    [0.07704550017872136, -0.9970275778042504, 0.0],
                    [0.9970275778042504, 0.07704550017872136, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment x tilt",
                input="alignment z rotation",
                output="alignment x tilt",
                affine=[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            ),
            Affine(
                type="affine",
                name="Tilt image alignment y tilt",
                input="alignment x tilt",
                output="alignment y tilt",
                affine=[
                    [0.5000000000000002, 0.0, 0.8660254037844386],
                    [0.0, 1.0, 0.0],
                    [-0.8660254037844386, 0.0, 0.5000000000000002],
                ],
            ),
        ],
        nominal_tilt_angle=60.0006,
        accumulated_dose=111.0,
        ctf_metadata=CTFMetadata(
            defocus_u=38544.476562, defocus_v=38449.148438, defocus_angle=-10.13496
        ),
        path="MotionCorr/job002/frames/TS_01_040_60_0.mrc",
        section="39",
    ),
]
