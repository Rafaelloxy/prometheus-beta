import pytest
from src.radix_sort import radix_sort

def test_radix_sort_normal_case():
    """Test radix sort with a standard list of integers."""
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    assert radix_sort(arr) == [2, 24, 45, 66, 75, 90, 170, 802]

def test_radix_sort_empty_list():
    """Test radix sort with an empty list."""
    assert radix_sort([]) == []

def test_radix_sort_single_element():
    """Test radix sort with a single element."""
    arr = [42]
    assert radix_sort(arr) == [42]

def test_radix_sort_already_sorted():
    """Test radix sort with an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert radix_sort(arr) == [1, 2, 3, 4, 5]

def test_radix_sort_with_duplicates():
    """Test radix sort with duplicate values."""
    arr = [5, 2, 9, 1, 5, 6, 2]
    assert radix_sort(arr) == [1, 2, 2, 5, 5, 6, 9]

def test_radix_sort_negative_input():
    """Test that radix sort raises an error for negative numbers."""
    with pytest.raises(ValueError, match="Radix sort only works with non-negative integers"):
        radix_sort([170, -45, 75, 90])

def test_radix_sort_large_numbers():
    """Test radix sort with large numbers."""
    arr = [1000000, 10, 100000, 1000, 10000]
    assert radix_sort(arr) == [10, 1000, 10000, 100000, 1000000]