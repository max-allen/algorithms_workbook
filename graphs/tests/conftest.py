import pytest
from graphs import GraphNode, AdjList as Graph


@pytest.fixture
def graph():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("A", "D")
    g.add_edge("B", "E")
    g.add_edge("B", "F")
    g.add_edge("C")
    g.add_edge("D", "G")
    g.add_edge("D", "H")
    g.add_edge("E")
    g.add_edge("F", "I")
    g.add_edge("F", "J")
    g.add_edge("G", "K")
    g.add_edge("H")
    g.add_edge("I")
    g.add_edge("J")
    g.add_edge("K")

    return {
        "fixture": g,
        "dfs_a_expected": ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"],
        "bfs_a_expected": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"],
    }


@pytest.fixture
def flood_fill_color_change():
    return {
        "input": [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
        "start_row": 1,
        "start_col": 1,
        "color": 2,
        "expected": [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
    }


@pytest.fixture
def flood_fill_no_connection():
    return {
        "input": [[0, 0, 0], [0, 0, 0]],
        "start_row": 0,
        "start_col": 0,
        "color": 0,
        "expected": [[0, 0, 0], [0, 0, 0]],
    }


@pytest.fixture
def river_sizes_matrix():
    return {
        "matrix": [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
        ],
        "expected": [2, 1, 5, 2, 2],
    }


@pytest.fixture
def graph_nodes():
    n1 = GraphNode(1)
    n2 = GraphNode(2, [n1])
    n3 = GraphNode(3, [n2])

    return {"n1": n1, "n2": n2, "n3": n3}


@pytest.fixture
def paths():
    return [
        {"foo": "bar"},
        {"bar": "baz"},
        {"qux": "quux"},
        {"corge": "grault"},
        {"garply": "waldo"},
        {"fred": "plugh"},
        {"xyzzy": "thud"},
    ]
