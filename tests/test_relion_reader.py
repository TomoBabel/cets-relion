from cets_relion.relion_to_cets.relion_reader import RelionPipeline
from tests.test_data.pipelines.short_pipeline_networks import (
    FULL_EDGES,
    FULL_NODES,
    FILES_CRIT_EDGES,
    FILES_EDGES,
    FILES_NODES,
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
from tests.testing_tools import CetsRelionTest
from cets_relion.utils import get_job_number


class PipelineReaderTests(CetsRelionTest):
    @staticmethod
    def compare_nodes_edges(test_network, exp_nodes, exp_edges):
        nodes = list(test_network.graph.nodes)
        nodes.sort(key=lambda x: get_job_number(x))
        assert nodes == exp_nodes
        edges = list(test_network.graph.edges)
        edges.sort(key=lambda x: get_job_number(x[0]))
        assert edges == exp_edges

    def test_instantiate_RelionPipeline_obj_main_graph(self):
        rp = RelionPipeline(self.test_data / "pipelines/short_pipeline.star")
        self.compare_nodes_edges(rp, FULL_NODES, FULL_EDGES)

    def test_instatiate_RelionPipeline_obj_jobs_graph(self):
        rp = RelionPipeline(
            self.test_data / "pipelines/short_pipeline.star"
        ).process_layer()
        self.compare_nodes_edges(rp, JOBS_NODES, JOBS_EDGES)

    def test_instatiate_RelionPipeline_obj_files_graph(self):
        rp = RelionPipeline(
            self.test_data / "pipelines/short_pipeline.star"
        ).files_layer()
        self.compare_nodes_edges(rp, FILES_NODES, FILES_EDGES)

    def test_upstream_full_critical_path(self):
        rp = RelionPipeline(self.test_data / "pipelines/short_pipeline.star")
        full_crit = rp.upstream_critical_path(start="Denoise/job008/tomograms.star")
        self.compare_nodes_edges(full_crit, FULL_CRIT_NODES, FULL_CRIT_EDGES)

    def test_upstream_files_critical_path(self):
        rp = RelionPipeline(
            self.test_data / "pipelines/short_pipeline.star"
        ).files_layer()
        files_crit = rp.upstream_critical_path(start="Denoise/job008/tomograms.star")
        self.compare_nodes_edges(files_crit, FILES_CRIT_NODES, FILES_CRIT_EDGES)

    def test_upstream_jobs_critical_path(self):
        rp = RelionPipeline(
            self.test_data / "pipelines/short_pipeline.star"
        ).process_layer()
        jobs_crit = rp.upstream_critical_path(start="Denoise/job008/")
        self.compare_nodes_edges(jobs_crit, JOBS_CRIT_NODES, UPSTREAM_JOBS_CRIT_EDGES)

    def test_downstream_full_critical_path(self):
        rp = RelionPipeline(self.test_data / "pipelines/short_pipeline.star")
        full_crit = rp.downstream_critical_path(start="Import/job001/tilt_series.star")
        self.compare_nodes_edges(full_crit, FULL_NODES[1:], FULL_EDGES[1:])

    def test_downstream_files_critical_path(self):
        rp = RelionPipeline(
            self.test_data / "pipelines/short_pipeline.star"
        ).files_layer()
        full_crit = rp.downstream_critical_path(
            start="MotionCorr/job002/corrected_tilt_series.star"
        )
        self.compare_nodes_edges(
            full_crit, DOWNSTREAM_CRIT_FILES_NODES, DOWNSTREAM_CRIT_FILES_EDGES
        )

    def test_jobs_downstream_critical_path(self):
        rp = RelionPipeline(
            self.test_data / "pipelines/short_pipeline.star"
        ).process_layer()
        full_crit = rp.downstream_critical_path(start="MotionCorr/job002/")
        self.compare_nodes_edges(full_crit, JOBS_NODES[1:], JOBS_EDGES[1:])

    def test_next_upstream_jobs(self):
        rp = RelionPipeline(self.test_data / "pipelines/forked_pipeline.star")
        nj = rp.next_upstream_jobs("JoinStar/job005/")
        assert nj == ["CtfFind/job003/", "CtfFind/job004/"]

    def test_next_upstream_jobs_of_type(self):
        rp = RelionPipeline(self.test_data / "pipelines/forked_pipeline.star")
        nj = rp.next_upstream_jobs("AutoPick/job006/", ["relion.ctffind.ctffind4"])
        assert nj == ["CtfFind/job003/", "CtfFind/job004/"]

    def test_next_downstream_jobs(self):
        rp = RelionPipeline(self.test_data / "pipelines/forked_pipeline.star")
        nj = rp.next_downstream_jobs("MotionCorr/job002/", ["relion.ctffind.ctffind4"])
        assert nj == ["CtfFind/job003/", "CtfFind/job004/"]

    def test_next_downstream_jobs_of_type(self):
        rp = RelionPipeline(self.test_data / "pipelines/forked_pipeline.star")
        nj = rp.next_downstream_jobs("Import/job001/", ["relion.ctffind.ctffind4"])
        assert nj == ["CtfFind/job003/", "CtfFind/job004/"]

    def test_next_upstream_files_of_type_multple_returns(self):
        rp = RelionPipeline(self.test_data / "pipelines/forked_pipeline.star")
        lf = rp.next_upstream_files(
            start="JoinStar/job005/", relion_type=["TomogramGroupMetadata"]
        )
        assert lf == [
            "CtfFind/job003/tilt_series_ctf.star",
            "CtfFind/job004/tilt_series_ctf.star",
        ]

    def test_next_upstream_file_of_type_just_type(self):
        rp = RelionPipeline(self.test_data / "pipelines/default_pipeline.star")
        lf = rp.next_upstream_files(
            start="ModelAngelo/job080/", relion_type=["TomogramGroupMetadata"]
        )
        assert lf == ["Denoise/job008/tomograms.star", "Polish/job070/tomograms.star"]

    def test_next_upstream_file_of_type_with_kwds(self):
        rp = RelionPipeline(self.test_data / "pipelines/default_pipeline.star")
        lf = rp.next_upstream_files(
            start="ModelAngelo/job080/",
            relion_type=["TomogramGroupMetadata"],
            kwds=["polish"],
        )
        assert lf == ["Polish/job070/tomograms.star"]

    def test_next_downstream_file_match_all_params(self):
        rp = RelionPipeline(self.test_data / "pipelines/short_pipeline.star")
        found = rp.next_downstream_files(
            start="MotionCorr/job002/corrected_tilt_series.star",
            relion_type=["TomogramGroupMetadata"],
            ext=["star"],
            kwds=["relion", "tomo", "ctffind"],
        )
        assert found == ["CtfFind/job003/tilt_series_ctf.star"]

    def test_next_downstream_file_one_kwd(self):
        rp = RelionPipeline(self.test_data / "pipelines/short_pipeline.star")
        found = rp.next_downstream_files(
            start="MotionCorr/job002/corrected_tilt_series.star", kwds=["ctffind"]
        )
        assert set(found) == {
            "CtfFind/job003/logfile.pdf",
            "CtfFind/job003/tilt_series_ctf.star",
        }

    def test_next_downstream_file_no_match(self):
        rp = RelionPipeline(self.test_data / "pipelines/short_pipeline.star")
        found = rp.next_downstream_files(
            start="MotionCorr/job002/corrected_tilt_series.star",
            relion_type=["TomogramGroupMetadata"],
            ext=["star"],
            kwds=["relion", "tomo", "ctffind", "XXXXX"],
        )
        assert found == []
