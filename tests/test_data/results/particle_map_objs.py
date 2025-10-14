from cets_data_model.models.models import (
    ParticleMap,
    Axis,
    CoordinateSystem,
    Affine,
    Translation,
    Scale,
)

FROM_REFINE = ParticleMap(
    width=127,
    height=127,
    depth=127,
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
        CoordinateSystem(
            name="Alignment relative to parent tomogram",
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
            name="Averaging translation",
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
            name="Averaging alignment",
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
            name="Å/pix",
            input="logical coordinates",
            output="physical coordinates",
            scale=[8.1],
        ),
        Affine(
            type="affine",
            name="Alignment relative to parent tomogram",
            input="physical coordinates",
            output="Alignment relative to parent tomogram",
            affine=[
                [0.20048649669676377, -0.979636773216343, 0.010814675424154076],
                [-0.9796963406311693, -0.2004686807592746, 0.002718122243769175],
                [-0.0004947687889736855, -0.011140044744404417, -0.9999378253706267],
            ],
        ),
        Affine(
            type="affine",
            name="Averaging alignment",
            input="Averaging translation",
            output="Alignment for averaging",
            affine=[
                [-0.04163069094218097, -0.15169932667815733, 0.9875495936190092],
                [0.38271226340456055, 0.910599515439265, 0.1560123261846128],
                [-0.9229291462574117, 0.3844422411327474, 0.020148305670593614],
            ],
        ),
        Translation(
            type="translation",
            name="Averaging translation",
            input="Alignment relative to parent tomogram",
            output="Averaging translation",
            translation=[22.89663, -41.90337, -21.52984],
        ),
    ],
    path="000001@Extract/job010/Subtomograms/TS_03/1_stack2d.mrcs",
)
FROM_CL3D = ParticleMap(
    width=127,
    height=127,
    depth=127,
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
        CoordinateSystem(
            name="Alignment relative to parent tomogram",
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
            name="Averaging translation",
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
            name="Averaging alignment",
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
            name="Å/pix",
            input="logical coordinates",
            output="physical coordinates",
            scale=[2.7],
        ),
        Affine(
            type="affine",
            name="Alignment relative to parent tomogram",
            input="physical coordinates",
            output="Alignment relative to parent tomogram",
            affine=[
                [0.7100144978744788, -0.7013855000136974, -0.06275183804947496],
                [-0.704186973868551, -0.7072332593747975, -0.06278393638466066],
                [-0.00034444434150621844, 0.08876653200748723, -0.996052400305054],
            ],
        ),
        Affine(
            type="affine",
            name="Averaging alignment",
            input="Averaging translation",
            output="Alignment for averaging",
            affine=[
                [-0.042992396110853204, -0.12391516413921591, 0.9913610270597681],
                [-0.19432190259434526, 0.9743652750377132, 0.11336361397201085],
                [-0.9799952306255173, -0.18776938753969585, -0.06596972831690479],
            ],
        ),
        Translation(
            type="translation",
            name="Averaging translation",
            input="Alignment relative to parent tomogram",
            output="Averaging translation",
            translation=[1.642283, -3.75772, -1.05772],
        ),
    ],
    path="000002@Extract/job013/Subtomograms/TS_03/2_stack2d.mrcs",
)
FROM_REC = ParticleMap(
    width=127,
    height=127,
    depth=127,
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
        CoordinateSystem(
            name="Alignment relative to parent tomogram",
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
            name="Averaging translation",
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
            name="Averaging alignment",
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
            name="Å/pix",
            input="logical coordinates",
            output="physical coordinates",
            scale=[1.35],
        ),
        Affine(
            type="affine",
            name="Alignment relative to parent tomogram",
            input="physical coordinates",
            output="Alignment relative to parent tomogram",
            affine=[
                [0.7100144978744788, -0.7013855000136974, -0.06275183804947496],
                [-0.704186973868551, -0.7072332593747975, -0.06278393638466066],
                [-0.00034444434150621844, 0.08876653200748723, -0.996052400305054],
            ],
        ),
        Affine(
            type="affine",
            name="Averaging alignment",
            input="Averaging translation",
            output="Alignment for averaging",
            affine=[
                [-0.042992396110853204, -0.12391516413921591, 0.9913610270597681],
                [-0.19432190259434526, 0.9743652750377132, 0.11336361397201085],
                [-0.9799952306255173, -0.18776938753969585, -0.06596972831690479],
            ],
        ),
        Translation(
            type="translation",
            name="Averaging translation",
            input="Alignment relative to parent tomogram",
            output="Averaging translation",
            translation=[0.0, 0.0, 0.0],
        ),
    ],
    path="000002@Extract/job020/Subtomograms/TS_03/2_stack2d.mrcs",
)
FROM_PP = ParticleMap(
    width=127,
    height=127,
    depth=127,
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
        CoordinateSystem(
            name="Alignment relative to parent tomogram",
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
            name="Averaging translation",
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
            name="Averaging alignment",
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
            name="Å/pix",
            input="logical coordinates",
            output="physical coordinates",
            scale=[1.35],
        ),
        Affine(
            type="affine",
            name="Alignment relative to parent tomogram",
            input="physical coordinates",
            output="Alignment relative to parent tomogram",
            affine=[
                [0.7100144978744788, -0.7013855000136974, -0.06275183804947496],
                [-0.704186973868551, -0.7072332593747975, -0.06278393638466066],
                [-0.00034444434150621844, 0.08876653200748723, -0.996052400305054],
            ],
        ),
        Affine(
            type="affine",
            name="Averaging alignment",
            input="Averaging translation",
            output="Alignment for averaging",
            affine=[
                [-0.02013095786431035, -0.14771367910226968, 0.9888252694695546],
                [-0.20999203221069296, 0.9675891309422759, 0.14026624715302893],
                [-0.9774958265606503, -0.2048217339259753, -0.05049719168496736],
            ],
        ),
        Translation(
            type="translation",
            name="Averaging translation",
            input="Alignment relative to parent tomogram",
            output="Averaging translation",
            translation=[-0.08993, -0.08993, 0.276596],
        ),
    ],
    path="000002@Extract/job041/Subtomograms/TS_03/2_stack2d.mrcs",
)

TS_01_1 = {
    "coordinate_systems": [
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
        CoordinateSystem(
            name="Alignment relative to parent tomogram",
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
            name="Averaging translation",
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
            name="Averaging alignment",
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
    "coordinate_transformations": [
        Scale(
            type="scale",
            name="Å/pix",
            input="logical coordinates",
            output="physical coordinates",
            scale=[8.1],
        ),
        Affine(
            type="affine",
            name="Alignment relative to parent tomogram",
            input="physical coordinates",
            output="Alignment relative to parent tomogram",
            affine=[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]],
        ),
        Affine(
            type="affine",
            name="Averaging alignment",
            input="Averaging translation",
            output="Alignment for averaging",
            affine=[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]],
        ),
        Translation(
            type="translation",
            name="Averaging translation",
            input="Alignment relative to parent tomogram",
            output="Averaging translation",
            translation=[0.0, 0.0, 0.0],
        ),
    ],
    "depth": 3,
    "height": 2,
    "path": "000001@Extract/job010/Subtomograms/TS_01/1_stack2d.mrcs",
    "width": 1,
}
