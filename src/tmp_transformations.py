from typing import Tuple, Optional
from cets_data_model.models.models import (
    Scale,
    CoordinateSystem,
    TransformationType,
    CoordinateTransformation,
)
from pydantic import Field, conlist
from cets_relion.transformation_names import (
    IMAGE_PIXEL_SIZE_XFROM,
    IMAGE_PIXEL_SIZE_COORDS,
)
from cets_relion.transformation_names import BASE_LOGICAL_COORDS_2D
from cets_data_model.utils.coordinate_systems import physical_coords


def image_pixel_size(apix: float) -> Tuple[Scale, CoordinateSystem]:
    """Get the scale transformation obj and final coord system for image pixel size"""
    return (
        Scale(
            name=IMAGE_PIXEL_SIZE_XFROM,
            input=BASE_LOGICAL_COORDS_2D,
            output=IMAGE_PIXEL_SIZE_COORDS,
            scale=[apix, apix],
        ),
        physical_coords(name=IMAGE_PIXEL_SIZE_COORDS, dim=2),
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
