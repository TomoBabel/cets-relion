from __future__ import annotations

from typing import List, Dict
from pathlib import Path
from src.cets_relion.relion_reader import RelionPipeline
from src.cets_relion.utils import joboptions_from_jobstar_file
from gemmi import cif


class RelionTiltSeriesStarfile(object):
    """Class for handling a global tilt series data file from RELION


    can be subclassed for job-specific variants of this type of file

    Many jobs create this type of file, this object should enable tracing back to the
    original movies and making the necessary objects
    """

    def __init__(self, file_name: str, pipeline: str = "default_pipeline.star") -> None:
        self.name = file_name
        self.pipeline = RelionPipeline(pipeline)

    def get_raw_files(
        self,
    ) -> List[str]:
        upstream = self.pipeline.upstream_critical_path(start=self.name)
        import_files = []
        for unode in upstream.nodes:
            if (
                upstream.nodes[unode].get("relion_type") == "TomogramGroupMetadata"
                and upstream.nodes[unode].get("file_type") == "star"
                and "import" in upstream.nodes[unode].get("kwds")
            ):
                import_files.append(unode)
        raw_data_files = []
        for file in import_files:
            # get the job the file came from
            importjob = list(self.pipeline.graph.predecessors(file))[0]
            # determine if was import of movies or merged tomos
            jobfile = str(Path(importjob) / "job.star")
            jobops = joboptions_from_jobstar_file(jobfile)
            if jobops["images_are_motion_corrected"] == "No":
                raw_data_files.append(file)
            else:
                raw_data_files.append(file)

        return raw_data_files

    def get_joboptions(self) -> Dict[str, str]:
        jobfile = Path(self.name).parent / "job.star"
        return joboptions_from_jobstar_file(str(jobfile))

    def tilt_series_in_file(self, ts_name: str) -> bool:
        """Check if a specific tilt series is in this file

        Args:
            ts_name (str): Tilt series name to check

        Returns:
            bool: Is the tilt series present in this file
        """
        data = cif.read_file(self.name).sole_block()
        names = data.find(prefix="_rln", tags=["TomoName"])
        return ts_name in [x[0] for x in names]

    def get_tilt_series_star_file(self, ts_name: str) -> str:
        """Get the path of star file containing info on a single tilt series image set

        Args:
            ts_name (str): The tilt series name

        Returns:
            str: Path of the starfile for that individual tilt series images
        """
        cifdata = (
            cif.read_file(self.name)
            .sole_block()
            .find(prefix="_rln", tags=["TomoName", "TomoTiltSeriesStarFile"])
        )
        for line in cifdata:
            if line[0] == ts_name:
                return line[1]
        return ""
