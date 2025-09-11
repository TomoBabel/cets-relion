from __future__ import annotations

import os
from pathlib import Path
from typing import Union, Optional
from dataclasses import dataclass
from gemmi import cif

from cets_relion.relion_reader import RelionPipeline
from cets_data_model.models.models import (
    Affine,
    CoordinateSystem,
    CoordinateTransformation,
)
from cets_relion.objs.coordinate_systems import RELION_COORDS_PHYSICAL
from cets_relion.utils import relion_eulers_to_matrix
from cets_data_model.utils.image_utils import get_mrc_dims


# Temp subtomogram class that until SubTomogram is added to models
@dataclass
class SubTomogram:
    path: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    depth: Optional[int] = None
    coordinate_systems: Optional[list[CoordinateSystem]] = None
    coordinate_transformations: Optional[list[CoordinateTransformation]] = None


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

        data_block = cif.read_file(self.name).find_block("particles")
        subtomos = data_block.find(
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
        subtomos, formatted_subtomos = list(subtomos), []
        for i in subtomos:
            formatted_subtomos.append(
                [i[0], int(i[1]), i[2], float(i[3]), float(i[4]), float(i[5])]
            )
        self.subtomos = formatted_subtomos

        # check of the subtomos have orientation relative to the tomo
        # EG: if they were extracted from the surface of a sphere
        st_orient = data_block.find(
            prefix="_rln",
            tags=[
                "ImageName",
                "TomoSubtomogramRot",
                "TomoSubtomogramTilt",
                "TomoSubtomogramPsi",
            ],
        )
        self.subtomo_orientations = []
        if st_orient is not None:
            orients, formatted_orients = list(st_orient), []
            for i in orients:
                formatted_orients.append([i[0]] + [float(x) for x in list(i)[1:]])
            self.subtomo_orientations = formatted_orients

        # check if the subtomos have been aligned for a subtomogram average
        st_align = data_block.find(
            prefix="_rln", tags=["ImageName", "AngleTilt", "AngleRot", "AnglePsi"]
        )
        self.subtomo_alignments = []
        if st_align is not None:
            aligns, formatted_aligns = list(st_align), []
            for i in aligns:
                formatted_aligns.append([i[0]] + [float(x) for x in list(i)[1:]])
            self.subtomo_alignments = formatted_aligns

    def get_subtomo(self, subtomo_file: Union[str, os.PathLike]) -> SubTomogram:
        subtomos = [x for x in self.subtomos if x[0] == subtomo_file]
        orientations = [x for x in self.subtomo_orientations if x[0] == subtomo_file]
        alignments = [x for x in self.subtomo_alignments if x[0] == subtomo_file]

        if not subtomos:
            raise ValueError(f"{subtomo_file} not found")
        if len(subtomos) > 1:
            raise ValueError(f"Multiple subtomograms found for {subtomo_file}")
        if len(orientations) and len(orientations) != len(subtomos):
            raise ValueError("Number of orientations and subtomograms do not match")
        if len(alignments) and len(alignments) != len(subtomos):
            raise ValueError("Number of alignments and subtomograms do not match")

        orient = [] if orientations is None else orientations[0][1:]
        align = [] if alignments is None else alignments[0][1:]

        # ToDO: this needs to be a SubTomogram obj, which isn't in the models yet
        subtom_obj = SubTomogram(
            path=str(subtomo_file), coordinate_systems=[RELION_COORDS_PHYSICAL]
        )

        # add the orientation relative to the tomogram
        if orientations:
            orient_xform = Affine(
                name="subtomogram orientation",
                affine=list(relion_eulers_to_matrix(orient[0], orient[1], orient[2])),
            )
            if subtom_obj.coordinate_transformations is None:
                subtom_obj.coordinate_transformations = [orient_xform]
            else:
                subtom_obj.coordinate_transformations.append(orient_xform)
        # add any alignments
        if alignments:
            alignments_xform = Affine(
                name="subtomogram alignment",
                affine=list(relion_eulers_to_matrix(align[0], align[1], align[2])),
            )
            if subtom_obj.coordinate_transformations is None:
                subtom_obj.coordinate_transformations = [alignments_xform]
            else:
                subtom_obj.coordinate_transformations.append(alignments_xform)

        # get the dimensions
        try:
            dims = get_mrc_dims(subtomo_file)
        except Exception:
            dims = (None, None, None)
        subtom_obj.width, subtom_obj.height, subtom_obj.depth = dims
        # get the ctf info
        # need to look up the mics...
        # add parent tomogram
        # look up from the extraction job

        return subtom_obj
