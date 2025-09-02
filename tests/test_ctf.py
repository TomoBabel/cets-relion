from tests.testing_tools import CetsRelionTest
from src.cets_relion.ctf import RelionCtfStarFile
from src.cets_relion.relion_reader import RelionPipeline
from pathlib import Path
from src.models.models import CTFMetadata


class CtfTests(CetsRelionTest):
    def test_instantiate_cets_ctf_object(self):
        self.setup_dirs(jobs_to=3)
        ctf = RelionCtfStarFile("CtfFind/job003/tilt_series_ctf.star")
        assert isinstance(ctf.file, Path)
        assert str(ctf.file) == "CtfFind/job003/tilt_series_ctf.star"
        assert ctf.name == "CtfFind/job003/tilt_series_ctf.star"
        assert isinstance(ctf.pipeline, RelionPipeline)

    def test_get_tilt_image_ctf(self):
        self.setup_dirs(jobs_to=3)
        ctf = RelionCtfStarFile("CtfFind/job003/tilt_series_ctf.star")
        ctfdata = ctf.get_tilt_image_ctf(
            ts_name="TS_01", image_name="frames/TS_01_004_6.0.mrc"
        )
        assert isinstance(ctfdata, CTFMetadata)
        assert ctfdata.defocus_u == 38871.554688
        assert ctfdata.defocus_v == 38659.703125
        assert ctfdata.defocus_angle == -86.54452
