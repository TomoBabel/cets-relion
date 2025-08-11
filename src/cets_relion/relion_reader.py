from gemmi import cif
from collections import namedtuple
import networkx as nx
from pathlib import Path
import matplotlib.pyplot as plt
import random
from typing import Optional, Tuple, List

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

    def __init__(self, pipeline_file: str) -> None:
        """Instantiate a RelionPipeline object

        Args:
             pipeline_file (str): Path to the default_pipeliner.star file
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
            G.add_node(job[0], type="process", relion_type=job[2])
            jobs_graph.add_node(job[0], type="process", relion_type=job[2])

        # create file nodes from pipeliner 'nodes'
        nodes_block = self.data.find_block(PIPELINE_BLOCK.nodes)
        pipe_nodes = nodes_block.find(
            prefix="_rlnPipeLineNode", tags=["Name", "TypeLabel"]
        )
        for pipe_node in pipe_nodes:
            split = pipe_node[1].split(".")
            kwds = [] if len(split) <= 2 else split[2:]
            G.add_node(
                pipe_node[0],
                type="file",
                relion_type=split[0],
                file_type=split[1],
                kwds=kwds,
            )
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
        if inputs_block:
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
        if outputs_block:
            out_edges = outputs_block.find(
                prefix="_rlnPipeLine", tags=["EdgeProcess", "EdgeToNode"]
            )

            for edge in out_edges:
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
        self, start: str, graph: Optional[nx.DiGraph] = None
    ) -> nx.DiGraph:
        """Return a subgraph tracing a job and all of its upstream parents

        Args:
            start (str): The job or file to start at
            graph (Optional[nx.DiGraph]): Which graph to use. If None it uses the main
                graph

        Returns:
            nx.DiGraph: The subgraph
        """
        graph = self.graph if graph is None else graph
        sub_nodes = nx.ancestors(graph, start) | {start}
        subgraph = graph.subgraph(sub_nodes).copy()
        return subgraph

    def downstream_critical_path(self, start: str, graph: Optional[nx.DiGraph] = None):
        """Return a subgraph tracing a job and all of its downstream children

        Args:
            start (str): The job or file to start at
            graph (Optional[nx.DiGraph]): Which graph to use. If None it uses the main
                graph

        Returns:
            nx.DiGraph: The subgraph
        """
        graph = self.graph if graph is None else graph
        sub_nodes = nx.descendants(graph, start) | {start}
        subgraph = graph.subgraph(sub_nodes).copy()
        return subgraph

    def last_job_of_type(self, start: str, jobtypes: List[str]) -> List[str]:
        """Find the most recent job(s) of a specific type in the workflow

        Args:
            start (str): The job or file to start the search from
            jobtypes (List[str]): The job type(s) to find

        Returns:
            List[str]: The most recent job(s) that match the criteria
        """
        crit_path = self.upstream_critical_path(start)
        found: List[str] = []
        ordered_nodes = list(crit_path)
        ordered_nodes.sort(key=lambda x: get_sort_key(x), reverse=True)
        for node in ordered_nodes:
            preds = crit_path.predecessors(node)
            for pred in preds:
                if self.graph.nodes[pred].get("relion_type") in jobtypes:
                    found.append(str(pred))
            if found:
                break
        return found

    def last_upstream_file_of_type(
        self,
        start: str,
        relion_type: List[str],
        file_type: Optional[List[str]] = None,
        kwds: Optional[List[str]] = None,
    ):
        """Find the most recent files(s) of a specific type in the workflow, working
        backward from the specified job. May return multiple files EG: if the start job
        took multiple inputs of the same file type

        Args:
            start (str): The job or file to start the search from
            relion_type (List[str]): The relion top level node type
            file_type (Optional(List[str]): The file extension, any if None
            kwds (Optional(List[str]): kwds to match, all must be matched, any if None

        Returns:
            List[str]: The most recent file(s) that match the criteria
        """
        crit_path = self.upstream_critical_path(start)
        file_type = [] if file_type is None else file_type
        kwds = [] if kwds is None else kwds
        found: List[str] = []
        ordered_nodes = list(crit_path)
        ordered_nodes.sort(key=lambda x: get_sort_key(x), reverse=True)
        for node in ordered_nodes:
            preds = crit_path.predecessors(node)
            for pred in preds:
                rt_match = self.graph.nodes[pred].get("relion_type") in relion_type
                found_kwds = self.graph.nodes[pred].get("kwds", [])
                kwds_match = all([x in found_kwds for x in kwds])
                ft_match = (
                    True
                    if not file_type
                    else self.graph.nodes[pred].get("file_type") in file_type
                )
                if all([rt_match, kwds_match, ft_match]):
                    found.append(str(pred))
            if found:
                break
        return found

    def next_downstream_file_of_type(
        self,
        start: str,
        relion_type: str = "",
        ext: str = "",
        kwds: Optional[List[str]] = None,
    ):
        kwds = [] if not kwds else kwds
        ds = self.downstream_critical_path(start)
        found_files = []
        for node in ds:
            succesors = ds.successors(node)
            for succ in [x for x in succesors if ds.nodes[x]["type"] == "file"]:
                type_match = (
                    ds.nodes[succ]["relion_type"] == relion_type or not relion_type
                )
                ext_match = ds.nodes[succ]["file_type"] == ext or not ext
                kwds_match = (
                    all([x in ds.nodes[succ]["kwds"] for x in kwds]) or not kwds
                )
                if all([type_match, ext_match, kwds_match]):
                    found_files.append(succ)
            if found_files:
                return found_files

        return found_files


def get_sort_key(node_name: str) -> Tuple[int, int]:
    """Get the keys for sorting multiple nodes associated with the same job

    Returns the criteria that the nodes are sorted on in descending order of
    importance: its depth in the project, job number, and finally name.

    Files come before the jobs that created them, as it's intended for working
    backwards through a project

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


def draw_graph(network: nx.DiGraph, outfile: str):
    """Tool for drawing a visualisation of the graphs

    Args:
        network (nx.DiGraph): The network to draw
        outfile (str): File to write the output

    """

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
