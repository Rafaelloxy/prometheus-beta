import pytest
from src.binary_search import binary_search

def test_basic_search():
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 13) == 6

def test_element_not_found():
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 4) == -1
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 14) == -1

def test_empty_list():
    arr = []
    assert binary_search(arr, 5) == -1

def test_single_element_list():
    arr = [5]
    assert binary_search(arr, 5) == 0
    assert binary_search(arr, 6) == -1

def test_invalid_input():
    with pytest.raises(TypeError):
        binary_search("not a list", 5)
    
    with pytest.raises(ValueError):
        binary_search([5, 3, 1], 3)  # Unsorted list