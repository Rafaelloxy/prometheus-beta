import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4]) == 10

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_numbers():
    """Test with all negative numbers, return the largest number."""
    assert max_subarray_sum([-1, -2, -3]) == -1

def test_single_element():
    """Test with a single element array."""
    assert max_subarray_sum([42]) == 42

def test_alternating_signs():
    """Test with alternating positive and negative numbers."""
    assert max_subarray_sum([1, -1, 2, -2, 3]) == 3

def test_zero_elements():
    """Test with zero elements."""
    assert max_subarray_sum([0, 0, 0]) == 0

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum(123)
    
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum(None)