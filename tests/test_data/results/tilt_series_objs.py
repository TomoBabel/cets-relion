MOCORR_0 = {
    "acquisition_order": None,
    "accumulated_dose": 3.0,
    "coordinate_systems": [
        {
            "axes": [
                {
                    "axis_type": "array",
                    "axis_unit": "pixel",
                    "name": "logical coordinates x axis",
                },
                {
                    "axis_type": "array",
                    "axis_unit": "pixel",
                    "name": "logical coordinates y axis",
                },
            ],
            "name": "logical coordinates 2d",
        }
    ],
    "coordinate_transformations": [],
    "ctf_metadata": None,
    "exposure_time": None,
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
    "acquisition_order": None,
    "coordinate_systems": [
        {
            "axes": [
                {
                    "axis_type": "array",
                    "axis_unit": "pixel",
                    "name": "logical coordinates x axis",
                },
                {
                    "axis_type": "array",
                    "axis_unit": "pixel",
                    "name": "logical coordinates y axis",
                },
            ],
            "name": "logical coordinates 2d",
        }
    ],
    "coordinate_transformations": [],
    "ctf_metadata": None,
    "exposure_time": None,
    "height": 2000,
    "id": "MotionCorr/job002/frames/TS_01_040_60_0.mrc",
    "movie_stack_id": None,
    "nominal_tilt_angle": 60.0006,
    "path": "MotionCorr/job002/frames/TS_01_040_60_0.mrc",
    "section": 40,
    "width": 2000,
}

CTF_0 = {
    "acquisition_order": None,
    "width": 2000,
    "exposure_time": None,
    "height": 2000,
    "coordinate_systems": [
        {
            "name": "logical coordinates 3d",
            "axes": [
                {
                    "name": "logical coordinates x axis",
                    "axis_unit": "pixel",
                    "axis_type": "array",
                },
                {
                    "name": "logical coordinates y axis",
                    "axis_unit": "pixel",
                    "axis_type": "array",
                },
                {
                    "name": "logical coordinates z axis",
                    "axis_unit": "pixel",
                    "axis_type": "array",
                },
            ],
        },
        {
            "name": "image_pixel_size",
            "axes": [
                {
                    "name": "physical coordinates x axis",
                    "axis_unit": "angstrom",
                    "axis_type": "space",
                },
                {
                    "name": "physical coordinates y axis",
                    "axis_unit": "angstrom",
                    "axis_type": "space",
                },
                {
                    "name": "physical coordinates z axis",
                    "axis_unit": "angstrom",
                    "axis_type": "space",
                },
            ],
        },
    ],
    "coordinate_transformations": [
        {
            "transformation_type": "scale",
            "name": "image_pixel_size",
            "input": "logical coordinates 3d",
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
    },
    "path": "MotionCorr/job002/frames/TS_01_000_0_0.mrc",
    "section": 0,
    "id": "MotionCorr/job002/frames/TS_01_000_0_0.mrc",
    "movie_stack_id": None,
}
CTF_40 = {
    "accumulated_dose": 123.0,
    "acquisition_order": None,
    "coordinate_systems": [
        {
            "axes": [
                {
                    "axis_type": "array",
                    "axis_unit": "pixel",
                    "name": "logical coordinates x axis",
                },
                {
                    "axis_type": "array",
                    "axis_unit": "pixel",
                    "name": "logical coordinates y axis",
                },
                {
                    "axis_type": "array",
                    "axis_unit": "pixel",
                    "name": "logical coordinates z axis",
                },
            ],
            "name": "logical coordinates 3d",
        },
        {
            "axes": [
                {
                    "axis_type": "space",
                    "axis_unit": "angstrom",
                    "name": "physical coordinates x axis",
                },
                {
                    "axis_type": "space",
                    "axis_unit": "angstrom",
                    "name": "physical coordinates y axis",
                },
                {
                    "axis_type": "space",
                    "axis_unit": "angstrom",
                    "name": "physical coordinates z axis",
                },
            ],
            "name": "image_pixel_size",
        },
    ],
    "coordinate_transformations": [
        {
            "input": "logical coordinates 3d",
            "name": "image_pixel_size",
            "output": "image_pixel_size",
            "scale": [1.35],
            "transformation_type": "scale",
        }
    ],
    "ctf_metadata": {
        "defocus_angle": -10.13496,
        "defocus_u": 38544.476562,
        "defocus_v": 38449.148438,
        "phase_shift": None,
    },
    "exposure_time": None,
    "height": 2000,
    "id": "MotionCorr/job002/frames/TS_01_040_60_0.mrc",
    "movie_stack_id": None,
    "nominal_tilt_angle": 60.0006,
    "path": "MotionCorr/job002/frames/TS_01_040_60_0.mrc",
    "section": 40,
    "width": 2000,
}
GAIN_FILE = {
    "coordinate_systems": [
        {
            "axes": [
                {
                    "axis_type": "array",
                    "axis_unit": "pixel",
                    "name": "logical coordinates x axis",
                },
                {
                    "axis_type": "array",
                    "axis_unit": "pixel",
                    "name": "logical coordinates y axis",
                },
            ],
            "name": "logical coordinates 2d",
        }
    ],
    "coordinate_transformations": [],
    "height": 2000,
    "id": "gain_reference.mrc",
    "path": "gain_reference.mrc",
    "width": 2000,
}
