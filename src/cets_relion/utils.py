from typing import Tuple
import mrcfile
import tifffile


def get_mrc_dims(in_mrc: str) -> Tuple[int, int, int]:
    """Get the shape of a mrc file

    Args:
        in_mrc (str): The name of the file
    Returns:
        tuple: (int,int,int) x,y,z size in pixels

    """
    with mrcfile.open(in_mrc, header_only=True) as mrc:
        return int(mrc.header.nx), int(mrc.header.ny), int(mrc.header.nz)


def get_tiff_dims(in_tiff: str) -> Tuple[int, int, int]:
    """Get the shape of a tiff file

    Args:
        in_tiff (str): The name of the file
    Returns:
        tuple: (int,int,int) x,y,z size in pixels

    """
    with tifffile.TiffFile(in_tiff) as tif:
        page = tif.pages[0]
        height, width = page.shape
        return width, height, len(tif.pages)


def get_image_dims(in_img: str) -> Tuple[int, int, int]:
    """Get the shape of an image file, automatically determines if it's mrc or tiff

    Args:
        in_img (str): The name of the file
    Returns:
        tuple: (int,int,int) x,y,z size in pixels
    Raises:
        ValueError: If the image isn't a valid mrc or tiff
    """
    try:
        return get_mrc_dims(in_img)
    except Exception:
        try:
            return get_tiff_dims(in_img)
        except Exception:
            raise ValueError("File is not valid mrc or tiff format")
