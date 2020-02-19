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

def test_breadth_error_value(graph):
    with pytest.raises(ValueError):
        graph.breadth_first('hello there i should be an error')

def test_breadth_functionality(graph):
    rice = graph.add_node('rice')
    spam = graph.add_node('spam')
    end = graph.add_node('end')
    start = graph.add_node('start')
    veggies = graph.add_node('veggies')
    graph.add_edge(start, end, 2)
    graph.add_edge(start, rice, 23)
    graph.add_edge(spam, rice, 420)
    graph.add_edge(end, veggies, 1986)
    graph.add_edge(veggies, spam, 1986)
    expected = [start, end, rice, veggies, spam]
    actual = graph.breadth_first(start)
    assert expected == actual

def test_depth_error_value(graph):
    with pytest.raises(ValueError):
        graph.depth_first('hello there i should be an error')

def test_depth_functionality(graph):
    rice = graph.add_node('rice')
    spam = graph.add_node('spam')
    end = graph.add_node('end')
    start = graph.add_node('start')
    veggies = graph.add_node('veggies')
    graph.add_edge(start, end, 2)
    graph.add_edge(start, rice, 23)
    graph.add_edge(spam, rice, 420)
    graph.add_edge(end, veggies, 1986)
    graph.add_edge(veggies, spam, 1986)
    expected = [start, rice, end, veggies, spam]
    actual = graph.depth_first(start)
    assert expected == actual

def test_test_edge_error_value(graph):
    with pytest.raises(ValueError):
        graph.depth_first('hello there i should be an error') 

