import os
import re
from pathlib import Path
from typing import Tuple, Dict, Union

import mrcfile
import tifffile
from gemmi import cif


def get_mrc_dims(in_mrc: Union[str, os.PathLike]) -> Tuple[int, int, int]:
    """Get the shape of a mrc file

    Args:
        in_mrc (str): The name of the file
    Returns:
        tuple: (int,int,int) x,y,z size in pixels

    """
    with mrcfile.open(in_mrc, header_only=True) as mrc:
        return int(mrc.header.nx), int(mrc.header.ny), int(mrc.header.nz)


def get_tiff_dims(in_tiff: Union[str, os.PathLike]) -> Tuple[int, int, int]:
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


def get_image_dims(in_img: Union[str, os.PathLike]) -> Tuple[int, int, int]:
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


def joboptions_from_jobstar_file(
    jobstar_file: Union[str, os.PathLike],
) -> Dict[str, str]:
    jobop_block = cif.read_file(str(jobstar_file)).find_block("joboptions_values")
    jobops_dict = dict(
        list(
            jobop_block.find(
                prefix="_rln", tags=["JobOptionVariable", "JobOptionValue"]
            )
        )
    )
    for key, val in jobops_dict.items():
        jobops_dict[key] = "" if val in ["''", '""'] else val
    return jobops_dict


def get_job_name(file: Union[str, os.PathLike]) -> Path:
    """Given a file get the Path for the RELION job the produced it

    Args:
        file (str): Name for the file

    Returns:
        Path: pathlib.Path object for the job that produced the file
    """
    fn = str(file)
    pattern = r"^job\d{3}$"
    splitname = fn.rstrip("/").split("/")[-1]
    print(splitname, "****")
    if re.match(pattern, splitname):
        return Path(fn)
    parents = Path(fn).parents
    for parent in parents:
        if re.match(pattern, str(parent).split("/")[-1]):
            return parent
    raise ValueError(f" {fn} does not contain a valid RELION job path")


def get_job_number(file: Union[str, os.PathLike]) -> int:
    """Get number of the job that produced a file or from the full job name

    Args:
        file (Union[str, os.PathLike): Path to the file/job dir

    Returns:
        int: The job number
    """
    jobname = get_job_name(file).name
    return int(jobname.lstrip("job"))
