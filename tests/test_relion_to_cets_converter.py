from pathlib import Path

from cets_relion.relion_to_cets.motion_corr import RelionMotionCorrStarFile
from cets_relion.relion_to_cets.movies import RelionMoviesStarFile
from cets_relion.relion_to_cets.tilt_series import RelionTiltSeriesStarfile
from cets_relion.relion_to_cets.tomograms import RelionTomosStarfile
from tests.testing_tools import CetsRelionTest
from cets_relion.relion_to_cets.relion_to_cets_converter import (
    parse_optimisation_set,
    RelionCetsConverter,
)
from cets_relion.relion_to_cets.particle_coords import (
    RelionCoordsStarFile,
    RelionParticlesStarFile,
)
from cets_relion.relion_to_cets.relion_reader import RelionPipeline


class TestParseOptimisationSet(CetsRelionTest):
    def test_parsing_optimisation_set_with_extracted_parts(self):
        self.setup_dirs(12)
        opt = parse_optimisation_set(Path("Refine3D/job012/run_optimisation_set.star"))
        assert isinstance(opt["particles"], RelionParticlesStarFile)
        assert opt["particles"].name == "Refine3D/job012/run_data.star"
        assert opt.get("picks") is None
        assert isinstance(opt["tomos"], RelionTomosStarfile)
        assert opt["tomos"].name == "Denoise/job008/tomograms.star"

    def test_parsing_optimisation_set_with_only_coords(self):
        self.setup_dirs(9)
        opt = parse_optimisation_set(Path("Picks/job009/optimisation_set.star"))
        assert isinstance(opt["picks"], RelionCoordsStarFile)
        assert opt["picks"].name == "Picks/job009/particles.star"
        assert opt.get("particles") is None
        assert isinstance(opt["tomos"], RelionTomosStarfile)
        assert opt["tomos"].name == "Denoise/job008/tomograms.star"


