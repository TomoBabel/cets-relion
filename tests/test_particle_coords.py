from tests.test_data.results.particle_map_objs import TS_01_1
from tests.testing_tools import CetsRelionTest
from cets_relion.relion_to_cets.particle_coords import (
    RelionCoordsStarFile,
    Sphere,
    RelionSphereAnnotations,
    RelionParticlesStarFile,
)
from cets_relion.objs.coordinate_systems import RELION_COORDS_PHYSICAL
from pathlib import Path
from pytest import fixture


class TestRelionParticleCoordsStarFile(CetsRelionTest):
    def test_instantiate_RelionParticleCoordsFile(self):
        self.setup_dirs(9)
        pcf = RelionCoordsStarFile("Picks/job009/particles.star")
        assert pcf.name == "Picks/job009/particles.star"
        assert pcf.file == Path("Picks/job009/particles.star")

    def test_get_parts_for_tomo(self):
        self.setup_dirs(9)
        pcf = RelionCoordsStarFile("Picks/job009/particles.star")
        parts = pcf.get_tomo_cets_coords_set("TS_01")
        self.assertEqual(parts.coordinate_systems, [RELION_COORDS_PHYSICAL])
        assert parts.path == pcf.name
        assert len(parts.origin3D) == 6981

    def test_get_annotation_file_type(self):
        self.setup_dirs(19)
        j9 = RelionCoordsStarFile("Picks/job009/particles.star")
        assert j9.determine_annotation_type() == "spheres"
        j19 = RelionCoordsStarFile("Picks/job019/particles.star")
        assert j19.determine_annotation_type() == "particles"

    def test_get_secondary_annotations_points(self):
        # points have no secondary annotations
        self.setup_dirs(19)
        j9 = RelionCoordsStarFile("Picks/job019/particles.star")
        assert j9.get_secondary_annotations("TS_01") is None

    def test_sphere_annotation_object(self):
        self.setup_dirs(9)
        sa = RelionSphereAnnotations("Picks/job009/annotations/TS_01_spheres.star")
        cets = sa.get_cets()
        assert len(cets) == 9
        assert cets[0].__dict__ == {
            "origin": (444.970917, 185.166, 208.641861),
            "radius": "43.955040",
        }

    def test_get_secondary_annotations_spheres(self):
        # points have no secondary annotations
        self.setup_dirs(9)
        j9 = RelionCoordsStarFile("Picks/job009/particles.star")
        annotations = j9.get_secondary_annotations("TS_01")
        assert isinstance(annotations, RelionSphereAnnotations)


class TestRelionParticlesStarFile(CetsRelionTest):
    @fixture(autouse=True)
    def _mock_get_mrc_dims(self, monkeypatch):
        monkeypatch.setattr(
            "cets_relion.relion_to_cets.particle_coords.get_mrc_dims",
            lambda *args, **kwargs: (1, 2, 3),
        )

    @fixture(autouse=True)
    def _mock_matrix_from_euler(self, monkeypatch):
        monkeypatch.setattr(
            "cets_relion.relion_to_cets.particle_coords.relion_eulers_to_matrix",
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
        assert cets_parts[0].__dict__ == TS_01_1

    def test_get_coords_object(self):
        self.setup_dirs(10)
        pf = RelionParticlesStarFile("Extract/job010/particles.star")
        coordsobj = pf.get_coords_object()
        assert len(coordsobj) == 1
        assert coordsobj[0].name == "Picks/job009/particles.star"

    def test_get_all_tomo_names_coords_file(self):
        self.setup_dirs(9)
        cf = RelionCoordsStarFile("Picks/job009/particles.star")
        assert cf.get_all_tomo_names() == ["TS_01", "TS_03", "TS_43", "TS_45", "TS_54"]

    def test_get_all_tomo_names_parts_file(self):
        self.setup_dirs(10)
        cf = RelionParticlesStarFile("Extract/job010/particles.star")
        assert cf.get_all_tomo_names() == ["TS_01", "TS_03", "TS_43", "TS_45", "TS_54"]


# ToDo: This is a placeholder class that will be replaced with a CETS model later
def test_instantiate_sphere():
    sp = Sphere((1.0, 2.0, 3.0), 10.0)
    assert sp.origin == (1.0, 2.0, 3.0)
    assert sp.radius == 10.0
