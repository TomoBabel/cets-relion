import os
from pathlib import Path
from typing import Union, Tuple, List, Optional

from cets_data_model.models.models import (
    PointSet3D,
    ConfiguredBaseModel,
    ParticleMap,
    Affine,
    Translation,
    Scale,
    Sequence,
)
from cets_data_model.utils.image_utils import get_mrc_dims
from gemmi import cif


from cets_relion.relion_to_cets.relion_reader import RelionPipeline
from cets_relion.math_utils import relion_eulers_to_matrix
from cets_relion.job_utils import joboptions_from_job
from tmp_transformations import (
    BASE_LOGICAL_COORDS_3D,
    logical_coords,
    physical_coords,
)
from cets_relion.relion_to_cets.transformation_names import (
    IMAGE_PIXEL_SIZE_COORDS,
    ALIGN_SUBTOMOGRAM_COORDS,
    ALIGN_SUBTOMOGRAM_XFROM,
)


# ToDo: This class will probably be superseded by CETS objects in cets_data_model
class Sphere(object):
    """A sphere this is a temp annotation object until a CETS Sphere model is available"""

    def __init__(self, origin: Tuple[float, float, float], radius: float):
        self.origin = origin
        self.radius = radius


class RelionAnnotationFile(object):
    """Superclass for handling starfiles in the RELION annotations dir

    Attributes:
        name (str): str of the path to the annotation file
        file (Path): Path object for the annotation file
        data (List[object]): CETS objects for the annotations

    """

    def __init__(self, in_file: Union[str, os.PathLike]) -> None:
        """Instantiate a Relion Annotation File

        Args:
            in_file (Union[str, os.PathLike]): Path to the starfile
        """
        self.name = str(in_file)
        self.file = Path(self.name)

    def get_cets(self) -> List[ConfiguredBaseModel]:
        """Get a list of CETS annotation objects - must be implemented in subclasses"""
        raise NotImplementedError("Needs to be implemented in subclass")


class RelionSphereAnnotations(RelionAnnotationFile):
    """A class to hold RELION sphere annotation files for a single tomogram"""

    def __init__(self, in_file: Union[str, os.PathLike]) -> None:
        """Instantiate a Relion Sphere Annotation File

        Args:
            in_file (Union[str, os.PathLike]): Path to the starfile
        """
        super().__init__(in_file)

    def get_cets(self) -> list:
        # get the tomo name from the data rather than file name for robustness
        data = (
            cif.read_file(self.name)
            .sole_block()
            .find(
                prefix="_rln",
                tags=[
                    "TomoName",
                    "CoordinateX",
                    "CoordinateY",
                    "CoordinateZ",
                    "SphereRadius",
                ],
            )
        )
        if len(set([x[0] for x in list(data)])) != 1:
            raise ValueError(
                "Invalid sphere annotation file; should have exactly one name"
            )
        spheres: List[Sphere] = []
        for line in data:
            spheres.append(
                Sphere(
                    origin=(float(line[1]), float(line[2]), float(line[3])),
                    radius=line[4],
                ),
            )
        return spheres


class RelionCoordsStarFile(object):
    """A class to hold RELION particle coordinates

    RELION makes two 'particles.star' files one which has only coordinates with
    associated annotations and a 2nd with actual extracted particles.  This one is for
    only coords.

    Attributes:
        name (str): String with the path to the starfile relative to the project
        file (Path): Path for the starfile
    """

    def __init__(self, in_file: Union[str, os.PathLike]) -> None:
        """Instantiate the relion particle coordinates file.
        Args:
            in_file (Union[str, os.PathLike]): Path to the starfile
        """
        self.name = str(in_file)
        self.file = Path(str(in_file))

    def get_tomo_cets_coords_set(self, tomo_name: str) -> PointSet3D:
        """Get a CETS object for the picked coordinates associated with a tomogram

        Args:
            tomo_name (str): The name of the tomogram

        Returns:
            PointSet3D: A PointSet3D object that contains the coordinates
        """
        data = cif.read_file(self.name).find_block("particles")
        parts = data.find(
            prefix="_rln",
            tags=[
                "TomoName",
                "CenteredCoordinateXAngst",
                "CenteredCoordinateYAngst",
                "CenteredCoordinateZAngst",
            ],
        )
        coords = []
        for part in parts:
            if part[0] == tomo_name:
                coords.append([float(x) for x in [part[1], part[2], part[3]]])
        return PointSet3D(
            origin3D=coords,
            coordinate_systems=[physical_coords(name="image_pixel_size", dim=3)],
            path=self.name,
        )

    def determine_annotation_type(self):
        """Determine the type of annotation in annotation file
        Args:
            annotation_file (Union[str,os.PathLike]): The file
        Returns:
            str: The type of annotation
        """
        jobops = joboptions_from_job(self.file.parent)
        return jobops.get("pick_mode")

    def get_secondary_annotations(
        self, tomo_name: str
    ) -> Optional[RelionAnnotationFile]:
        """Get the annotations for a particular tomo
        Args:
            tomo_name (str): The name of the tomo
        Returns:
            List[Union[Point, Sphere]]: The annotations
        """
        annotype = self.determine_annotation_type()
        if annotype is None or annotype == "particles":
            return None
        annofile = self.file.parent / f"annotations/{tomo_name}_{annotype}.star"
        if annotype == "spheres":
            return RelionSphereAnnotations(annofile)
        else:
            raise NotImplementedError(f"Can't handle this annotation type: {annotype}")

    def get_all_tomo_names(self):
        data = (
            cif.read_file(self.name).sole_block().find(prefix="_rln", tags=["TomoName"])
        )
        return sorted(list(set([cif.as_string(x[0]) for x in data])))


