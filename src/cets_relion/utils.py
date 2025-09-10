import os
import re
from pathlib import Path
from typing import Dict, Union

from gemmi import cif
from scipy import spatial
import numpy as np


def clean_file_input(in_val: Union[str, os.PathLike]) -> str:
    return str(in_val)


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
        Path: pathlib.Path object for the job that produced the file relative to
            the project directory
    """
    fn = str(file)
    pattern = r"^job\d{3}$"
    splitname = fn.rstrip("/").split("/")[-1]
    if re.match(pattern, splitname):
        return Path(fn)
    parents = Path(fn).parents
    for parent in parents:
        if re.match(pattern, str(parent).split("/")[-1]):
            return Path(*parent.parts[-2:])
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


def relion_eulers_to_matrix(tilt: float, rot: float, psi: float) -> np.ndarray:
    """Convert the Euler angles from a RELION star file into a rotation matrix

    Args:
        tilt (float): _rlnAngleTilt (Phi)
        rot (float): _rlnAngleRot (Theta)
        psi (float): _rlnAnglePsi (Psi)

    Returns:
        np.ndarray: The transformation matrix

    """
    sipy_rot = spatial.transform.Rotation.from_euler(
        seq="ZYZ", angles=[tilt, rot, psi], degrees=True
    )
    return sipy_rot.as_matrix()
