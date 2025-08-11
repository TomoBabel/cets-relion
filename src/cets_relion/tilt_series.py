from __future__ import annotations

from typing import List, Union
from pathlib import Path
from gemmi import cif
from src.cets_relion.relion_reader import RelionPipeline
from src.cets_relion.movies import RelionMoviesStarFile


class RelionTiltSeriesStarfile(object):
    """Class for handling a global tilt series data file from RELION

    will probably be subclassed for job-specific variants of this type of file

    Many jobs create this type of file, this object shoudl enable tracing back to the
    original movies and making the necessary objects
    """

    def __init__(self, file_name: str, pipeline: str = "default_pipeline.star") -> None:
        self.name = file_name
        self.pipeline = RelionPipeline(pipeline)

    def get_raw_files(
        self,
    ) -> List[Union[RelionMoviesStarFile, RelionTiltSeriesStarfile]]:
        upstream = self.pipeline.upstream_critical_path(start=self.name)
        import_files = []
        for unode in upstream.nodes:
            if (
                upstream.nodes[unode].get("relion_type") == "TomogramGroupMetadata"
                and upstream.nodes[unode].get("file_type") == "star"
                and "import" in upstream.nodes[unode].get("kwds")
            ):
                import_files.append(unode)
        raw_data_files: List[Union[RelionMoviesStarFile, RelionTiltSeriesStarfile]] = []
        for file in import_files:
            # get the job the file came from
            importjob = list(self.pipeline.graph.predecessors(file))[0]

            # determine if was import of movies or merged tomos
            jobfile = str(Path(importjob) / "job.star")
            jobop_block = cif.read_file(jobfile).find_block("joboptions_values")
            jobops = dict(
                list(
                    jobop_block.find(
                        prefix="_rln", tags=["JobOptionVariable", "JobOptionValue"]
                    )
                )
            )
            if jobops["images_are_motion_corrected"] == "No":
                raw_data_files.append(RelionMoviesStarFile(file))
            else:
                raw_data_files.append(RelionTiltSeriesStarfile(file))

        return raw_data_files
