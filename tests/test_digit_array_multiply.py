import pytest
from src.digit_array_multiply import multiply_digit_arrays

def test_basic_multiplication():
    """Test basic multiplication of digit arrays"""
    assert multiply_digit_arrays([1, 2], [3, 4]) == [4, 0, 8]

def test_multiplication_with_zeros():
    """Test multiplication involving zeros"""
    assert multiply_digit_arrays([0, 5], [1, 0]) == [0, 5]

def test_large_numbers():
    """Test multiplication of larger multi-digit numbers"""
    assert multiply_digit_arrays([9, 9], [9, 9]) == [9, 8, 0, 1]

def test_unequal_length_arrays():
    """Test that unequal length arrays raise a ValueError"""
    with pytest.raises(ValueError, match="Input arrays must be of equal length"):
        multiply_digit_arrays([1, 2], [3, 4, 5])

def test_invalid_digits():
    """Test that non-digit inputs raise a ValueError"""
    with pytest.raises(ValueError, match="All elements must be single digits"):
        multiply_digit_arrays([1, 10], [3, 4])
    
    with pytest.raises(ValueError, match="All elements must be single digits"):
        multiply_digit_arrays([1, -1], [3, 4])

def test_single_digit_arrays():
    """Test multiplication of single-digit arrays"""
    assert multiply_digit_arrays([5], [7]) == [3, 5]

def test_zero_multiplication():
    """Test multiplication by zero"""
    assert multiply_digit_arrays([0, 0], [1, 2]) == [0]