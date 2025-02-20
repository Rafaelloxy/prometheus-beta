import pytest
from src.list_utils import remove_unique_elements

def test_remove_unique_elements_basic():
    # Test basic functionality
    assert remove_unique_elements([1, 2, 2, 3, 3, 4]) == [2, 3]

def test_remove_unique_elements_empty_list():
    # Test with an empty list
    assert remove_unique_elements([]) == []

def test_remove_unique_elements_no_duplicates():
    # Test with a list with no duplicates
    assert remove_unique_elements([1, 2, 3, 4]) == []

def test_remove_unique_elements_all_duplicates():
    # Test with a list where all elements are duplicates
    assert remove_unique_elements([1, 1, 1, 1]) == [1]

def test_remove_unique_elements_mixed_duplicates():
    # Test with a more complex list of duplicates
    assert remove_unique_elements([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]) == [2, 3, 4]