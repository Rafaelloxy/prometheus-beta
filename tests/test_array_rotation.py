import pytest
from src.array_rotation import rotate_left

def test_basic_rotation():
    """Test basic left rotation"""
    assert rotate_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]

def test_full_rotation():
    """Test rotation equal to array length"""
    assert rotate_left([1, 2, 3], 3) == [1, 2, 3]

def test_partial_rotation():
    """Test partial rotation"""
    assert rotate_left([1, 2, 3, 4], 1) == [2, 3, 4, 1]

def test_zero_rotation():
    """Test zero rotation"""
    assert rotate_left([1, 2, 3], 0) == [1, 2, 3]

def test_rotation_larger_than_length():
    """Test rotation amount larger than array length"""
    assert rotate_left([1, 2, 3], 5) == [1, 2, 3]

def test_empty_array():
    """Test empty array"""
    assert rotate_left([], 2) == []

def test_single_element_array():
    """Test single element array"""
    assert rotate_left([42], 3) == [42]

def test_invalid_input_not_list():
    """Test non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_left("not a list", 2)

def test_invalid_rotation_type():
    """Test non-integer rotation amount raises TypeError"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_left([1, 2, 3], "2")

def test_negative_rotation():
    """Test negative rotation amount raises ValueError"""
    with pytest.raises(ValueError, match="Rotation amount must be non-negative"):
        rotate_left([1, 2, 3], -1)