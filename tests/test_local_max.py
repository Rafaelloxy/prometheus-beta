import pytest
from src.local_max import find_local_maxima

def test_find_local_maxima_basic():
    """Test basic scenario with local maxima"""
    assert find_local_maxima([1, 3, 2, 4, 1, 5, 3]) == [1, 3, 5]

def test_find_local_maxima_single_element():
    """Test single element list"""
    assert find_local_maxima([42]) == [0]

def test_find_local_maxima_two_elements():
    """Test two elements where first is larger"""
    assert find_local_maxima([5, 3]) == [0]

def test_find_local_maxima_two_elements_reversed():
    """Test two elements where second is larger"""
    assert find_local_maxima([3, 5]) == [1]

def test_find_local_maxima_all_same():
    """Test list with all elements being the same"""
    assert find_local_maxima([1, 1, 1, 1]) == []

def test_find_local_maxima_increasing_sequence():
    """Test strictly increasing sequence"""
    assert find_local_maxima([1, 2, 3, 4, 5]) == [4]

def test_find_local_maxima_decreasing_sequence():
    """Test strictly decreasing sequence"""
    assert find_local_maxima([5, 4, 3, 2, 1]) == [0]

def test_find_local_maxima_multiple_local_maxima():
    """Test multiple local maxima"""
    assert find_local_maxima([1, 3, 2, 4, 1, 5, 3]) == [1, 3, 5]

def test_invalid_input_not_list():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        find_local_maxima("not a list")

def test_invalid_input_empty_list():
    """Test that ValueError is raised for empty list"""
    with pytest.raises(ValueError):
        find_local_maxima([])