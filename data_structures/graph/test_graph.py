import pytest
from graph import Graph, Vertex


@pytest.fixture
def graph():
    return Graph()


def test_add_node(graph):
    expected = 'spam'
    actual = graph.add_node('spam').value
    assert actual == expected

def test_size_empty(graph):
    expected = 0
    actual = graph.size()
    assert actual == expected

def test_size(graph):
    graph.add_node('spam')
    expected = 1
    actual = graph.size()
    assert actual == expected

def test_add_edge_interloper_start(graph):
    start = Vertex('start')
    end = graph.add_node('end')
    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_add_edge_interloper_end(graph):
    end = Vertex('end')
    start = graph.add_node('start')
    with pytest.raises(KeyError):
        graph.add_edge(start, end)

def test_get_nodes(graph):
    graph.add_node('banana')
    graph.add_node('apple')
    Vertex('loner')
    expected = 2
    actual = len(graph.get_nodes())
    assert actual == expected
