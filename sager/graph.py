from datetime import datetime
import json

from sage.all import DiGraph
from sage.all import Graph


def create_graph(data, vertex_getter, edge_getter, directed=False):
    """Construct a directed or undirected graph for the provided data. The
    vertex_getter is a callable which takes a single argument and returns the
    name of a vertex, and edge_getter is a callable which takes a single
    argument and returns a list of adjacencies.
    """

    data = {vertex_getter(node): edge_getter(node) for node in data}

    return DiGraph(data) if directed else Graph(data)


def load_graph(json_file, directed=False):
    """Load a directed or undirected graph from the provided file containing
    JSON data in the following form:
        [
            {"v_name": ["v_neighbor_1", "v_neighbor_2"]},
            ...
        ]
    """

    data = ''

    with open(json_file, 'r') as json_file:
        data = json.loads(json_file.read())

    return DiGraph(data) if directed else Graph(data)


def dump_graph(data, vertex_getter, edge_getter, filename=None):
    """Dump the data to a file in JSON format. The vertex_getter is a callable
    which takes a single argument and returns the name of a vertex, and
    edge_getter is a callable which takes a single argument and returns a list
    of adjacencies. Return the name of the file that was written.
    """

    if not filename:
        filename = '%s.txt' % datetime.now().strftime('%m-%d-%Y_%H-%M-%S')

    data = {vertex_getter(node): edge_getter(node) for node in data}

    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(data))

    return filename

