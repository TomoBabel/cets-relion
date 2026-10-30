from typing import Tuple
from cets_data_model.models.models import (
    Scale,
    CoordinateSystem,
)
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
