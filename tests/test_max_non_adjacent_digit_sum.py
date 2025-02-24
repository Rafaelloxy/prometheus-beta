import pytest
from src.max_non_adjacent_digit_sum import max_non_adjacent_digit_sum

def test_single_digit():
    """Test single digit input"""
    assert max_non_adjacent_digit_sum(5) == 5

def test_two_digits():
    """Test two digit input"""
    assert max_non_adjacent_digit_sum(42) == 4  # max of 4
    assert max_non_adjacent_digit_sum(24) == 4  # max of 4

def test_multiple_digits():
    """Test various multi-digit inputs"""
    assert max_non_adjacent_digit_sum(3241) == 7  # 3 + 4
    assert max_non_adjacent_digit_sum(9876) == 16  # 9 + 7
    assert max_non_adjacent_digit_sum(1234) == 6  # actual max possible

def test_all_zeros():
    """Test input with all zeros"""
    assert max_non_adjacent_digit_sum(1010) == 2  # 1 + 1

def test_large_number():
    """Test a larger number"""
    assert max_non_adjacent_digit_sum(123456789) == 25  # 1 + 3 + 5 + 7 + 9

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum(0)
    
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum(-123)
    
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum(3.14)
    
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum("123")