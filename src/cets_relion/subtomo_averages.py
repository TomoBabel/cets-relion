import os
from typing import Union, List
from pathlib import Path
from gemmi import cif

from cets_relion.relion_reader import RelionPipeline
from cets_data_model.models.models import Average, ParticleMap
from cets_relion.particle_coords import RelionParticlesStarFile


class RelionSubtomoAverage(object):
    """A subtomo average from a relion Refine3D, CLass3D, Reconstruct, or PostProcess job"""

    def __init__(self, file_name: Union[str, os.PathLike]):
        self.file_name = str(file_name)
        self.path = Path(self.file_name)
        if self.path.parts[0] == "Class3D":
            raise NotImplementedError(
                "Class3D classes cannot be used for generating CETS averages"
            )
        if self.path.parts[0] == "Refine3D":
            opt_sets = sorted(list(self.path.parent.glob("*_optimisation_set.star")))
            self.opt_set = opt_sets[-1]
        elif self.path.parts[0] == "PostProcess":
            # find refine dir from the previous refine3D
            pipeline = RelionPipeline("default_pipeline.star")
            refine_job = pipeline.next_upstream_jobs(
                start=str(self.path.parent) + "/",
                jobtypes=["relion.refine3d.tomo", "relion.refine3d.tomo.helical"],
            )[0]
            self.opt_set = Path(refine_job) / "run_optimisation_set.star"

        elif self.path.parts[0] == "Reconstruct":
            # find the optimization set from the extract job
            pipeline = RelionPipeline("default_pipeline.star")
            extract_job = pipeline.next_upstream_jobs(
                start=str(self.path.parent) + "/", jobtypes=["relion.pseudosubtomo"]
            )[0]
            self.opt_set = Path(extract_job) / "optimisation_set.star"

        else:
            raise ValueError(
                "Invalid job type, must be 'PostProcess', 'Class3D', 'Reconstruct',"
                "or 'Refine3D'"
            )

        opt = cif.read_file(str(self.opt_set)).sole_block()
        self.tomos = opt.find_pair("_rlnTomoTomogramsFile")[1]
        self.particles = opt.find_pair("_rlnTomoParticlesFile")[1]

    def get_particle_maps(self) -> List[ParticleMap]:
        parts = RelionParticlesStarFile(self.particles)
        return parts.get_cets_particles()

    def get_cets_average(self) -> Average:
        return Average(name=self.file_name, particle_maps=self.get_particle_maps())
