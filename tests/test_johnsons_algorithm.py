import pytest
from src.johnsons_algorithm import johnsons_algorithm

def test_basic_graph():
    # Simple graph with positive weights
    graph = {
        0: [(1, 5), (2, 2)],
        1: [(2, 1), (3, 3)],
        2: [(3, 6)],
        3: []
    }
    
    result = johnsons_algorithm(graph)
    
    # Verify shortest paths
    assert result[0][1] == 5  # 0 -> 1
    assert result[0][2] == 2  # 0 -> 2
    assert result[0][3] == 8  # 0 -> 3
    assert result[1][3] == 3  # 1 -> 3
    assert result[2][3] == 6  # 2 -> 3

def test_graph_with_negative_edges():
    # Graph with some negative edge weights
    graph = {
        0: [(1, -1), (2, 4)],
        1: [(2, 3), (3, 2)],
        2: [(3, 5)],
        3: []
    }
    
    result = johnsons_algorithm(graph)
    
    # Verify shortest paths
    assert result[0][1] == -1  # 0 -> 1
    assert result[0][2] == 2   # 0 -> 2
    assert result[0][3] == 1   # 0 -> 3
    assert result[1][3] == 2   # 1 -> 3

def test_negative_cycle():
    # Graph with a negative cycle
    graph = {
        0: [(1, 1)],
        1: [(2, -3)],
        2: [(0, -2)]
    }
    
    result = johnsons_algorithm(graph)
    
    # Verify that a negative cycle returns None
    assert result is None

def test_disconnected_graph():
    # Graph with a disconnected vertex
    graph = {
        0: [(1, 5)],
        1: [(0, 5)],
        2: []
    }
    
    result = johnsons_algorithm(graph)
    
    # Verify paths for connected components
    assert result[0][1] == 5
    assert result[1][0] == 5
    assert 2 not in result[0]
    assert 2 not in result[1]

def test_single_vertex_graph():
    # Graph with only one vertex
    graph = {
        0: []
    }
    
    result = johnsons_algorithm(graph)
    
    # Verify empty result for single vertex
    assert len(result) == 1
    assert len(result[0]) == 0