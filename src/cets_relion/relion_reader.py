from gemmi import cif
from collections import namedtuple
from os import PathLike
import networkx as nx
from pathlib import Path

PipelineBlockNames = namedtuple(
    "PipelineBlockNames", ["outputs", "inputs", "nodes", "processes", "general"]
)
PIPELINE_BLOCK = PipelineBlockNames(
    "pipeline_output_edges",
    "pipeline_input_edges",
    "pipeline_nodes",
    "pipeline_processes",
    "pipeliner_general",
)


class RelionPipeline(object):
    def __init__(self, pipeline_file: PathLike):
        self.data = cif.read_file(str(pipeline_file))
        G = nx.DiGraph()

        jobs_block = self.data.find_block(PIPELINE_BLOCK.processes)
        jobs = jobs_block.find(tags=["_rlnPipeLineProcessName"])
        for job in jobs:
            G.add_node(Path(job[0]))

        inputs_block = self.data.find_block(PIPELINE_BLOCK.inputs)
        edges = inputs_block.find(
            prefix="_rlnPipeLine", tags=["EdgeFromNode", "EdgeProcess"]
        )
        G.add_edges_from(
            [(Path(x[0]).parent, Path(x[1]), {"file": x[0]}) for x in edges]
        )
        self.graph = G

    def parents(self, process: PathLike):
        if not isinstance(process, Path):
            process = Path(process)
        sub_nodes = nx.ancestors(self.graph, process) | {process}
        subgraph = self.graph.subgraph(sub_nodes).copy()
        return subgraph


def get_job_number(jobname: PathLike) -> int:
    return int(str(jobname).split("/")[-1].replace("job", ""))
