import os
from typing import Union, Tuple, List
from gemmi import cif
from pathlib import Path
from cets_relion.objs.coordinate_systems import RELION_COORDS_PHYSICAL
from cets_data_model.models.models import (
    PointSet3D,
    ConfiguredBaseModel,
    ParticleMap,
    Affine,
    Translation,
)
from cets_data_model.utils.image_utils import get_mrc_dims

from cets_relion.relion_reader import RelionPipeline
from cets_relion.utils import (
    get_job_name,
    relion_eulers_to_matrix,
)


# ToDo: These classes will probably be superseded by CETS objects in cets_data_model
class Sphere(object):
    """A sphere this is a temp annotation object until a CETS Sphere model is available"""

    def __init__(self, origin: Tuple[float, float, float], radius: float):
        self.origin = origin
        self.radius = radius


class RelionAnnotationFile(object):
    """Superclass for handling starfiles in the RELION annotations dir"""

    def __init__(self, in_file: Union[str, os.PathLike]) -> None:
        self.name = str(in_file)

    def get_cets(self) -> List[ConfiguredBaseModel]:
        """Get a list of CETS annotation objects - must be implemented in subclasses"""
        raise NotImplementedError("Needs to be implemented in subclass")


class RelionSphereAnnotations(RelionAnnotationFile):
    """A class to hold RELION sphere annotation files"""

    def __init__(self, in_file: Union[str, os.PathLike]) -> None:
        super().__init__(in_file)

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
        self.tomo_name = data[0][0]
        self.spheres: List[Sphere] = []
        for line in data:
            self.spheres.append(
                Sphere(
                    origin=(float(line[1]), float(line[2]), float(line[3])),
                    radius=line[4],
                ),
            )

    def get_cets(self) -> List[ConfiguredBaseModel]:
        # ToDo: Need a CETS model for spheres
        return []


class RelionPointAnnotations(RelionAnnotationFile):
    """A class to hold RELION point annotation files"""

    def __init__(self, in_file: Union[str, os.PathLike]):
        super().__init__(in_file)

    def get_cets(self) -> List[ConfiguredBaseModel]:
        data = (
            cif.read_file(self.name)
            .sole_block()
            .find(
                prefix="_rln",
                tags=["CoordinateX", "CoordinateY", "CoordinateZ"],
            )
        )
        coords = [[float(x[0]), float(x[1]), float(x[2])] for x in data]
        return [
            PointSet3D(origin3D=coords, coordinate_systems=[RELION_COORDS_PHYSICAL])
        ]


class RelionCoordsStarFile(object):
    """A class to hold RELION particle coordinates

    RELION makes two 'particles.star' files one which has only coordinates with
    associated annotations and a 2nd with actual extracted particles.  This one is for
    only coords.

    """

    def __init__(self, in_file: Union[str, os.PathLike]) -> None:
        """Initialize the relion particle coordinates file."""
        self.name = str(in_file)
        job = get_job_name(self.name)
        annotations = job.glob("annotations/*.star")

        # parse the names of the annotation files
        self.annotation_files = {}
        for f in annotations:
            fnsplit = str(f).split("_")
            tomoname = str(f.name).rstrip(f"_{fnsplit[-1]}")
            self.annotation_files[tomoname] = f

    def get_tomo_cets_particle_set(self, tomo_name: str) -> PointSet3D:
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
            origin3D=coords, coordinate_systems=[RELION_COORDS_PHYSICAL], path=self.name
        )

    @staticmethod
    def determine_annotation_type(annotation_file: Union[str, os.PathLike]):
        """Determine the type of annotation in annotation file
        Args:
            annotation_file (Union[str,os.PathLike]): The file
        Returns:
            str: The type of annotation
        """
        print(cif.read_file(str(annotation_file)).sole_block())
        data = (
            cif.read_file(str(annotation_file))
            .sole_block()
            .find(prefix="_rln", tags=["TomoName"])
        )
        tags = data.loop.tags
        if len(tags) == 4:
            return "points"
        elif "_rlnSphereRadius" in tags:
            return "spheres"
        else:
            # ToDo: find out what the other annotation file formats are and return names
            #  for them.
            return "other"

    def get_secondary_annotations(self, tomo_name: str) -> List[Sphere]:
        """Get the annotations for a particular tomo
        Args:
            tomo_name (str): The name of the tomo
        Returns:
            List[Union[Point, Sphere]]: The annotations
        """
        anno_file = self.annotation_files.get(tomo_name)
        annotations = []
        if anno_file is not None:
            annotype = self.determine_annotation_type(str(anno_file))
            if annotype == "points":
                pass
            if annotype == "spheres":
                annotations = RelionSphereAnnotations(anno_file).spheres
            else:
                annotations = []  # ToDo: add other annotation types here
        return annotations


class RelionParticlesStarFile(object):
    """A class for holding a RELION particle star file containing extracted particles

    Not just coordinates, should also have optics data and alignments
    """

    def __init__(self, file_name: str):
        self.file = Path(str(file_name))
        self.name = str(file_name)

    def get_cets_particles(self, tomo_name: str) -> List[ParticleMap]:
        """Get CETS ParticleMap objects for extracted particles

        Args:
            tomo_name (str): The name of the tomo

        Returns:
            List[ParticleMap]: CETS ParticleMap object for each particle
        """
        data = cif.read_file(self.name)
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
            ],
        )
        parts = [x for x in all_parts if x[0] == tomo_name]
        cets_particles = []
        for part in parts:
            tomorot, tomotilt, tomopsi = float(part[1]), float(part[2]), float(part[3])
            tilt, rot, psi = float(part[4]), float(part[5]), float(part[6])
            x, y, z = (float(part[7]), float(part[8]), float(part[9]))
            image_number = int(part[10].split("/")[-1])
            image_name = f"{image_number:06}@{part[11]}"
            align_affine = Affine(
                name="Averaging alignment",
                affine=list(relion_eulers_to_matrix(tilt, rot, psi)),
            )
            align_translate = Translation(
                name="Averaging translation",
                translation=[x, y, z],
            )
            subtomo_affine = Affine(
                name="Alignment relative to parent tomogram",
                affine=list(relion_eulers_to_matrix(tomotilt, tomorot, tomopsi)),
            )
            dims = get_mrc_dims(part[4])
            cets_part = ParticleMap(
                path=image_name,
                width=dims[0],
                height=dims[1],
                depth=dims[2],
                coordinate_systems=[RELION_COORDS_PHYSICAL],
                coordinate_transformations=[
                    subtomo_affine,
                    align_affine,
                    align_translate,
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


def parse_particles_file(
    in_file: str,
) -> Tuple[str, Union[RelionParticlesStarFile, RelionCoordsStarFile]]:
    """Parse a RELION particle star file and return the right object

    figure out if it's actual particles or just coords

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
