MOCORR_0 = {
    "accumulated_dose": 3.0,
    "coordinate_systems": [
        {
            "axes": [
                {
                    "axis_type": None,
                    "axis_unit": "pixel",
                    "name": "logical coordinates x axis",
                },
                {
                    "axis_type": None,
                    "axis_unit": "pixel",
                    "name": "logical coordinates y axis",
                },
            ],
            "name": "base_logical_coordinates_2d",
        }
    ],
    "coordinate_transformations": [],
    "ctf_metadata": None,
    "height": 2000,
    "id": "MotionCorr/job002/frames/TS_01_000_0_0.mrc",
    "movie_stack_id": None,
    "nominal_tilt_angle": 0.001,
    "path": "MotionCorr/job002/frames/TS_01_000_0_0.mrc",
    "section": 0,
    "width": 2000,
}
MOCORR_40 = {
    "accumulated_dose": 123.0,
    "coordinate_systems": [
        {
            "axes": [
                {
                    "axis_type": None,
                    "axis_unit": "pixel",
                    "name": "logical coordinates x axis",
                },
                {
                    "axis_type": None,
                    "axis_unit": "pixel",
                    "name": "logical coordinates y axis",
                },
            ],
            "name": "base_logical_coordinates_2d",
        }
    ],
    "coordinate_transformations": [],
    "ctf_metadata": None,
    "height": 2000,
    "id": "MotionCorr/job002/frames/TS_01_040_60_0.mrc",
    "movie_stack_id": None,
    "nominal_tilt_angle": 60.0006,
    "path": "MotionCorr/job002/frames/TS_01_040_60_0.mrc",
    "section": 40,
    "width": 2000,
}

CTF_0 = {
    "width": 2000,
    "height": 2000,
    "coordinate_systems": [
        {
            "name": "base_logical_coordinates_3d",
            "axes": [
                {
                    "name": "logical coordinates x axis",
                    "axis_unit": "pixel",
                    "axis_type": None,
                },
                {
                    "name": "logical coordinates y axis",
                    "axis_unit": "pixel",
                    "axis_type": None,
                },
                {
                    "name": "logical coordinates z axis",
                    "axis_unit": "pixel",
                    "axis_type": None,
                },
            ],
        },
        {
            "name": "image_pixel_size",
            "axes": [
                {
                    "name": "physical coordinates x axis",
                    "axis_unit": "angstrom",
                    "axis_type": None,
                },
                {
                    "name": "physical coordinates y axis",
                    "axis_unit": "angstrom",
                    "axis_type": None,
                },
                {
                    "name": "physical coordinates z axis",
                    "axis_unit": "angstrom",
                    "axis_type": None,
                },
            ],
        },
    ],
    "coordinate_transformations": [
        {
            "transformation_type": "scale",
            "name": "image_pixel_size",
            "input": "base_logical_coordinates_3d",
            "output": "image_pixel_size",
            "scale": [1.35],
        }
    ],
    "nominal_tilt_angle": 0.001,
    "accumulated_dose": 3.0,
    "ctf_metadata": {
        "defocus_u": 38855.828125,
        "defocus_v": 38750.828125,
        "defocus_angle": 35.154533,
        "phase_shift": None,
        "defocus_handedness": -1,
    },
    "path": "MotionCorr/job002/frames/TS_01_000_0_0.mrc",
    "section": 0,
    "id": "MotionCorr/job002/frames/TS_01_000_0_0.mrc",
    "movie_stack_id": None,
}
CTF_40 = {
    "width": 2000,
    "height": 2000,
    "coordinate_systems": [
        {
            "name": "base_logical_coordinates_3d",
            "axes": [
                {
                    "name": "logical coordinates x axis",
                    "axis_unit": "pixel",
                    "axis_type": None,
                },
                {
                    "name": "logical coordinates y axis",
                    "axis_unit": "pixel",
                    "axis_type": None,
                },
                {
                    "name": "logical coordinates z axis",
                    "axis_unit": "pixel",
                    "axis_type": None,
                },
            ],
        },
        {
            "name": "image_pixel_size",
            "axes": [
                {
                    "name": "physical coordinates x axis",
                    "axis_unit": "angstrom",
                    "axis_type": None,
                },
                {
                    "name": "physical coordinates y axis",
                    "axis_unit": "angstrom",
                    "axis_type": None,
                },
                {
                    "name": "physical coordinates z axis",
                    "axis_unit": "angstrom",
                    "axis_type": None,
                },
            ],
        },
    ],
    "coordinate_transformations": [
        {
            "transformation_type": "scale",
            "name": "image_pixel_size",
            "input": "base_logical_coordinates_3d",
            "output": "image_pixel_size",
            "scale": [1.35],
        }
    ],
    "nominal_tilt_angle": 60.0006,
    "accumulated_dose": 123.0,
    "ctf_metadata": {
        "defocus_u": 38544.476562,
        "defocus_v": 38449.148438,
        "defocus_angle": -10.13496,
        "phase_shift": None,
        "defocus_handedness": -1,
    },
    "path": "MotionCorr/job002/frames/TS_01_040_60_0.mrc",
    "section": 40,
    "id": "MotionCorr/job002/frames/TS_01_040_60_0.mrc",
    "movie_stack_id": None,
}
GAIN_FILE = {
    "width": 2000,
    "height": 2000,
    "coordinate_systems": [
        {
            "name": "base_logical_coordinates_2d",
            "axes": [
                {
                    "name": "logical coordinates x axis",
                    "axis_unit": "pixel",
                    "axis_type": None,
                },
                {
                    "name": "logical coordinates y axis",
                    "axis_unit": "pixel",
                    "axis_type": None,
                },
            ],
        },
    ],
    "coordinate_transformations": [],
    "path": "gain_reference.mrc",
}