class RelionCetsConverterTest(CetsRelionTest):
    def test_instantiate_converter_with_import_job(self):
        self.setup_dirs(1)
        converter = RelionCetsConverter(terminal_job="Import/job001/")
        assert isinstance(converter.pipeline, RelionPipeline)
        assert isinstance(converter.movies[0], RelionMoviesStarFile)
        assert converter.movies[0].name == "Import/job001/tilt_series.star"
        assert converter.movies[0].ctf_files == []
        assert converter.movies[0].mocorr_files == []
        for f in [
            "ctf",
            "mocorr",
            "picks",
            "particles",
            "tilt_series",
            "tomos",
            "averages",
        ]:
            assert converter.__getattribute__(f) == []

    def test_instantiate_converter_with_mocorr_job(self):
        self.setup_dirs(2)
        converter = RelionCetsConverter(terminal_job="MotionCorr/job002/")
        assert isinstance(converter.pipeline, RelionPipeline)
        assert isinstance(converter.movies[0], RelionMoviesStarFile)
        assert isinstance(converter.mocorr[0], RelionMotionCorrStarFile)
        assert converter.movies[0].name == "Import/job001/tilt_series.star"
        assert converter.movies[0].ctf_files == []
        assert converter.movies[0].mocorr_files == converter.mocorr
        assert (
            converter.mocorr[0].name == "MotionCorr/job002/corrected_tilt_series.star"
        )
        for f in [
            "ctf",
            "picks",
            "particles",
            "tilt_series",
            "tomos",
            "averages",
        ]:
            assert converter.__getattribute__(f) == []

    def test_instantiate_converter_with_ctf_job(self):
        self.setup_dirs(3)
        converter = RelionCetsConverter(terminal_job="CtfFind/job003/")
        assert isinstance(converter.pipeline, RelionPipeline)
        assert isinstance(converter.movies[0], RelionMoviesStarFile)
        assert isinstance(converter.mocorr[0], RelionMotionCorrStarFile)
        assert isinstance(converter.ctf[0], RelionTiltSeriesStarfile)
        assert converter.movies[0].ctf_files == converter.ctf
        assert converter.movies[0].mocorr_files == converter.mocorr
        assert converter.movies[0].name == "Import/job001/tilt_series.star"
        assert (
            converter.mocorr[0].name == "MotionCorr/job002/corrected_tilt_series.star"
        )
        assert converter.ctf[0].name == "CtfFind/job003/tilt_series_ctf.star"
        for f in [
            "picks",
            "particles",
            "tilt_series",
            "tomos",
            "averages",
        ]:
            assert converter.__getattribute__(f) == []

    def test_instantiate_converter_with_exclude_job(self):
        self.setup_dirs(4)
        converter = RelionCetsConverter(terminal_job="ExcludeTiltImages/job004/")
        assert isinstance(converter.pipeline, RelionPipeline)
        assert isinstance(converter.movies[0], RelionMoviesStarFile)
        assert isinstance(converter.mocorr[0], RelionMotionCorrStarFile)
        assert isinstance(converter.ctf[0], RelionTiltSeriesStarfile)
        assert isinstance(converter.tilt_series[0], RelionTiltSeriesStarfile)
        assert converter.movies[0].ctf_files == converter.ctf
        assert converter.movies[0].mocorr_files == converter.mocorr
        assert converter.movies[0].name == "Import/job001/tilt_series.star"
        assert (
            converter.mocorr[0].name == "MotionCorr/job002/corrected_tilt_series.star"
        )
        assert converter.ctf[0].name == "CtfFind/job003/tilt_series_ctf.star"
        assert (
            converter.tilt_series[0].name
            == "ExcludeTiltImages/job004/selected_tilt_series.star"
        )
        for f in [
            "picks",
            "particles",
            "tomos",
            "averages",
        ]:
            assert converter.__getattribute__(f) == []

    def test_instantiate_converter_with_align_job(self):
        self.setup_dirs(5)
        converter = RelionCetsConverter(terminal_job="AlignTiltSeries/job005/")
        assert isinstance(converter.pipeline, RelionPipeline)
        assert isinstance(converter.movies[0], RelionMoviesStarFile)
        assert isinstance(converter.mocorr[0], RelionMotionCorrStarFile)
        assert isinstance(converter.ctf[0], RelionTiltSeriesStarfile)
        assert isinstance(converter.tilt_series[0], RelionTiltSeriesStarfile)
        assert converter.movies[0].ctf_files == converter.ctf
        assert converter.movies[0].mocorr_files == converter.mocorr
        assert converter.movies[0].name == "Import/job001/tilt_series.star"
        assert (
            converter.mocorr[0].name == "MotionCorr/job002/corrected_tilt_series.star"
        )
        assert converter.ctf[0].name == "CtfFind/job003/tilt_series_ctf.star"
        assert (
            converter.tilt_series[0].name
            == "AlignTiltSeries/job005/aligned_tilt_series.star"
        )
        for f in [
            "picks",
            "particles",
            "tomos",
            "averages",
        ]:
            assert converter.__getattribute__(f) == []

    def test_instantiate_converter_with_picking_job(self):
        """First instance of using a optimisation set for tomos and picks/parts"""
        self.setup_dirs(9)
        converter = RelionCetsConverter(terminal_job="Picks/job009/")
        assert isinstance(converter.pipeline, RelionPipeline)
        assert isinstance(converter.movies[0], RelionMoviesStarFile)
        assert isinstance(converter.mocorr[0], RelionMotionCorrStarFile)
        assert isinstance(converter.ctf[0], RelionTiltSeriesStarfile)
        assert isinstance(converter.tilt_series[0], RelionTiltSeriesStarfile)
        assert isinstance(converter.tomos[0], RelionTomosStarfile)
        assert isinstance(converter.picks[0], RelionCoordsStarFile)
        assert converter.movies[0].ctf_files == converter.ctf
        assert converter.movies[0].mocorr_files == converter.mocorr
        assert converter.movies[0].name == "Import/job001/tilt_series.star"
        assert (
            converter.mocorr[0].name == "MotionCorr/job002/corrected_tilt_series.star"
        )
        assert converter.ctf[0].name == "CtfFind/job003/tilt_series_ctf.star"
        assert (
            converter.tilt_series[0].name
            == "AlignTiltSeries/job005/aligned_tilt_series.star"
        )
        assert converter.tomos[0].name == "Denoise/job008/tomograms.star"
        assert converter.picks[0].name == "Picks/job009/particles.star"
        for f in [
            "particles",
            "averages",
        ]:
            assert converter.__getattribute__(f) == []

    def test_instantiate_converter_with_extract_job(self):
        """every attr in the converter should now be filled"""
        self.setup_dirs(10)
        converter = RelionCetsConverter(terminal_job="Extract/job010/")
        assert isinstance(converter.pipeline, RelionPipeline)
        assert isinstance(converter.movies[0], RelionMoviesStarFile)
        assert isinstance(converter.mocorr[0], RelionMotionCorrStarFile)
        assert isinstance(converter.ctf[0], RelionTiltSeriesStarfile)
        assert isinstance(converter.tilt_series[0], RelionTiltSeriesStarfile)
        assert isinstance(converter.tomos[0], RelionTomosStarfile)
        assert isinstance(converter.picks[0], RelionCoordsStarFile)
        assert isinstance(converter.particles[0], RelionParticlesStarFile)
        assert converter.movies[0].ctf_files == converter.ctf
        assert converter.movies[0].mocorr_files == converter.mocorr
        assert converter.movies[0].name == "Import/job001/tilt_series.star"
        assert (
            converter.mocorr[0].name == "MotionCorr/job002/corrected_tilt_series.star"
        )
        assert converter.ctf[0].name == "CtfFind/job003/tilt_series_ctf.star"
        assert (
            converter.tilt_series[0].name
            == "AlignTiltSeries/job005/aligned_tilt_series.star"
        )
        assert converter.averages == []
        assert converter.tomos[0].name == "Denoise/job008/tomograms.star"
        assert converter.picks[0].name == "Picks/job009/particles.star"
        assert converter.particles[0].name == "Extract/job010/particles.star"

    def test_instantiate_converter_with_refine_job(self):
        """every attr in the converter should now be filled"""
        self.setup_dirs(64)
        converter = RelionCetsConverter(terminal_job="Refine3D/job064/")
        assert isinstance(converter.pipeline, RelionPipeline)
        assert isinstance(converter.movies[0], RelionMoviesStarFile)
        assert isinstance(converter.mocorr[0], RelionMotionCorrStarFile)
        assert isinstance(converter.ctf[0], RelionTiltSeriesStarfile)
        assert isinstance(converter.tilt_series[0], RelionTiltSeriesStarfile)
        assert isinstance(converter.tomos[0], RelionTomosStarfile)
        assert isinstance(converter.picks[0], RelionCoordsStarFile)
        assert isinstance(converter.particles[0], RelionParticlesStarFile)
        assert converter.movies[0].ctf_files == converter.ctf
        assert converter.movies[0].mocorr_files == converter.mocorr
        assert converter.movies[0].name == "Import/job001/tilt_series.star"
        assert (
            converter.mocorr[0].name == "MotionCorr/job002/corrected_tilt_series.star"
        )
        assert converter.ctf[0].name == "CtfFind/job003/tilt_series_ctf.star"
        assert (
            converter.tilt_series[0].name
            == "AlignTiltSeries/job005/aligned_tilt_series.star"
        )
        assert converter.tomos[0].name == "Polish/job060/tomograms.star"
        assert converter.picks[0].name == "Picks/job009/particles.star"
        assert converter.particles[0].name == "Refine3D/job064/run_data.star"
        assert converter.averages[0].path == Path("Refine3D/job064/run_class001.mrc")
        assert converter.averages[0].particles == converter.particles[0].name

    def test_instantiate_converter_with_postprocess_job(self):
        self.setup_dirs(22)
        converter = RelionCetsConverter(terminal_job="PostProcess/job022/")
        assert isinstance(converter.pipeline, RelionPipeline)
        assert isinstance(converter.movies[0], RelionMoviesStarFile)
        assert isinstance(converter.mocorr[0], RelionMotionCorrStarFile)
        assert isinstance(converter.ctf[0], RelionTiltSeriesStarfile)
        assert isinstance(converter.tilt_series[0], RelionTiltSeriesStarfile)
        assert isinstance(converter.tomos[0], RelionTomosStarfile)
        assert isinstance(converter.picks[0], RelionCoordsStarFile)
        assert isinstance(converter.particles[0], RelionParticlesStarFile)
        assert converter.movies[0].ctf_files == converter.ctf
        assert converter.movies[0].mocorr_files == converter.mocorr
        assert converter.movies[0].name == "Import/job001/tilt_series.star"
        assert (
            converter.mocorr[0].name == "MotionCorr/job002/corrected_tilt_series.star"
        )
        assert converter.ctf[0].name == "CtfFind/job003/tilt_series_ctf.star"
        assert (
            converter.tilt_series[0].name
            == "AlignTiltSeries/job005/aligned_tilt_series.star"
        )
        assert converter.tomos[0].name == "Denoise/job008/tomograms.star"
        assert converter.picks[0].name == "Picks/job009/particles.star"
        assert converter.particles[0].name == "Refine3D/job015/run_data.star"
        assert converter.averages[0].path == Path("PostProcess/job022/postprocess.mrc")
        assert converter.averages[0].particles == converter.particles[0].name

    def test_instantiate_converter_with_reconstruct_job(self):
        self.setup_dirs(42)
        converter = RelionCetsConverter(terminal_job="Reconstruct/job042/")
        assert isinstance(converter.pipeline, RelionPipeline)
        assert isinstance(converter.movies[0], RelionMoviesStarFile)
        assert isinstance(converter.mocorr[0], RelionMotionCorrStarFile)
        assert isinstance(converter.ctf[0], RelionTiltSeriesStarfile)
        assert isinstance(converter.tilt_series[0], RelionTiltSeriesStarfile)
        assert isinstance(converter.tomos[0], RelionTomosStarfile)
        assert isinstance(converter.picks[0], RelionCoordsStarFile)
        assert isinstance(converter.particles[0], RelionParticlesStarFile)
        assert converter.movies[0].ctf_files == converter.ctf
        assert converter.movies[0].mocorr_files == converter.mocorr
        assert converter.movies[0].name == "Import/job001/tilt_series.star"
        assert (
            converter.mocorr[0].name == "MotionCorr/job002/corrected_tilt_series.star"
        )
        assert converter.ctf[0].name == "CtfFind/job003/tilt_series_ctf.star"
        assert (
            converter.tilt_series[0].name
            == "AlignTiltSeries/job005/aligned_tilt_series.star"
        )
        assert converter.tomos[0].name == "Polish/job040/tomograms.star"
        assert converter.picks[0].name == "Picks/job009/particles.star"
        assert converter.particles[0].name == "Extract/job041/particles.star"
        assert converter.averages[0].path == Path("Reconstruct/job042/merged.mrc")
        assert converter.averages[0].particles == converter.particles[0].name

    def test_get_all_tomos_with_full_project(self):
        self.setup_dirs(64)
        converter = RelionCetsConverter(terminal_job="Refine3D/job064/")
        assert converter.get_all_tomo_names() == [
            "TS_01",
            "TS_03",
            "TS_43",
            "TS_45",
            "TS_54",
        ]

    def test_get_all_tomos_with_extract_job(self):
        """every attr in the converter should now be filled"""
        self.setup_dirs(10)
        converter = RelionCetsConverter(terminal_job="Extract/job010/")
        assert converter.get_all_tomo_names() == [
            "TS_01",
            "TS_03",
            "TS_43",
            "TS_45",
            "TS_54",
        ]

    def test_get_all_tomos_with_picking_job(self):
        """First instance of using a optimisation set for tomos and picks/parts"""
        self.setup_dirs(9)
        converter = RelionCetsConverter(terminal_job="Picks/job009/")
        assert converter.get_all_tomo_names() == [
            "TS_01",
            "TS_03",
            "TS_43",
            "TS_45",
            "TS_54",
        ]

    def test_get_all_tomos_with_reconstruct_job(self):
        self.setup_dirs(6)
        converter = RelionCetsConverter(terminal_job="Tomograms/job006/")
        assert converter.get_all_tomo_names() == [
            "TS_01",
            "TS_03",
            "TS_43",
            "TS_45",
            "TS_54",
        ]

    def test_get_all_tomos_with_align_job(self):
        self.setup_dirs(5)
        converter = RelionCetsConverter(terminal_job="AlignTiltSeries/job005/")
        assert converter.get_all_tomo_names() == [
            "TS_01",
            "TS_03",
            "TS_43",
            "TS_45",
            "TS_54",
        ]

    def test_get_all_tomos_with_exclude_job(self):
        self.setup_dirs(4)
        converter = RelionCetsConverter(terminal_job="ExcludeTiltImages/job004/")
        assert converter.get_all_tomo_names() == [
            "TS_01",
            "TS_03",
            "TS_43",
            "TS_45",
            "TS_54",
        ]

    def test_get_all_tomos_with_ctf_job(self):
        self.setup_dirs(3)
        converter = RelionCetsConverter(terminal_job="CtfFind/job003/")
        assert converter.get_all_tomo_names() == [
            "TS_01",
            "TS_03",
            "TS_43",
            "TS_45",
            "TS_54",
        ]

    def test_get_all_tomos_with_mocorr_job(self):
        self.setup_dirs(2)
        converter = RelionCetsConverter(terminal_job="MotionCorr/job002/")
        assert converter.get_all_tomo_names() == [
            "TS_01",
            "TS_03",
            "TS_43",
            "TS_45",
            "TS_54",
        ]

    def test_get_all_tomos_with_import_job(self):
        self.setup_dirs(1)
        converter = RelionCetsConverter(terminal_job="Import/job001/")
        assert converter.get_all_tomo_names() == [
            "TS_01",
            "TS_03",
            "TS_43",
            "TS_45",
            "TS_54",
        ]