class RelionParticlesStarFile(object):
    """A class for holding a RELION particle star file containing extracted particles

    Not just coordinates, should also have optics data and alignments
    """

    def __init__(self, file_name: str) -> None:
        """Instantiate a RELION particle star file.

        Args:
            file_name (str): Path to the starfile
        """
        self.file = Path(str(file_name))
        self.name = str(file_name)

    def get_cets_particles(self, tomo_name: str = "") -> List[ParticleMap]:
        """Get CETS ParticleMap objects for extracted particles

        Args:
            tomo_name (str): The name of the tomo

        Returns:
            List[ParticleMap]: CETS ParticleMap object for each particle
        """

        data = cif.read_file(self.name)
        optics_block = data.find_block("optics")
        optics_data = optics_block.find(
            prefix="_rln", tags=["OpticsGroup", "ImagePixelSize"]
        )
        optics_dict = {x[0]: x[1] for x in optics_data}
        parts_block = data.find_block("particles")
        all_parts = parts_block.find(
            prefix="_rln",
            tags=[
                "TomoName",
                "TomoSubtomogramRot",
                "TomoSubtomogramTilt",
                "TomoSubtomogramPsi",
                "AngleRot",
                "AngleTilt",
                "AnglePsi",
                "OriginXAngst",
                "OriginYAngst",
                "OriginZAngst",
                "TomoParticleName",
                "ImageName",
                "OpticsGroup",
            ],
        )
        parts = [x for x in all_parts if x[0] == tomo_name] if tomo_name else all_parts
        cets_particles = []
        for part in parts:
            tomorot, tomotilt, tomopsi = float(part[1]), float(part[2]), float(part[3])
            tilt, rot, psi = float(part[4]), float(part[5]), float(part[6])
            x, y, z = (float(part[7]), float(part[8]), float(part[9]))
            image_number = int(part[10].split("/")[-1])
            image_name = f"{image_number:06}@{part[11]}"
            apix = float(optics_dict[part[12]])

            # add scale transformation for logical coords
            scale_xform = Scale(
                name="Å/pix",
                input=BASE_LOGICAL_COORDS_3D,
                output=IMAGE_PIXEL_SIZE_COORDS,
                scale=[apix],
            )

            subtomo_affine = Affine(
                name="Alignment relative to parent tomogram",
                affine=list(relion_eulers_to_matrix(tomotilt, tomorot, tomopsi)),
                input=IMAGE_PIXEL_SIZE_COORDS,
                output="Alignment relative to parent tomogram",
            )
            subtomo_coordsys = physical_coords(
                name="Alignment relative to parent tomogram", dim=3
            )

            align_translate = Translation(
                name="Averaging translation",
                translation=[x / apix, y / apix, z / apix],
                input="Alignment relative to parent tomogram",
                output="Averaging translation",
            )
            align_trans_coord_sys = logical_coords(name="Averaging translation")

            align_affine = Affine(
                name="Averaging alignment",
                affine=list(relion_eulers_to_matrix(tilt, rot, psi)),
                input="Averaging translation",
            )
            final_alignment = Sequence(
                sequence=[subtomo_affine, align_translate, align_affine],
                input=IMAGE_PIXEL_SIZE_COORDS,
                output=ALIGN_SUBTOMOGRAM_COORDS,
                name=ALIGN_SUBTOMOGRAM_XFROM,
            )
            final_coords = physical_coords(dim=3, name=ALIGN_SUBTOMOGRAM_COORDS)

            dims = get_mrc_dims(part[4])
            cets_part = ParticleMap(
                path=image_name,
                width=dims[0],
                height=dims[1],
                depth=dims[2],
                coordinate_systems=[
                    logical_coords(dim=3),
                    physical_coords(name=IMAGE_PIXEL_SIZE_COORDS, dim=3),
                    subtomo_coordsys,
                    align_trans_coord_sys,
                    final_coords,
                ],
                coordinate_transformations=[
                    scale_xform,
                    final_alignment,
                ],
            )
            cets_particles.append(cets_part)
        return cets_particles

    def get_coords_object(self) -> List[RelionCoordsStarFile]:
        """Get the data for the original picking of the particles

        Returns:
            List[RelionParticlesStarFile]: RelionParticlesStarFile object
        """
        pipeline = RelionPipeline("default_pipeline.star")
        pick_jobs = pipeline.next_upstream_jobs(self.name, jobtypes=["relion.picktomo"])
        return [RelionCoordsStarFile(Path(x) / "particles.star") for x in pick_jobs]

    def get_all_tomo_names(self):
        data = (
            cif.read_file(self.name)
            .find_block("particles")
            .find(prefix="_rln", tags=["TomoName"])
        )
        return sorted(list(set([cif.as_string(x[0]) for x in data])))


def parse_particles_file(
    in_file: str,
) -> Tuple[str, Union[RelionParticlesStarFile, RelionCoordsStarFile]]:
    """Parse a RELION particle star file and return the right object

    Figure out if it's actual particles or just coords

    Args:
        in_file (str): The file to parse
    Returns:
        Tuple[str, Union[RelionParticlesStarFile, RelionCoordsStarFile]]: (the type,
           (picks or particles), correct object for it (ReliionCoordsStarFile or
           RelionParticlesStarFile))
    """
    data = cif.read_file(in_file)
    # if the file contains extracted particles it wil have an optics block
    optics = data.find_block("optics")
    if optics is None:
        return "picks", RelionCoordsStarFile(in_file)
    else:
        return "particles", RelionParticlesStarFile(in_file)
