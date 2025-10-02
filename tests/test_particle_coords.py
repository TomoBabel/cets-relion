from tests.testing_tools import CetsRelionTest
from cets_relion.particle_coords import (
    RelionCoordsStarFile,
    Sphere,
    RelionSphereAnnotations,
    RelionPointAnnotations,
    RelionParticlesStarFile,
)
from cets_relion.objs.coordinate_systems import RELION_COORDS_PHYSICAL
from cets_data_model.models.models import Translation, Axis, Affine, CoordinateSystem
from pathlib import Path
from pytest import fixture


class TestRelionParticleCoordsStarFile(CetsRelionTest):
    def test_instantiate_RelionParticleCoordsFile(self):
        self.setup_dirs(9)
        pcf = RelionCoordsStarFile("Picks/job009/particles.star")
        assert pcf.name == "Picks/job009/particles.star"
        self.assertEqual(
            pcf.annotation_files,
            {
                "TS_01": Path("Picks/job009/annotations/TS_01_spheres.star"),
                "TS_03": Path("Picks/job009/annotations/TS_03_spheres.star"),
                "TS_43": Path("Picks/job009/annotations/TS_43_spheres.star"),
                "TS_45": Path("Picks/job009/annotations/TS_45_spheres.star"),
                "TS_54": Path("Picks/job009/annotations/TS_54_spheres.star"),
            },
        )

    def test_get_parts_for_tomo(self):
        self.setup_dirs(9)
        pcf = RelionCoordsStarFile("Picks/job009/particles.star")
        parts = pcf.get_tomo_cets_particle_set("TS_01")
        self.assertEqual(parts.coordinate_systems, [RELION_COORDS_PHYSICAL])
        assert parts.path == pcf.name
        assert len(parts.origin3D) == 6981

    def test_get_annotation_file_type(self):
        self.setup_dirs(19)
        j9 = RelionCoordsStarFile("Picks/job009/particles.star")
        assert j9.determine_annotation_type(j9.annotation_files["TS_01"]) == "spheres"
        j19 = RelionCoordsStarFile("Picks/job019/particles.star")
        assert j19.determine_annotation_type(j19.annotation_files["TS_01"]) == "points"

    def test_get_secondary_annotations_points(self):
        # points have no secondary annotations
        self.setup_dirs(19)
        j9 = RelionCoordsStarFile("Picks/job019/particles.star")
        assert j9.get_secondary_annotations("TS_01") == []

    def test_get_secondary_annotations_spheres(self):
        # points have no secondary annotations
        self.setup_dirs(9)
        j9 = RelionCoordsStarFile("Picks/job009/particles.star")
        annotations = j9.get_secondary_annotations("TS_01")
        assert len(annotations) == 9
        assert all([isinstance(x, Sphere) for x in annotations])


class RelionAnnotationFilesTest(CetsRelionTest):
    def test_instantiate_RelionSphereAnnotations(self):
        f = "skeleton_project/Picks/job009/annotations/TS_01_spheres.star"
        sphere_file = RelionSphereAnnotations(self.test_data / f)
        assert sphere_file.tomo_name == "TS_01"
        assert len(sphere_file.spheres) == 9
        assert all([isinstance(x, Sphere) for x in sphere_file.spheres])

    # ToDo: Will need updating when CETS Sphere object is added
    def test_get_cets_from_sphere_annotations(self):
        f = "skeleton_project/Picks/job009/annotations/TS_01_spheres.star"
        sphere_file = RelionSphereAnnotations(self.test_data / f)
        assert sphere_file.get_cets() == []

    def test_instantiate_RelionPointsAnnotations(self):
        f = "skeleton_project/Picks/job019/annotations/TS_01_particles.star"
        points_file = RelionPointAnnotations(self.test_data / f)
        assert points_file.name == str(self.test_data / f)

    def test_get_cets_from_relion_point_annotations(self):
        f = "skeleton_project/Picks/job019/annotations/TS_01_particles.star"
        points_file = RelionPointAnnotations(self.test_data / f)
        cets = points_file.get_cets()
        assert len(cets) == 1
        assert len(cets[0].origin3D) == 1960


class TestRelionParticlesStarFile(CetsRelionTest):
    @fixture(autouse=True)
    def _mock_get_mrc_dims(self, monkeypatch):
        monkeypatch.setattr(
            "cets_relion.particle_coords.get_mrc_dims",
            lambda *args, **kwargs: (1, 2, 3),
        )

    @fixture(autouse=True)
    def _mock_matrix_from_euler(self, monkeypatch):
        monkeypatch.setattr(
            "cets_relion.particle_coords.relion_eulers_to_matrix",
            lambda *args, **kwargs: [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        )

    def test_instantiate_RelionParticlesStarFile(self):
        self.setup_dirs(10)
        pf = RelionParticlesStarFile("Extract/job010/particles.star")
        assert pf.__dict__ == {
            "file": Path("Extract/job010/particles.star"),
            "name": "Extract/job010/particles.star",
        }

    def test_get_cets_from_relion_particles_star(self):
        self.setup_dirs(10)
        pf = RelionParticlesStarFile("Extract/job010/particles.star")
        cets_parts = pf.get_cets_particles("TS_01")
        assert len(cets_parts) == 6623
        assert cets_parts[0].__dict__ == {
            "coordinate_systems": [
                CoordinateSystem(
                    name="physical coordinates",
                    axes=[
                        Axis(
                            name="physical coordinates x axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates y axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                        Axis(
                            name="physical coordinates z axis",
                            axis_unit="Ångstrom",
                            axis_type=None,
                        ),
                    ],
                )
            ],
            "coordinate_transformations": [
                Affine(
                    name="Alignment relative to parent tomogram",
                    input=None,
                    output=None,
                    affine=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                ),
                Affine(
                    name="Averaging alignment",
                    input=None,
                    output=None,
                    affine=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                ),
                Translation(
                    name="Averaging translation",
                    input=None,
                    output=None,
                    translation=[0.0, 0.0, 0.0],
                ),
            ],
            "depth": 3,
            "height": 2,
            "path": "000001@Extract/job010/Subtomograms/TS_01/1_stack2d.mrcs",
            "width": 1,
        }

    def test_get_coords_object(self):
        self.setup_dirs(10)
        pf = RelionParticlesStarFile("Extract/job010/particles.star")
        coordsobj = pf.get_coords_object()
        assert len(coordsobj) == 1
        assert coordsobj[0].__dict__ == {
            "annotation_files": {
                "TS_01": Path("Picks/job009/annotations/TS_01_spheres.star"),
                "TS_03": Path("Picks/job009/annotations/TS_03_spheres.star"),
                "TS_43": Path("Picks/job009/annotations/TS_43_spheres.star"),
                "TS_45": Path("Picks/job009/annotations/TS_45_spheres.star"),
                "TS_54": Path("Picks/job009/annotations/TS_54_spheres.star"),
            },
            "name": "Picks/job009/particles.star",
        }


# ToDo: This is a placeholder class that will be replaced with a CETS model later
def test_instantiate_sphere():
    sp = Sphere((1.0, 2.0, 3.0), 10.0)
    assert sp.origin == (1.0, 2.0, 3.0)
    assert sp.radius == 10.0
