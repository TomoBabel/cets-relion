from __future__ import annotations

import os
from pathlib import Path
from typing import Union, List

from gemmi import cif

from src.cets_relion.relion_reader import RelionPipeline
from src.models.models import SubProjectionImage


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

    def get_all_subtomos(self, ts_name: str) -> List[Path]:
        data_block = cif.read_file(self.name).find_block("particles")
        parts = data_block.find(prefix="_rln", tags=["TomoName", "ImageName"])
        return [Path(x[1]) for x in parts if x[0] == ts_name]

    def get_subtomo(self, subtomo_file: Union[str, os.PathLike]) -> SubProjectionImage:
        data_block = cif.read_file(self.name).find_block("particles")
        parts = data_block.find(
            prefix="_rln",
            tags=[
                "ImageName",
                "OpticsGroup",
                "TomoParticleName",
                "CenteredCoordinateXAngst",
                "CenteredCoordinateYAngst",
                "CenteredCoordinateZAngst",
            ],
        )
        file = [x for x in parts if x[0] == str(subtomo_file)]
        if not file:
            raise ValueError(f"{subtomo_file} not found")
        subtomo = list(file[0])
        subtomo_index = int(subtomo[2].split("/")[-1])

        # ToDo: Code for getting the pixel size for converting coords, this currently
        #  isn't being used in the SubProjectionImage but will be needed

        # optics_block = cif.read_file(self.name).find_block("optics")
        # px_size = optics_block.find(
        #     prefix="_rln", tags=["OpticsGroup", "ImagePixelSize"]
        # )
        # px_dic = {}
        # for line in px_size:
        #     px_dic[line[0]] = float(line[1])
        # x, y, z = [float(x) / px_dic[subtomo[1]] for x in subtomo[-3:]]
        # ToDo: Will this need to return a separate SubProjectionImage for each frame
        #  of the subtomogram?? Looks like yes, wait in implementing this until the
        #  data model is hashed out.
        return SubProjectionImage(particle_index=subtomo_index, path=str(subtomo_file))
