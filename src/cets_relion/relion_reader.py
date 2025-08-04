from gemmi import cif
from collections import namedtuple
from os import PathLike
import networkx as nx
from pathlib import Path
import matplotlib.pyplot as plt
import random
from typing import Optional, Tuple

# definitions for the names of blocks in the RELION pipeline cif file
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
    """An object for reading a RELION pipeline file into networkx
    Attrs:
        graph (nx.DiGraph):  a directed acyclic graph (DAG) with two types of nodes:
            files and jobs
        jobs_graph (nx.DiGraph):A DAG with just the jobs
        files_graph (nx.DiGraph): A DAG with just the files
    """

    def __init__(self, pipeline_file: PathLike) -> None:
        """Instantiate a RelionPipeline object

        Args:
             pipeline_file (PathLike): Path to the default_pipeliner.star file
        """
        self.data = cif.read_file(str(pipeline_file))

        # a Directed graph objects for the pipeline
        G = nx.DiGraph()
        jobs_graph = nx.DiGraph()
        files_graph = nx.DiGraph()

        # add Process obj for each job as a node on the network
        jobs_block = self.data.find_block(PIPELINE_BLOCK.processes)
        jobs = jobs_block.find(
            tags=[
                "_rlnPipeLineProcessName",
                "_rlnPipeLineProcessAlias",
                "_rlnPipeLineProcessTypeLabel",
                "_rlnPipeLineProcessStatusLabel",
            ]
        )
        for job in jobs:
            G.add_node(job[0], type="process")
            jobs_graph.add_node(job[0], type="process")

        # create file nodes from pipeliner 'nodes'
        nodes_block = self.data.find_block(PIPELINE_BLOCK.nodes)
        pipe_nodes = nodes_block.find(
            prefix="_rlnPipeLineNode", tags=["Name", "TypeLabel"]
        )
        for pipe_node in pipe_nodes:
            split = pipe_node[1].split(".")
            kwds = [] if len(split) <= 2 else split[2:]
            G.add_node(pipe_node[0], type="file")
            files_graph.add_node(
                pipe_node[0],
                type="file",
                relion_type=split[0],
                file_type=split[1],
                kwds=kwds,
            )

        # add network edges
        all_edges = []

        inputs_block = self.data.find_block(PIPELINE_BLOCK.inputs)
        in_edges = inputs_block.find(
            prefix="_rlnPipeLine", tags=["EdgeFromNode", "EdgeProcess"]
        )

        for edge in in_edges:
            parent_proc = str(Path(edge[0]).parent) + "/"
            child_proc = edge[1]
            all_edges.extend(
                [
                    [parent_proc, edge[0]],
                    [edge[0], child_proc],
                ]
            )

        outputs_block = self.data.find_block(PIPELINE_BLOCK.outputs)
        out_edges = outputs_block.find(
            prefix="_rlnPipeLine", tags=["EdgeProcess", "EdgeToNode"]
        )

        for edge in out_edges:
            print(edge[0], "->", edge[1])
            all_edges.append([edge[0], edge[1]])
        G.add_edges_from(all_edges)

        self.graph = G

        # add the edges to jobs graph
        for job in jobs:
            outputs = self.graph.successors(job[0])
            for outfile in outputs:
                children = self.graph.successors(outfile)
                for child_job in children:
                    jobs_graph.add_edge(job[0], child_job)

        self.jobs_graph = jobs_graph

        # add the edges to files graph
        for file in pipe_nodes:
            inputs_to = self.graph.successors(file[0])
            for recipient in inputs_to:
                children = self.graph.successors(recipient)
                for ds_file in children:
                    files_graph.add_edge(file[0], ds_file)
            outputs_from = self.graph.predecessors(file[0])
            for parent in outputs_from:
                parent_files = self.graph.predecessors(parent)
                for parent_file in parent_files:
                    files_graph.add_edge(parent_file, file[0])

        self.files_graph = files_graph

    def upstream_critical_path(
        self, start: PathLike, graph: Optional[nx.DiGraph] = None
    ) -> nx.DiGraph:
        """Return a subgraph tracing a job and all of its upstream parents

        Args:
            start (PathLike): The job or file to start at
            graph (Optional[nx.DiGraph]): Which graph to use. If None it uses the main
                graph

        Returns:
            nx.DiGraph: The subgraph
        """
        graph = self.graph if graph is None else graph
        startstr = str(start)
        sub_nodes = nx.ancestors(graph, startstr) | {startstr}
        subgraph = graph.subgraph(sub_nodes).copy()
        return subgraph

    def downstream_critical_path(
        self, start: PathLike, graph: Optional[nx.DiGraph] = None
    ):
        """Return a subgraph tracing a job and all of its downstream children

        Args:
            start (PathLike): The job or file to start at
            graph (Optional[nx.DiGraph]): Which graph to use. If None it uses the main
                graph

        Returns:
            nx.DiGraph: The subgraph
        """
        graph = self.graph if graph is None else graph
        startstr = str(start)
        sub_nodes = nx.descendants(graph, startstr) | {startstr}
        subgraph = graph.subgraph(sub_nodes).copy()
        return subgraph


