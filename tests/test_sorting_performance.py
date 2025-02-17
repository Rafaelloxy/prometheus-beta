import pytest
import random
from src.sorting_performance import compare_sorting_algorithms, bubble_sort, quick_sort

def test_sorting_performance_comparison():
    # Generate a random input list
    input_list = [random.randint(1, 1000) for _ in range(100)]
    
    # Compare bubble sort and quick sort
    result = compare_sorting_algorithms(bubble_sort, quick_sort, input_list)
    
    # Verify result structure
    assert isinstance(result, dict)
    assert "algorithm1_time" in result
    assert "algorithm2_time" in result
    assert "faster_algorithm" in result
    assert "performance_difference" in result
    assert "sorted_list1" in result
    assert "sorted_list2" in result
    
    # Check sorting correctness
    assert result["sorted_list1"] == sorted(input_list)
    assert result["sorted_list2"] == sorted(input_list)
    
    # Performance metrics validation
    assert result["algorithm1_time"] >= 0
    assert result["algorithm2_time"] >= 0
    assert result["performance_difference"] >= 0
    assert result["faster_algorithm"] in ["Algorithm 1", "Algorithm 2"]

def test_performance_comparison_with_large_input():
    # Generate a larger random input list
    input_list = [random.randint(1, 10000) for _ in range(1000)]
    
    # Compare bubble sort and quick sort
    result = compare_sorting_algorithms(bubble_sort, quick_sort, input_list)
    
    # Expect quick sort to be faster for larger lists
    assert result["algorithm2_time"] < result["algorithm1_time"]
    assert result["faster_algorithm"] == "Algorithm 2"

def test_empty_list_handling():
    # Test with an empty list
    input_list = []
    
    result = compare_sorting_algorithms(bubble_sort, quick_sort, input_list)
    
    assert result["sorted_list1"] == []
    assert result["sorted_list2"] == []
    assert result["algorithm1_time"] >= 0
    assert result["algorithm2_time"] >= 0