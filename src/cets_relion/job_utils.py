import os
import re
from pathlib import Path
from typing import Dict, Union
from gemmi import cif


def joboptions_from_job(
    job_name: Union[str, os.PathLike],
) -> Dict[str, str]:
    job_name = Path(job_name)
    jobstar = str(job_name / "job.star")
    jobop_block = cif.read_file(jobstar).find_block("joboptions_values")
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


def get_job_type(job_name: str) -> str:
    """Get the RELION/pipeliner type of a job

    Args:
        job_name (str): name of the job

    Returns:
        str: RELION/pipeliner jobtype
    """
    jobstar = Path(job_name) / "job.star"
    jt_block = cif.read_file(str(jobstar)).find_block("job")
    job_type = jt_block.find_pair("_rlnJobTypeLabel")
    return cif.as_string(job_type[1])


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
