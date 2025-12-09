from typing import Tuple, Optional
from cets_data_model.models.models import (
    Scale,
    CoordinateSystem,
    Axis,
    TransformationType,
    CoordinateTransformation,
)
from pydantic import Field, conlist

# Standard coordinate system and transformation names - The transformation or sequence
# of transformations that accomplish these tasks must have these specific names and
# the endpoint coordinate system must have the associated name.

# The actual transformation/sequence and coordinate system can vary as long as the
# correct string from below is used in the `name` field.

# Axis definitions
x_axis_logical = Axis(name="logical coordinates x axis", axis_unit="pixel/voxel")
y_axis_logical = Axis(name="logical coordinates y axis", axis_unit="pixel/voxel")
z_axis_logical = Axis(name="logical coordinates z axis", axis_unit="pixel/voxel")

x_axis_physical = Axis(name="physical coordinates x axis", axis_unit="Ångstrom")
y_axis_physical = Axis(name="physical coordinates y axis", axis_unit="Ångstrom")
z_axis_physical = Axis(name="physical coordinates z axis", axis_unit="Ångstrom")

# NAMES - for the globals coordinate systems always end with COORDS, transformations
# always end with XFORM

# basic logical coords
BASE_LOGICAL_COORDS_2D = "base_logical_coordinates_2d"
BASE_LOGICAL_COORDS_3D = "base_logical_coordinates_3d"


# Align calibration image to movie frame
ALIGN_CALIBRATION_IMAGE_XFROM = "align_calibration_image_to_movie_frame"
ALIGN_CALIBRATION_IMAGE_COORDS = "aligned_calibration_image"

# Align movie frame to projection
ALIGN_MOVIE_FRAME_XFROM = "align_movie_frame_to_projection"
ALIGN_MOVIE_FRAME_COORDS = "aligned_movie_frame"

# Align projection image to tomogram
ALIGN_PROJECTION_IMAGE_XFROM = "align_projection_image_to_tomogram"
ALIGN_PROJECTION_IMAGE_COORDS = "aligned_projection_image"

# Align subtomogram to tomogram R3D
ALIGN_SUBTOMOGRAM_XFROM = "align_subtomogram_to_tomogram"
ALIGN_SUBTOMOGRAM_COORDS = "aligned_subtomogram"

# Align map to tomogram
ALIGN_MAP_XFROM = "align_map_to_tomogram"
ALIGN_MAP_COORDS = "aligned_map"

# Align annotation to tomogram
ALIGN_ANNOTATION_XFROM = "align_annotation_to_tomogram"
ALIGN_ANNOTATION_COORDS = "aligned_annotation"

# set pixel size of image
IMAGE_PIXEL_SIZE_XFROM = "image_pixel_size"
IMAGE_PIXEL_SIZE_COORDS = "image_pixel_size"

# set super res pixel size of image
IMAGE_SUPER_RES_PIXEL_SIZE_XFROM = "image_pixel_size"
IMAGE_SUPER_RES_PIXEL_SIZE_COORDS = "image_pixel_size"

# Helper functions


def physical_coords(name: str, dim: int) -> CoordinateSystem:
    """Generate physical coordinates object"""
    axes = [x_axis_physical, y_axis_physical]
    name = name
    if dim == 3:
        axes.append(z_axis_physical)
    elif dim not in (2, 3):
        raise ValueError(f"{dim} is not a valid dimension")
    return CoordinateSystem(name=name, axes=axes)


def logical_coords(name: Optional[str] = None, dim: int = 2) -> CoordinateSystem:
    """Generate physical coordinates object

    Gives the base logical coordinates if no name specified
    """
    name = BASE_LOGICAL_COORDS_2D if name is None else name
    axes = [x_axis_logical, y_axis_logical]
    if dim == 3:
        name = BASE_LOGICAL_COORDS_3D
        axes.append(z_axis_logical)
    elif dim not in (2, 3):
        raise ValueError(f"{dim} is not a valid dimension")
    return CoordinateSystem(name=name, axes=axes)


# helper functions for generating transformations and their associated coordinate
# systems with the correct naming conventions. Each one returns the transformation
# and the final coordinate system.

# helper functions for scaling - just provide pixel size


def image_pixel_size(apix: float) -> Tuple[Scale, CoordinateSystem]:
    """Get the scale transformation obj and final coord system for image pixel size"""
    return (
        Scale(
            type="scale",
            name=IMAGE_PIXEL_SIZE_XFROM,
            input=BASE_LOGICAL_COORDS_2D,
            output=IMAGE_PIXEL_SIZE_COORDS,
            scale=[apix, apix],
        ),
        physical_coords(name=IMAGE_PIXEL_SIZE_COORDS, dim=2),
    )


def image_super_res_pixel_size(apix: float) -> Tuple[Scale, CoordinateSystem]:
    """Get the scale transformation obj and final coord system for superres image pixel
    size"""
    return (
        Scale(
            type="scale",
            name=IMAGE_SUPER_RES_PIXEL_SIZE_XFROM,
            input=BASE_LOGICAL_COORDS_2D,
            output=IMAGE_SUPER_RES_PIXEL_SIZE_COORDS,
            scale=[apix, apix],
        ),
        physical_coords(name=IMAGE_SUPER_RES_PIXEL_SIZE_COORDS, dim=2),
    )


class Rotation2D(CoordinateTransformation):
    """
    A 2D rotation transformation
    """

    rotation2d: Optional[
        conlist(
            min_length=2,
            max_length=2,
            item_type=conlist(min_length=2, max_length=2, item_type=float),
        )
    ] = Field(default=None, description="""The rotation matrix""")
    type: Optional[TransformationType] = Field(
        default="affine", description="""The type of transformation."""
    )
    name: Optional[str] = Field(
        default=None, description="""The name of the coordinate transformation"""
    )
    input: Optional[str] = Field(
        default=None, description="""The source coordinate system name"""
    )
    output: Optional[str] = Field(
        default=None, description="""The target coordinate system name"""
    )


class Flip2D(CoordinateTransformation):
    """
    A 2D flip transformation
    """

    flip2d: Optional[
        conlist(
            min_length=2,
            max_length=2,
            item_type=conlist(min_length=2, max_length=2, item_type=int),
        )
    ] = Field(default=None, description="""The flip matrix""")
    type: Optional[TransformationType] = Field(
        default="affine", description="""The type of transformation."""
    )
    name: Optional[str] = Field(
        default=None, description="""The name of the coordinate transformation"""
    )
    input: Optional[str] = Field(
        default=None, description="""The source coordinate system name"""
    )
    output: Optional[str] = Field(
        default=None, description="""The target coordinate system name"""
    )
