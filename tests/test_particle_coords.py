from tests.testing_tools import CetsRelionTest
from cets_relion.particle_coords import (
    RelionParticleCoordsFile,
    Sphere,
    RelionSphereAnnotations,
    RelionPointAnnotations,
)
from cets_relion.objs.coordinate_systems import RELION_COORDS_PHYSICAL
from pathlib import Path


class TestRelionParticleCoords(CetsRelionTest):
    def test_instantiate_RelionParticleCoordsFile(self):
        self.setup_dirs(9)
        pcf = RelionParticleCoordsFile("Picks/job009/particles.star")
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
        pcf = RelionParticleCoordsFile("Picks/job009/particles.star")
        parts = pcf.get_tomo_cets_particle_set("TS_01")
        self.assertEqual(parts.coordinate_systems, [RELION_COORDS_PHYSICAL])
        assert parts.path == pcf.name
        assert len(parts.origin3D) == 6981

    def test_get_parts_for_all_tomos(self):
        pcf = RelionParticleCoordsFile(
            str(self.test_data / "skeleton_project/Picks/job009/particles.star")
        )
        parts = pcf.all_particle_sets()
        exp_counts = {
            "TS_45": 8364,
            "TS_43": 8573,
            "TS_54": 6548,
            "TS_01": 6981,
            "TS_03": 5622,
        }
        print(parts.keys())
        for ts, psobj in parts.items():
            self.assertEqual(psobj.coordinate_systems, [RELION_COORDS_PHYSICAL])
            assert psobj.path == pcf.name
            assert len(psobj.origin3D) == exp_counts[ts]

    def test_get_annotation_file_type(self):
        self.setup_dirs(19)
        j9 = RelionParticleCoordsFile("Picks/job009/particles.star")
        assert j9.determine_annotation_type(j9.annotation_files["TS_01"]) == "spheres"
        j19 = RelionParticleCoordsFile("Picks/job019/particles.star")
        assert j19.determine_annotation_type(j19.annotation_files["TS_01"]) == "points"

    def test_get_secondary_annotations_points(self):
        # points have no secondary annotations
        self.setup_dirs(19)
        j9 = RelionParticleCoordsFile("Picks/job019/particles.star")
        assert j9.get_secondary_annotations("TS_01") == []

    def test_get_secondary_annotations_spheres(self):
        # points have no secondary annotations
        self.setup_dirs(9)
        j9 = RelionParticleCoordsFile("Picks/job009/particles.star")
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


# ToDo: This is a placeholder class that will be replaced with a CETS model later
def test_instantiate_sphere():
    sp = Sphere((1.0, 2.0, 3.0), 10.0)
    assert sp.origin == (1.0, 2.0, 3.0)
    assert sp.radius == 10.0
