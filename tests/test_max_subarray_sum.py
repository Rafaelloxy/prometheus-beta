import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_functionality():
    """Test basic functionality with a normal input."""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_all_positive_numbers():
    """Test with an array of all positive numbers."""
    arr = [5, 3, 7, 2, 9, 1, 6]
    k = 3
    assert max_subarray_sum(arr, k) == 18  # 7 + 2 + 9 = 18

def test_array_with_negative_numbers():
    """Test with an array containing negative numbers."""
    arr = [-1, 4, -2, 3, -4, 5, 6, -5, 1]
    k = 3
    assert max_subarray_sum(arr, k) == 7  # 5 + 6 + (-5) = 6

def test_single_element_array():
    """Test with a single element array."""
    arr = [42]
    k = 1
    assert max_subarray_sum(arr, k) == 42

def test_invalid_k_greater_than_array():
    """Test when k is greater than array length."""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k cannot be greater than the length of the array"):
        max_subarray_sum(arr, 4)

def test_empty_array():
    """Test with an empty array."""
    arr = []
    with pytest.raises(ValueError, match="k cannot be greater than the length of the array"):
        max_subarray_sum(arr, 1)

def test_invalid_k_zero():
    """Test with k = 0."""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum(arr, 0)

def test_invalid_k_negative():
    """Test with negative k."""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be a positive integer"):
        max_subarray_sum(arr, -2)

def test_k_equal_to_array_length():
    """Test when k is equal to the array length."""
    arr = [1, 2, 3, 4]
    assert max_subarray_sum(arr, 4) == 10