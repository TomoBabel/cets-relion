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
                [0.9910488295477008, -0.13337511157340148, 0.005770360899859925],
                [-0.133499618837432, -0.9900355054638975, 0.04480568815569209],
                [-0.00026310148668653435, -0.04517496578446365, -0.9989790554581112],
            ],
        ),
        Affine(
            type="affine",
            name="Averaging alignment",
            input="Averaging translation",
            output="Alignment for averaging",
            affine=[
                [-0.10251085961280204, 0.057973834532939375, 0.9930410657022155],
                [-0.08628111017328001, 0.994019574957615, -0.06693769213491753],
                [-0.9909828927326196, -0.09254252595769173, -0.09689575429635322],
            ],
        ),
        Translation(
            type="translation",
            name="Averaging translation",
            input="Alignment relative to parent tomogram",
            output="Averaging translation",
            translation=[-37.72984, -37.72984, 17.57898],
        ),
    ],
    path="000001@Extract/job010/Subtomograms/TS_01/1_stack2d.mrcs",
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
                [0.13092364625824407, -0.9698575059870079, -0.20551257122401773],
                [-0.9909367229741296, -0.12173608334852255, -0.056786768461101464],
                [0.030056778133049328, 0.21108468464486557, -0.977005550647814],
            ],
        ),
        Affine(
            type="affine",
            name="Averaging alignment",
            input="Averaging translation",
            output="Alignment for averaging",
            affine=[
                [-0.12565781272105925, -0.11642509927386767, 0.9852184074413294],
                [-0.03202850847922693, 0.9930484030505851, 0.11326536912613247],
                [-0.991556498010454, -0.017322397575191877, -0.12851321253276526],
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
    path="000012@Extract/job020/Subtomograms/TS_01/12_stack2d.mrcs",
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
                [0.13092364625824407, -0.9698575059870079, -0.20551257122401773],
                [-0.9909367229741296, -0.12173608334852255, -0.056786768461101464],
                [0.030056778133049328, 0.21108468464486557, -0.977005550647814],
            ],
        ),
        Affine(
            type="affine",
            name="Averaging alignment",
            input="Averaging translation",
            output="Alignment for averaging",
            affine=[
                [-0.12859958749903055, -0.08704297677291388, 0.9878692556657431],
                [-0.03642505354906922, 0.9958830256812498, 0.08300731674922938],
                [-0.9910274272536692, -0.025308483843751572, -0.131240691389919],
            ],
        ),
        Translation(
            type="translation",
            name="Averaging translation",
            input="Alignment relative to parent tomogram",
            output="Averaging translation",
            translation=[0.276596, -0.08993, -0.08993],
        ),
    ],
    path="000012@Extract/job041/Subtomograms/TS_01/12_stack2d.mrcs",
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