def draw_graph(network: nx.DiGraph, outfile: str):
    """Tool for drawing a visualisation of the graphs

    Args:
        network (nx.DiGraph): The network to draw
        outfile (str): File to write the output

    """

    def get_sort_key(node_name: str) -> Tuple[int, int]:
        """Get the keys for sorting multiple nodes associated with the same job

        Returns the criteria that the nodes are sorted on in descending order of
        importance: its depth in the project, job number, and finally name.

        Args:
            node_name (str): The node name, a job or a file

        Returns:
            Tuple[int, int]: (job number, depth)

        """
        parts = node_name.split("/")
        try:
            job_num = int(parts[1].replace("job", ""))
            depth = 0 if parts[-1] == "" else 1
        except Exception:
            return 0, 0
        return job_num, depth

    def get_x_pos(node_name, ngraph, is_jobs) -> float:
        """Get the x position of a node in the graph image

        Side is assigned randomly, The more children a node has the further to the side
        it is. This makes it easy to visualize.

        Args:
            node_name (str): Name of the node
            ngraph (nx.DiGraph): The graph that holds the node
            is_jobs (bool): Does the graph contain only jobs and no files?

        Returns:
             int: The x position of the object in the graph image
        """
        if node_name.split("/")[-1] == "" and not is_jobs:
            return 0
        outedges = [x[1] for x in ngraph.out_edges(node_name)]
        parents = list(ngraph.predecessors(node_name))
        flip = random.choice([1, -1])

        if parents:
            siblings = list(ngraph.successors(parents[0]))
            nindex = siblings.index(node_name)
            flip = flip if not nindex % 2 else flip * -1
        if len(ngraph.out_edges(node_name)) == 1:
            return SPACING * flip
        else:
            return len(outedges) * SPACING * flip

    SPACING = 0.25
    ordered_nodes = list(network.nodes())
    ordered_nodes.sort(key=lambda x: get_sort_key(x))
    file_nodes = [
        n for n, attrs in network.nodes(data=True) if attrs.get("type") == "file"
    ]
    file_nodes.sort(key=lambda x: get_sort_key(x))
    pos = {
        node: (
            get_x_pos(node, network, is_jobs=file_nodes == []),
            (len(ordered_nodes) - i) * SPACING,
        )
        for i, node in enumerate(ordered_nodes)
    }

    # Separate node types
    file_nodes = [n for n, d in network.nodes(data=True) if d.get("type") == "file"]
    job_nodes = [n for n, d in network.nodes(data=True) if d.get("type") == "process"]

    nx.draw_networkx_edges(network, pos, arrows=True, width=0.25, arrowsize=5)

    # Draw file nodes as circles
    nx.draw_networkx_nodes(
        network,
        pos,
        nodelist=file_nodes,
        node_shape="o",  # circle
        node_color="lightblue",
        node_size=50,
        label="File",
    )

    # Draw job nodes as squares
    nx.draw_networkx_nodes(
        network,
        pos,
        nodelist=job_nodes,
        node_shape="s",  # square
        node_color="red",
        node_size=50,
        label="Job",
    )

    # Draw labels
    nx.draw_networkx_labels(network, pos, font_size=4, font_color="black")

    plt.savefig(outfile, format="png", dpi=300)
    plt.close()
