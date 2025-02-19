import pytest
from src.two_sum import two_sum

def test_two_sum_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_multiple_solutions():
    # When multiple solutions exist, return the first found
    assert two_sum([3, 2, 4], 6) == [1, 2]

def test_two_sum_no_solution():
    assert two_sum([1, 2, 3, 4], 10) == []

def test_two_sum_duplicate_numbers():
    assert two_sum([3, 3], 6) == [0, 1]

def test_two_sum_negative_numbers():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_two_sum_mixed_numbers():
    assert two_sum([-1, 2, 3, 4, -5], -2) == [0, 4]

def test_two_sum_empty_list():
    assert two_sum([], 5) == []

def test_two_sum_zero_target():
    assert two_sum([0, 0], 0) == [0, 1]