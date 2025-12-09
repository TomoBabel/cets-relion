MOCORR_0 = {
    "accumulated_dose": 3.0,
    "acquisition_order": None,
    "coordinate_systems": [
        {
            "axes": [
                {
                    "axis_type": None,
                    "axis_unit": "pixel/voxel",
                    "name": "logical coordinates x axis",
                },
                {
                    "axis_type": None,
                    "axis_unit": "pixel/voxel",
                    "name": "logical coordinates y axis",
                },
            ],
            "name": "base_logical_coordinates_2d",
        }
    ],
    "coordinate_transformations": None,
    "ctf_metadata": None,
    "height": 2000,
    "nominal_tilt_angle": 0.001,
    "path": "MotionCorr/job002/frames/TS_01_000_0_0.mrc",
    "section": 0,
    "width": 2000,
    "type": "projection",
}
MOCORR_40 = {
    "accumulated_dose": 123.0,
    "acquisition_order": None,
    "coordinate_systems": [
        {
            "axes": [
                {
                    "axis_type": None,
                    "axis_unit": "pixel/voxel",
                    "name": "logical coordinates x axis",
                },
                {
                    "axis_type": None,
                    "axis_unit": "pixel/voxel",
                    "name": "logical coordinates y axis",
                },
            ],
            "name": "base_logical_coordinates_2d",
        }
    ],
    "coordinate_transformations": None,
    "ctf_metadata": None,
    "height": 2000,
    "nominal_tilt_angle": 60.0006,
    "path": "MotionCorr/job002/frames/TS_01_040_60_0.mrc",
    "section": 40,
    "width": 2000,
    "type": "projection",
}

CTF_0 = {
    "accumulated_dose": 3.0,
    "coordinate_systems": [
        {
            "axes": [
                {
                    "axis_type": None,
                    "axis_unit": "pixel/voxel",
                    "name": "logical coordinates x axis",
                },
                {
                    "axis_type": None,
                    "axis_unit": "pixel/voxel",
                    "name": "logical coordinates y axis",
                },
            ],
            "name": "base_logical_coordinates_2d",
        },
        {
            "axes": [
                {
                    "axis_type": None,
                    "axis_unit": "Ångstrom",
                    "name": "physical coordinates x axis",
                },
                {
                    "axis_type": None,
                    "axis_unit": "Ångstrom",
                    "name": "physical coordinates y axis",
                },
            ],
            "name": "physical coordinates",
        },
    ],
    "coordinate_transformations": [
        {
            "input": "base_logical_coordinates_2d",
            "name": "image_pixel_size",
            "output": "image_pixel_size",
            "type": "scale",
        }
    ],
    "ctf_metadata": {
        "defocus_angle": 35.154533,
        "defocus_u": 38855.828125,
        "defocus_v": 38750.828125,
    },
    "height": 2000,
    "nominal_tilt_angle": 0.001,
    "path": "MotionCorr/job002/frames/TS_01_000_0_0.mrc",
    "section": 0,
    "width": 2000,
}
CTF_40 = {
    "accumulated_dose": 123.0,
    "coordinate_systems": [
        {
            "axes": [
                {
                    "axis_type": None,
                    "axis_unit": "pixel/voxel",
                    "name": "logical coordinates x axis",
                },
                {
                    "axis_type": None,
                    "axis_unit": "pixel/voxel",
                    "name": "logical coordinates y axis",
                },
            ],
            "name": "base_logical_coordinates_2d",
        },
        {
            "axes": [
                {
                    "axis_type": None,
                    "axis_unit": "Ångstrom",
                    "name": "physical coordinates x axis",
                },
                {
                    "axis_type": None,
                    "axis_unit": "Ångstrom",
                    "name": "physical coordinates y axis",
                },
            ],
            "name": "physical coordinates",
        },
    ],
    "coordinate_transformations": [
        {"input": "logical", "name": "Å/pix", "output": "physical", "type": "scale"}
    ],
    "ctf_metadata": {
        "defocus_angle": -10.13496,
        "defocus_u": 38544.476562,
        "defocus_v": 38449.148438,
    },
    "height": 2000,
    "nominal_tilt_angle": 60.0006,
    "path": "MotionCorr/job002/frames/TS_01_040_60_0.mrc",
    "section": 40,
    "width": 2000,
}
GAIN_FILE = {
    "width": 1000,
    "height": 1000,
    "coordinate_systems": [
        {
            "name": "base_logical_coordinates_2d",
            "axes": [
                {
                    "name": "logical coordinates x axis",
                    "axis_unit": "pixel/voxel",
                    "axis_type": None,
                },
                {
                    "name": "logical coordinates y axis",
                    "axis_unit": "pixel/voxel",
                    "axis_type": None,
                },
            ],
        },
    ],
    "coordinate_transformations": None,
    "path": "gain_reference.mrc",
}
