from __future__ import annotations

import os
from pathlib import Path
from typing import Optional, Union

from cets_data_model.models.models import Tomogram
from gemmi import cif

from tmp_transformations import logical_coords


class RelionTomosStarfile(object):
    """Class for handling a global tomgrams data file from RELION

    can be subclassed for job-specific variants of this type of file

    Many jobs create this type of file, this object should enable tracing back to the
    original tomograms and making the necessary objects
    """

    def __init__(
        self,
        file_name: Union[str, os.PathLike],
    ) -> None:
        """Instantiate a RelionTomosStarfile object
        Args:
            file_name (Union[str, os.PathLike]): path to tomograms data file

        """
        self.name = str(file_name)
        self.file = Path(str(file_name))

    def get_reconstructed_tomo(self, tomogram_name: str) -> Optional[str]:
        """Get the full reconstructed tomogram mrc file for a tomo

        Relion will only generate full tomograms from denoise jobs, Reconstruct and
        Denoise Train jobs only generate half set tomos used for denoising and will
        return None

        Args:
            tomogram_name (str): Name of the tomogram to find

        Returns:
            Optional[str]: Path of the full reconstructed tomogram file or None
        """

        # see of this job produced the reconstructed tomo
        cifdata = cif.read_file(self.name).find_block("global")
        tomo = cifdata.find(
            prefix="_rln", tags=["TomoName", "TomoReconstructedTomogramDenoised"]
        )
        if tomo:
            tomo_dict = dict(list(tomo))
            return tomo_dict.get(tomogram_name)
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
                dims = [int(line[1]), int(line[2]), int(line[3])]
                break
        if not dims:
            raise ValueError("Couldn't get tomogram dimensions")

        return Tomogram(
            id=tomogram_name,
            path=tomo,
            coordinate_systems=[logical_coords()],
            height=dims[1],
            width=dims[0],
            depth=dims[2],
        )

    def get_all_tomo_names(self):
        data = (
            cif.read_file(self.name)
            .find_block("global")
            .find(prefix="_rln", tags=["TomoName"])
        )
        return sorted([cif.as_string(x[0]) for x in data])
