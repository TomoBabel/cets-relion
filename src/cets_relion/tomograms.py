from __future__ import annotations

import os
from pathlib import Path
from typing import Tuple, Optional, Union

from gemmi import cif

from cets_relion.relion_reader import RelionPipeline
from cets_data_model.models.models import Tomogram


class RelionTomosStarfile(object):
    """Class for handling a global tomgrams data file from RELION

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

    def get_reconstructed_tomo(self, tomogram_name: str) -> Optional[Tuple[str, bool]]:
        """Get the full reconstructed tomogram file for a tomo

        Relion may only generate full tomograms from denoise jobs, Reconstruct and
        Denoise Train jobs cans also generate half set tomos used for denoising.  If
        only the half tomos are present, half1 is returned.

        Args:
            tomogram_name (str): Name of the tomogram to find

        Returns:
            Optional[Tuple[str, bool]]: (tomo file name, True if is  full reconstructed
            tomo, False if it is a half). None if the tomo name was not found.
        """

        # see of this job produced the reconstructed tomo
        cifdata = cif.read_file(self.name).find_block("global")
        tomos = cifdata.find(
            prefix="_rln", tags=["TomoName", "TomoReconstructedTomogramDenoised"]
        )
        if tomos:
            tomo_dict = dict(list(tomos))
            tomo = tomo_dict.get(tomogram_name)
            if tomo:
                return tomo, True
            else:
                return None

        # if this job didn't create denoised tomos return the half tomo 1
        tomos = cifdata.find(
            prefix="_rln", tags=["TomoName", "TomoReconstructedTomogramHalf1"]
        )
        if tomos:
            tomo_dict = dict(list(tomos))
            tomo = tomo_dict.get(tomogram_name)
            if tomo:
                return tomo, False
            else:
                return None
        else:
            return None

    def get_cets_tomo(self, tomogram_name: str) -> Optional[Tomogram]:
        """Get a CETS Tomogram object for a specific tomogram

        Args:
            tomogram_name (str): Name of the tomogram to make the obj for

        Returns:
            Optional[TomoGram]: The CETS Tomogram object, or None if not found
        """
        tomo = self.get_reconstructed_tomo(tomogram_name)
        if not tomo:
            return None
        cifdata = cif.read_file(self.name).find_block("global")
        dimdata = cifdata.find(
            prefix="_rln", tags=["TomoName", "TomoSizeX", "TomoSizeY", "TomoSizeZ"]
        )
        dims = []
        for line in dimdata:
            if line[0] == tomogram_name:
                dims = [int(x) for x in line[1:]]
                break
        if not dims:
            raise ValueError("Couldn't get tomogram dimensions")

        return Tomogram(path=tomo[0], height=dims[1], width=dims[0], depth=dims[2])
