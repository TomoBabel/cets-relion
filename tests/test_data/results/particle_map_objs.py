from cets_data_model.models.models import (
    ParticleMap,
    Axis,
    CoordinateSystem,
    Affine,
    Translation,
    Scale,
    Sequence,
)

FROM_REFINE = ParticleMap(
    id="Extract/job010/Subtomograms/TS_01/1_stack2d.mrcs",
    width=127,
    height=127,
    depth=127,
    coordinate_systems=[
        CoordinateSystem(
            name="logical coordinates 3d",
            axes=[
                Axis(
                    name="logical coordinates x axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates y axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates z axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
            ],
        ),
        CoordinateSystem(
            name="image_pixel_size",
            axes=[
                Axis(
                    name="physical coordinates x axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates y axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates z axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
            ],
        ),
        CoordinateSystem(
            name="Alignment relative to parent tomogram",
            axes=[
                Axis(
                    name="physical coordinates x axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates y axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates z axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
            ],
        ),
        CoordinateSystem(
            name="Averaging translation",
            axes=[
                Axis(
                    name="logical coordinates x axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates y axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates z axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
            ],
        ),
        CoordinateSystem(
            name="aligned_subtomogram",
            axes=[
                Axis(
                    name="physical coordinates x axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates y axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates z axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
            ],
        ),
    ],
    coordinate_transformations=[
        Scale(
            name="Å/pix",
            input="logical coordinates 3d",
            output="image_pixel_size",
            scale=[8.1],
        ),
        Sequence(
            name="align_subtomogram_to_tomogram",
            input="image_pixel_size",
            output="aligned_subtomogram",
            sequence=[
                Affine(
                    name="Alignment relative to parent tomogram",
                    input="image_pixel_size",
                    output="Alignment relative to parent tomogram",
                    affine=[
                        [
                            0.9910488295477008,
                            -0.13337511157340148,
                            0.005770360899859925,
                        ],
                        [-0.133499618837432, -0.9900355054638975, 0.04480568815569209],
                        [
                            -0.00026310148668653435,
                            -0.04517496578446365,
                            -0.9989790554581112,
                        ],
                    ],
                ),
                Translation(
                    name="Averaging translation",
                    input="Alignment relative to parent tomogram",
                    output="Averaging translation",
                    translation=[
                        -4.658004938271605,
                        -4.658004938271605,
                        2.1702444444444446,
                    ],
                ),
                Affine(
                    name="Averaging alignment",
                    input="Averaging translation",
                    output=None,
                    affine=[
                        [
                            -0.10251085961280204,
                            0.057973834532939375,
                            0.9930410657022155,
                        ],
                        [-0.08628111017328001, 0.994019574957615, -0.06693769213491753],
                        [
                            -0.9909828927326196,
                            -0.09254252595769173,
                            -0.09689575429635322,
                        ],
                    ],
                ),
            ],
        ),
    ],
    path="Extract/job010/Subtomograms/TS_01/1_stack2d.mrcs",
)
FROM_REC = ParticleMap(
    id="Extract/job020/Subtomograms/TS_01/12_stack2d.mrcs",
    width=127,
    height=127,
    depth=127,
    coordinate_systems=[
        CoordinateSystem(
            name="logical coordinates 3d",
            axes=[
                Axis(
                    name="logical coordinates x axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates y axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates z axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
            ],
        ),
        CoordinateSystem(
            name="image_pixel_size",
            axes=[
                Axis(
                    name="physical coordinates x axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates y axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates z axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
            ],
        ),
        CoordinateSystem(
            name="Alignment relative to parent tomogram",
            axes=[
                Axis(
                    name="physical coordinates x axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates y axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates z axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
            ],
        ),
        CoordinateSystem(
            name="Averaging translation",
            axes=[
                Axis(
                    name="logical coordinates x axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates y axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates z axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
            ],
        ),
        CoordinateSystem(
            name="aligned_subtomogram",
            axes=[
                Axis(
                    name="physical coordinates x axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates y axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates z axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
            ],
        ),
    ],
    coordinate_transformations=[
        Scale(
            name="Å/pix",
            input="logical coordinates 3d",
            output="image_pixel_size",
            scale=[1.35],
        ),
        Sequence(
            name="align_subtomogram_to_tomogram",
            input="image_pixel_size",
            output="aligned_subtomogram",
            sequence=[
                Affine(
                    name="Alignment relative to parent tomogram",
                    input="image_pixel_size",
                    output="Alignment relative to parent tomogram",
                    affine=[
                        [
                            0.13092364625824407,
                            -0.9698575059870079,
                            -0.20551257122401773,
                        ],
                        [
                            -0.9909367229741296,
                            -0.12173608334852255,
                            -0.056786768461101464,
                        ],
                        [0.030056778133049328, 0.21108468464486557, -0.977005550647814],
                    ],
                ),
                Translation(
                    name="Averaging translation",
                    input="Alignment relative to parent tomogram",
                    output="Averaging translation",
                    translation=[0.0, 0.0, 0.0],
                ),
                Affine(
                    name="Averaging alignment",
                    input="Averaging translation",
                    output=None,
                    affine=[
                        [
                            -0.12565781272105925,
                            -0.11642509927386767,
                            0.9852184074413294,
                        ],
                        [-0.03202850847922693, 0.9930484030505851, 0.11326536912613247],
                        [
                            -0.991556498010454,
                            -0.017322397575191877,
                            -0.12851321253276526,
                        ],
                    ],
                ),
            ],
        ),
    ],
    path="Extract/job020/Subtomograms/TS_01/12_stack2d.mrcs",
)

FROM_PP = ParticleMap(
    id="Extract/job041/Subtomograms/TS_01/12_stack2d.mrcs",
    width=127,
    height=127,
    depth=127,
    coordinate_systems=[
        CoordinateSystem(
            name="logical coordinates 3d",
            axes=[
                Axis(
                    name="logical coordinates x axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates y axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates z axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
            ],
        ),
        CoordinateSystem(
            name="image_pixel_size",
            axes=[
                Axis(
                    name="physical coordinates x axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates y axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates z axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
            ],
        ),
        CoordinateSystem(
            name="Alignment relative to parent tomogram",
            axes=[
                Axis(
                    name="physical coordinates x axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates y axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates z axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
            ],
        ),
        CoordinateSystem(
            name="Averaging translation",
            axes=[
                Axis(
                    name="logical coordinates x axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates y axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates z axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
            ],
        ),
        CoordinateSystem(
            name="aligned_subtomogram",
            axes=[
                Axis(
                    name="physical coordinates x axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates y axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates z axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
            ],
        ),
    ],
    coordinate_transformations=[
        Scale(
            name="Å/pix",
            input="logical coordinates 3d",
            output="image_pixel_size",
            scale=[1.35],
        ),
        Sequence(
            name="align_subtomogram_to_tomogram",
            input="image_pixel_size",
            output="aligned_subtomogram",
            sequence=[
                Affine(
                    name="Alignment relative to parent tomogram",
                    input="image_pixel_size",
                    output="Alignment relative to parent tomogram",
                    affine=[
                        [
                            0.13092364625824407,
                            -0.9698575059870079,
                            -0.20551257122401773,
                        ],
                        [
                            -0.9909367229741296,
                            -0.12173608334852255,
                            -0.056786768461101464,
                        ],
                        [0.030056778133049328, 0.21108468464486557, -0.977005550647814],
                    ],
                ),
                Translation(
                    name="Averaging translation",
                    input="Alignment relative to parent tomogram",
                    output="Averaging translation",
                    translation=[
                        0.20488592592592592,
                        -0.06661481481481481,
                        -0.06661481481481481,
                    ],
                ),
                Affine(
                    name="Averaging alignment",
                    input="Averaging translation",
                    output=None,
                    affine=[
                        [
                            -0.12859958749903055,
                            -0.08704297677291388,
                            0.9878692556657431,
                        ],
                        [-0.03642505354906922, 0.9958830256812498, 0.08300731674922938],
                        [
                            -0.9910274272536692,
                            -0.025308483843751572,
                            -0.131240691389919,
                        ],
                    ],
                ),
            ],
        ),
    ],
    path="Extract/job041/Subtomograms/TS_01/12_stack2d.mrcs",
)

TS_01_1 = {
    "id": "Extract/job010/Subtomograms/TS_01/1_stack2d.mrcs",
    "coord_index": None,
    "coordinate_systems": [
        CoordinateSystem(
            name="logical coordinates 3d",
            axes=[
                Axis(
                    name="logical coordinates x axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates y axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates z axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
            ],
        ),
        CoordinateSystem(
            name="image_pixel_size",
            axes=[
                Axis(
                    name="physical coordinates x axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates y axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates z axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
            ],
        ),
        CoordinateSystem(
            name="Alignment relative to parent tomogram",
            axes=[
                Axis(
                    name="physical coordinates x axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates y axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates z axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
            ],
        ),
        CoordinateSystem(
            name="Averaging translation",
            axes=[
                Axis(
                    name="logical coordinates x axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates y axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
                Axis(
                    name="logical coordinates z axis",
                    axis_unit="pixel",
                    axis_type="array",
                ),
            ],
        ),
        CoordinateSystem(
            name="aligned_subtomogram",
            axes=[
                Axis(
                    name="physical coordinates x axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates y axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
                Axis(
                    name="physical coordinates z axis",
                    axis_unit="angstrom",
                    axis_type="space",
                ),
            ],
        ),
    ],
    "coordinate_transformations": [
        Scale(
            transformation_type="scale",
            name="Å/pix",
            input="logical coordinates 3d",
            output="image_pixel_size",
            scale=[8.1],
        ),
        Sequence(
            transformation_type="sequence",
            name="align_subtomogram_to_tomogram",
            input="image_pixel_size",
            output="aligned_subtomogram",
            sequence=[
                Affine(
                    transformation_type="affine",
                    name="Alignment relative to parent tomogram",
                    input="image_pixel_size",
                    output="Alignment relative to parent tomogram",
                    affine=[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]],
                ),
                Translation(
                    transformation_type="translation",
                    name="Averaging translation",
                    input="Alignment relative to parent tomogram",
                    output="Averaging translation",
                    translation=[0.0, 0.0, 0.0],
                ),
                Affine(
                    transformation_type="affine",
                    name="Averaging alignment",
                    input="Averaging translation",
                    output=None,
                    affine=[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]],
                ),
            ],
        ),
    ],
    "depth": 3,
    "height": 2,
    "path": "Extract/job010/Subtomograms/TS_01/1_stack2d.mrcs",
    "source_annotation_id": None,
    "source_region_id": None,
    "width": 1,
}
