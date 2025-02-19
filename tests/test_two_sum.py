import pytest
from src.two_sum import two_sum

def test_two_sum_basic():
    """Test basic case with a solution in the array"""
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]

def test_two_sum_end_indices():
    """Test case where solution is at the end of the array"""
    nums = [3, 2, 4]
    target = 6
    assert two_sum(nums, target) == [1, 2]

def test_two_sum_no_solution():
    """Test case where no solution exists"""
    nums = [1, 2, 3, 4]
    target = 10
    assert two_sum(nums, target) == []

def test_two_sum_duplicate_values():
    """Test case with duplicate values"""
    nums = [3, 3]
    target = 6
    assert two_sum(nums, target) == [0, 1]

def test_two_sum_large_numbers():
    """Test case with larger numbers"""
    nums = [230, 863, 916, 585, 981, 404, 316, 785, 88, 12, 70, 435, 384, 778, 887, 755, 740, 337, 86, 92, 325, 422, 815, 650, 920, 125, 277, 336, 221, 847, 168, 23, 677, 61, 400, 136, 874, 363, 394, 199, 863, 997, 794, 587, 124, 321, 212, 957, 764, 173, 314, 422, 927, 783, 930, 282, 306, 506, 44, 926, 691, 568, 68, 730, 933, 737, 531, 180, 414, 751, 28, 546, 60, 371, 493, 370, 527, 387, 43, 541, 13, 457, 328, 227, 652, 365, 430, 803, 59, 858, 538, 427, 583, 368, 375, 173, 809, 896, 370, 789]
    target = 542
    result = two_sum(nums, target)
    assert nums[result[0]] + nums[result[1]] == target