import pytest
from src.max_subarray_sum import max_non_overlapping_subarray_sum

def test_positive_array():
    assert max_non_overlapping_subarray_sum([1, 2, 3, 4, 5]) == 9
    assert max_non_overlapping_subarray_sum([-1, 2, 3, -4, 5]) == 7
    assert max_non_overlapping_subarray_sum([1, -1, 2, -1, 3]) == 5

def test_single_element_array():
    assert max_non_overlapping_subarray_sum([5]) == 5
    assert max_non_overlapping_subarray_sum([-3]) == 0

def test_all_negative_array():
    assert max_non_overlapping_subarray_sum([-1, -2, -3]) == 0

def test_empty_array():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_non_overlapping_subarray_sum([])

def test_invalid_input():
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_non_overlapping_subarray_sum("not a list")
        max_non_overlapping_subarray_sum(123)
        max_non_overlapping_subarray_sum(None)