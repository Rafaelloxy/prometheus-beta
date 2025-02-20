import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a typical scenario."""
    assert find_missing_number([1, 2, 4, 5]) == 3

def test_find_missing_number_first_number_missing():
    """Test when the first number is missing."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_find_missing_number_last_number_missing():
    """Test when the last number is missing."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_large_set():
    """Test with a larger set of numbers."""
    nums = list(range(1, 11))
    nums.remove(7)
    assert find_missing_number(nums) == 7

def test_find_missing_number_invalid_input():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_missing_number([])