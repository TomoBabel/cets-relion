from src.cets_relion.relion_reader import RelionPipeline
from tests.testing_tools import CetsRelionTest
from tests.test_data.short_pipeline_networks import (
    FULL_EDGES,
    FULL_NODES,
    FILES_CRIT_EDGES,
    FILES_NODES,
    FILES_EDGES,
    FILES_CRIT_NODES,
    JOBS_EDGES,
    JOBS_NODES,
    JOBS_CRIT_NODES,
    FULL_CRIT_NODES,
    FULL_CRIT_EDGES,
    DOWNSTREAM_CRIT_FILES_NODES,
    DOWNSTREAM_CRIT_FILES_EDGES,
    UPSTREAM_JOBS_CRIT_EDGES,
)


class PipelineReaderTests(CetsRelionTest):
    def test_instatiate_RelionPipeline_obj_main_graph(self):
        rp = RelionPipeline(self.test_data / "short_pipeline.star")
        assert list(rp.graph.nodes()) == FULL_NODES
        assert list(rp.graph.edges()) == FULL_EDGES

    def test_instatiate_RelionPipeline_obj_jobs_graph(self):
        rp = RelionPipeline(self.test_data / "short_pipeline.star")
        assert list((rp.jobs_graph.nodes())) == JOBS_NODES
        assert list(rp.jobs_graph.edges()) == JOBS_EDGES

    def test_instatiate_RelionPipeline_obj_files_graph(self):
        rp = RelionPipeline(self.test_data / "short_pipeline.star")
        assert list((rp.files_graph.nodes())) == FILES_NODES
        assert list(rp.files_graph.edges()) == FILES_EDGES

    def test_upstream_full_critical_path(self):
        rp = RelionPipeline(self.test_data / "short_pipeline.star")
        full_crit = rp.upstream_critical_path(start="Denoise/job008/tomograms.star")
        assert list(full_crit.nodes()) == FULL_CRIT_NODES
        assert list(full_crit.edges()) == FULL_CRIT_EDGES

    def test_upstream_files_critical_path(self):
        rp = RelionPipeline(self.test_data / "short_pipeline.star")
        full_crit = rp.upstream_critical_path(
            start="Denoise/job008/tomograms.star", graph=rp.files_graph
        )
        assert list(full_crit.nodes()) == FILES_CRIT_NODES
        assert list(full_crit.edges()) == FILES_CRIT_EDGES

    def test_upstream_jobs_critical_path(self):
        rp = RelionPipeline(self.test_data / "short_pipeline.star")
        full_crit = rp.upstream_critical_path(
            start="Denoise/job008/", graph=rp.jobs_graph
        )
        assert list(full_crit.nodes()) == JOBS_CRIT_NODES
        assert list(full_crit.edges()) == UPSTREAM_JOBS_CRIT_EDGES

    def test_downstream_full_critical_path(self):
        rp = RelionPipeline(self.test_data / "short_pipeline.star")
        full_crit = rp.downstream_critical_path(start="Import/job001/tilt_series.star")
        assert list(full_crit.nodes()) == FULL_NODES[1:]
        assert list(full_crit.edges()) == FULL_EDGES[1:]

    def test_downstream_files_critical_path(self):
        rp = RelionPipeline(self.test_data / "short_pipeline.star")
        full_crit = rp.downstream_critical_path(
            start="MotionCorr/job002/corrected_tilt_series.star", graph=rp.files_graph
        )
        assert list(full_crit.nodes()) == DOWNSTREAM_CRIT_FILES_NODES
        assert list(full_crit.edges()) == DOWNSTREAM_CRIT_FILES_EDGES

    def test_jobs_downstream_critical_path(self):
        rp = RelionPipeline(self.test_data / "short_pipeline.star")
        full_crit = rp.downstream_critical_path(
            start="MotionCorr/job002/", graph=rp.jobs_graph
        )
        assert list(full_crit.nodes()) == JOBS_NODES[1:]
        assert list(full_crit.edges()) == JOBS_EDGES[1:]

    def test_last_job_of_type(self):
        rp = RelionPipeline(self.test_data / "short_pipeline.star")
        lj = rp.last_job_of_type("Denoise/job008/", ["relion.ctffind.ctffind4"])
        assert lj == ["CtfFind/job003/"]

    def test_last_job_of_type_with_multiple_retruls(self):
        rp = RelionPipeline(self.test_data / "forked_pipeline.star")
        lj = rp.last_job_of_type("JoinStar/job005/", ["relion.ctffind.ctffind4"])
        assert lj == ["CtfFind/job003/", "CtfFind/job004/"]
