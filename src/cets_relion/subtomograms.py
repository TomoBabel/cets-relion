from __future__ import annotations
from typing import Union
import os
from src.cets_relion.relion_reader import RelionPipeline
from pathlib import Path


class RelionSubTomosStarfile(object):
    """Class for handling a global subtomograms data file from RELION


    can be subclassed for job-specific variants of this type of file

    Many jobs create this type of file, this object should enable tracing back to the
    original tomograms and making the necessary objects
    """

    def __init__(
        self,
        file_name: Union[str, os.PathLike],
        pipeline: str = "default_pipeline.star",
    ) -> None:
        self.name = str(file_name)
        self.file = Path(str(file_name))
        self.pipeline = RelionPipeline(pipeline)

    def get_all_subtomos(self):
        pass
