import os
from typing import Dict, Union, Tuple, List
from gemmi import cif
from cets_relion.objs.coordinate_systems import RELION_COORDS_PHYSICAL
from cets_data_model.models.models import PointSet3D, ConfiguredBaseModel
from cets_relion.utils import get_job_name


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


class RelionParticleCoordsFile(object):
    """A class to hold RELION particle coordinates."""

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

    def all_particle_sets(self) -> Dict[str, PointSet3D]:
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
        tomo_coords: Dict[str, List[List[float]]] = {}
        # get all particles for each tomo
        for part in parts:
            coords = [float(x) for x in (part[1], part[2], part[3])]
            if tomo_coords.get(part[0]) is None:
                tomo_coords[part[0]] = [coords]
            else:
                tomo_coords[part[0]].append(coords)
        # make PointSet3D objs for each tomo
        tomo_sets = {}
        for tomo in tomo_coords:
            tomo_sets[tomo] = PointSet3D(
                origin3D=tomo_coords[tomo],
                coordinate_systems=[RELION_COORDS_PHYSICAL],
                path=self.name,
            )
        return tomo_sets

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
