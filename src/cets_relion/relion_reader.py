from __future__ import annotations

import os
from pathlib import Path
from typing import Optional, Tuple, List, Union, Literal, Hashable, Any
from dataclasses import dataclass
import networkx as nx
from gemmi import cif
from cets_relion.utils import get_job_number


@dataclass()
class StarKeys:
    general_block = "pipeline_general"
    job_counter = "_rlnPipeLineJobCounter"
    process_block = "pipeline_processes"
    process_prefix = "_rlnPipeLineProcess"
    process_suffix = ["Name", "Alias", "TypeLabel", "StatusLabel"]
    node_block = "pipeline_nodes"
    node_prefix = "_rlnPipeLineNode"
    node_suffixes = ["Name", "TypeLabel"]
    input_edge_block = "pipeline_input_edges"
    input_edge_prefix = "_rlnPipeLineEdge"
    input_edge_suffixes = ["FromNode", "Process"]
    output_edge_block = "pipeline_output_edges"
    output_edge_prefix = "_rlnPipeLineEdge"
    output_edge_suffixes = ["Process", "ToNode"]


class RelionPipeline(object):
    """An object for reading a RELION pipeline file into a nx networkx
    Attributes:
        graph (networkx.DiGraph):  A bipartate directed graph (BDG) with two types of
            nodes; files and jobs
        next_job_number (int): The number that will be given to the next job added to
            the workflow
    """

    def __init__(
        self,
        pipeline_file: Union[str, os.PathLike] = "",
        from_graph: Optional[nx.Graph[Hashable | Any]] = None,
    ) -> None:
        """Instantiate a RelionPipeline object

        Args:
             pipeline_file (str): Path to the default_pipeliner.star file
             from_graph (Optional[networkx.DiGraph]): Create from a nx.DiGraph object
                rather than reading a file
        """
        super().__init__()
        G: nx.DiGraph = nx.DiGraph()

        # caches to prevent recreating objects
        self._process_cache: List[str] = []
        self._file_cache: List[str] = []
        self.next_job_number = 1
        if not pipeline_file and from_graph is None:
            self.graph = G
            return
        elif from_graph is not None:
            if pipeline_file:
                raise ValueError(
                    "Both graph and pipeline file are specified, use only one"
                )
            self.graph = from_graph
            return

        data = cif.read_file(str(pipeline_file))

        # get the next job number
        gen_block = data.find_block(StarKeys.general_block)
        job_counter = gen_block.find_value(StarKeys.job_counter)
        self.next_job_number = int(job_counter)

        # add Process obj for each job as a process node on the network
        jobs_block = data.find_block(StarKeys.process_block)
        jobs = jobs_block.find(
            tags=[
                "_rlnPipeLineProcessName",
                "_rlnPipeLineProcessTypeLabel",
                "_rlnPipeLineProcessStatusLabel",
                "_rlnPipeLineProcessAlias",
            ]
        )
        for job in jobs:
            G.add_node(
                cif.as_string(job[0]),
                type="process",
                relion_type=cif.as_string(job[1]),
                status=cif.as_string(job[2]),
                alias=cif.as_string(job[3]),
            )

        # create file nodes from pipeliner 'nodes'
        nodes_block = data.find_block(StarKeys.node_block)
        pipe_nodes = nodes_block.find(
            prefix="_rlnPipeLineNode", tags=["Name", "TypeLabel"]
        )
        for pipe_node in pipe_nodes:
            split = cif.as_string(pipe_node[1]).split(".")
            kwds = [] if len(split) <= 2 else split[2:]
            G.add_node(
                cif.as_string(pipe_node[0]),
                type="file",
                relion_type=cif.as_string(split[0]),
                file_type=cif.as_string(split[1]),
                kwds=kwds,
            )

        # add network edges
        all_edges = []

        inputs_block = data.find_block(StarKeys.input_edge_block)
        if inputs_block:
            in_edges = inputs_block.find(
                prefix="_rlnPipeLine", tags=["EdgeFromNode", "EdgeProcess"]
            )

            for edge in in_edges:
                parent_proc = str(Path(cif.as_string(edge[0])).parent) + "/"
                child_proc = cif.as_string(edge[1])
                all_edges.extend(
                    [
                        (parent_proc, cif.as_string(edge[0])),
                        (cif.as_string(edge[0]), child_proc),
                    ]
                )

        outputs_block = data.find_block(StarKeys.output_edge_block)
        if outputs_block:
            out_edges = outputs_block.find(
                prefix="_rlnPipeLine", tags=["EdgeProcess", "EdgeToNode"]
            )

            for edge in out_edges:
                all_edges.append((cif.as_string(edge[0]), cif.as_string(edge[1])))

        G.add_edges_from(all_edges)
        self.graph = G

    def subpipeline(self, subgraph_type: Literal["process", "file"]) -> nx.DiGraph:
        """
        Extract a subgraph of the workflow of containing just processes or files.

        Don't use this method directly. Use self.process_layer() or self.file_layer()

        Args:
            subgraph_type (Literal["process", "file"]): Should the subgraph contain
                process nodes or file nodes?

        Returns:
            networkx.DiGraph: The subgraph
        """
        subgraph: nx.DiGraph = nx.DiGraph()
        oppo_type = "file" if subgraph_type == "process" else "process"

        # First, add all nodes to the new graph
        for node, data in self.graph.nodes(data=True):
            if data.get("type") == subgraph_type:
                subgraph.add_node(node, **data)

        # Then, look for edges of the form process -> file -> process
        for file_node, data in self.graph.nodes(data=True):
            if data.get("type") != oppo_type:
                continue

            # Get predecessors (processes that wrote to this file)
            predecessors = [
                n
                for n in self.graph.predecessors(file_node)
                if self.graph.nodes[n].get("type") == subgraph_type
            ]

            # Get successors (processes that read from this file)
            successors = [
                n
                for n in self.graph.successors(file_node)
                if self.graph.nodes[n].get("type") == subgraph_type
            ]

            # Add input and output edges to the new graph
            for p1 in predecessors:
                for p2 in successors:
                    subgraph.add_edge(p1, p2)

        return subgraph

    def upstream_critical_path(self, start: str) -> RelionPipeline:
        """Return a RelionPipeline tracing a job and all of its upstream parent nodes

        Args:
            start (str): The job or file to start at

        Returns:
            RelionPipeline: RelionPipeline object for the upstream path
        """
        sub_nodes = nx.ancestors(self.graph, start) | {start}
        subgraph = self.graph.subgraph(sub_nodes).copy()

        # add output nodes that aren't directly a part of the subgraph
        for node in list(subgraph.nodes):
            if subgraph.nodes[node] and subgraph.nodes[node]["type"] == "process":
                for outfile in self.graph.successors(node):
                    if (
                        outfile not in [list(subgraph.nodes)]
                        and self.graph.nodes[outfile]["type"] == "file"
                    ):
                        outnode = self.graph.nodes[outfile]
                        subgraph.add_node(outfile, **outnode)
                        subgraph.add_edge(node, outfile)
        return RelionPipeline(from_graph=subgraph)

    def downstream_critical_path(self, start: str) -> RelionPipeline:
        """Return a subgraph tracing a job and all of its downstream children

        Args:
            start (str): The job or file to start at

        Returns:
            RelionPipeline: RelionPipeline object for the downstream path
        """
        sub_nodes = nx.descendants(self.graph, start) | {start}
        subgraph = self.graph.subgraph(sub_nodes).copy()

        # add output nodes that aren't directly a part of the subgraph
        for node in list(subgraph.nodes):
            if subgraph.nodes[node]["type"] == "process":
                for outfile in self.graph.successors(node):
                    if (
                        outfile not in [list(subgraph.nodes)]
                        and self.graph.nodes[outfile]["type"] == "file"
                    ):
                        outnode = self.graph.nodes[outfile]
                        subgraph.add_node(outfile, **outnode)
                        subgraph.add_edge(node, outfile)
        return RelionPipeline(from_graph=subgraph)

    def process_layer(self) -> RelionPipeline:
        """Get a RelionPipeline object for just the processes of a workflow

        If the self.process or self.find_process methods are used on this object
        input_nodes and output_nodes in the Process objects returned
        will be empty

        """
        return RelionPipeline(from_graph=self.subpipeline("process"))

    def files_layer(self) -> RelionPipeline:
        """Get a RelionPipeline object for just the files in a workflow

        If the self.file or self.find_file methods are used on this object
        input_to_processes_list and output_from_process in the Node objects returned
        will be empty

        Returns: RelionPipeline: With just the file nodes.
        """
        return RelionPipeline(from_graph=self.subpipeline("file"))

    def next_upstream_jobs(
        self, start: str, jobtypes: Optional[List[str]] = None
    ) -> List[str]:
        """Find the next upstream job(s) from a specific job in the workflow

        Follows all upstream branches separately until it finds a job that matches the
        search criteria for that branch.

        Args:
            start (str): The job or file to start the search from
            jobtypes (Optional[List[str]]): The job type(s) to find, if None if finds
                the next upstream jobs

        Returns:
            List[str]: The most recent job(s) from upstream branches that match the
            criteria
        """
        found_nodes = set()
        visited = set()
        jobtypes = [] if jobtypes is None else jobtypes

        def node_visited(node: str, initial: bool = True) -> None:
            """Check that a node has already been visited"""
            if node in visited:
                return
            visited.add(node)

            if self.graph.nodes[node].get("relion_type") in jobtypes or (
                jobtypes == []
                and not initial
                and self.graph.nodes[node]["type"] == "process"
            ):
                found_nodes.add(node)
                return

            for pred in self.graph.predecessors(node):
                node_visited(pred, initial=False)

        node_visited(start)
        nodes = list(found_nodes)
        nodes.sort(key=lambda x: get_sort_key(x))
        return nodes

    def next_downstream_jobs(
        self, start: Union[str, os.PathLike], jobtypes: Optional[List[str]] = None
    ) -> List[str]:
        """Find the next downstream job(s) from a specific job in the workflow

        Follows all downstream branches separately until it finds a job that satisfies
        the search criteria for that branch.

        Args:
            start (str): The job or file to start the search from
            jobtypes (List[str]): The job type(s) to find

        Returns:
            List[str]: The most recent job(s) from upstream branches that match the
            criteria
        """
        found_nodes = set()
        visited = set()
        jobtypes = [] if jobtypes is None else jobtypes

        def dfs(node, initial=True):
            if node in visited:
                return
            visited.add(node)

            if self.graph.nodes[node].get("relion_type") in jobtypes or (
                jobtypes == []
                and not initial
                and self.graph.nodes[node]["type"] == "process"
            ):
                found_nodes.add(node)
                return

            for succ in self.graph.successors(node):
                dfs(succ, initial=False)

        dfs(start)
        nodes = list(found_nodes)
        nodes.sort(key=lambda x: get_sort_key(x))
        return nodes

    def next_upstream_files(
        self,
        start: Union[str, os.PathLike],
        relion_type: Optional[List[str]] = None,
        ext: Optional[List[str]] = None,
        kwds: Optional[List[str]] = None,
    ):
        """Find the closest upstream files(s) from a starting point

        Follows all upstream branches separately until it finds a file that satisfies
        the search criteria for that branch. May return multiple files for a branch EG:
        if a job had multiple inputs/outputs of the same file type

        Args:
            start (str): The job or file to start the search from
            relion_type (List[str]): The RELION top level node type
            ext (Optional[List[str]]): The file extension, any if None
            kwds (Optional[List[str]]): kwds to match, all must be matched, any if None

        Returns:
            List[str]: The most recent file(s) that match the criteria
        """
        found_nodes = set()
        visited = set()
        relion_type = [] if relion_type is None else relion_type
        ext = [] if ext is None else ext
        kwds = [] if kwds is None else kwds

        def dfs(node, initial=True):
            if node in visited:
                return
            visited.add(node)

            rt_match = self.graph.nodes[node].get("relion_type") in relion_type or (
                relion_type == [] and not initial
            )
            found_kwds = self.graph.nodes[node].get("kwds", [])
            kwds_match = all([x in found_kwds for x in kwds])
            ft_match = (
                True if not ext else self.graph.nodes[node].get("file_type") in ext
            )
            if all([rt_match, kwds_match, ft_match]):
                found_nodes.add(node)
                return

            for pred in self.graph.predecessors(node):
                dfs(pred, initial=False)

        dfs(start)
        nodes = list(found_nodes)
        nodes.sort(key=lambda x: get_sort_key(x))
        return nodes

    def next_downstream_files(
        self,
        start: Union[str, os.PathLike],
        relion_type: Optional[List[str]] = None,
        ext: Optional[List[str]] = None,
        kwds: Optional[List[str]] = None,
    ):
        """Find the next downstream files(s) from a starting point

        Follows all downstream branches separately until it finds a file that satisfies
        the search criteria for that branch. May return multiple files for a branch EG:
        if a job took multiple inputs/outputs of the same file type

        Args:
            start (str): The job or file to start the search from
            relion_type (List[str]): The RELION top level node type
            ext (Optional[List[str]]): The file extension, any if None
            kwds (Optional[List[str]]): kwds to match, all must be matched, any if None

        Returns:
            List[str]: The most recent file(s) that match the criteria
        """
        found_nodes = set()
        visited = set()
        relion_type = [] if relion_type is None else relion_type
        ext = [] if ext is None else ext
        kwds = [] if kwds is None else kwds

        def dfs(node, initial=True):
            if node in visited:
                return
            visited.add(node)

            rt_match = (
                self.graph.nodes[node].get("relion_type") in relion_type
                or relion_type == []
                and not initial
            )
            found_kwds = self.graph.nodes[node].get("kwds", [])
            kwds_match = all([x in found_kwds for x in kwds])
            ft_match = (
                True if not ext else self.graph.nodes[node].get("file_type") in ext
            )
            if all([rt_match, kwds_match, ft_match]):
                found_nodes.add(node)
                return

            for succ in self.graph.successors(node):
                dfs(succ, initial=False)

        dfs(start)
        nodes = list(found_nodes)
        nodes.sort(key=lambda x: get_sort_key(x))
        return nodes


def get_sort_key(node_name: Union[str, os.PathLike]) -> Tuple[int, int]:
    """Get the keys for sorting multiple nodes associated with the same job

    Nodes are sorted on (in descending order of importance) its depth in the project,
    job number, and finally name.

    Files come before the jobs that created them, as it's intended for working
    backwards through a project

    Args:
        node_name (Union[str, os.PathLike]): The node name; a job or a file

    Returns:
        Tuple[int, int]: (job number, depth)

    """
    node_name = str(node_name)
    try:
        job_num = get_job_number(node_name)
        depth = 0 if Path(node_name).is_dir() == "" else 1
    except Exception:
        return 0, 0
    return job_num, depth
