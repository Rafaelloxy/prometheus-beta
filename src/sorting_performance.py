import time
import logging
import random
from typing import List, Callable

def compare_sorting_algorithms(
    algorithm1: Callable[[List[int]], List[int]], 
    algorithm2: Callable[[List[int]], List[int]], 
    input_list: List[int]
) -> dict:
    """
    Compare the performance of two sorting algorithms.
    
    Args:
        algorithm1 (callable): First sorting algorithm to compare
        algorithm2 (callable): Second sorting algorithm to compare
        input_list (list): List of integers to be sorted
    
    Returns:
        dict: Performance metrics for both sorting algorithms
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    # Create copies of input list to ensure fair comparison
    list1 = input_list.copy()
    list2 = input_list.copy()
    
    # Measure performance of first algorithm
    start_time1 = time.time()
    sorted_list1 = algorithm1(list1)
    end_time1 = time.time()
    time1 = end_time1 - start_time1
    
    # Measure performance of second algorithm
    start_time2 = time.time()
    sorted_list2 = algorithm2(list2)
    end_time2 = time.time()
    time2 = end_time2 - start_time2
    
    # Log performance metrics
    logger.info(f"Algorithm 1 Execution Time: {time1:.6f} seconds")
    logger.info(f"Algorithm 2 Execution Time: {time2:.6f} seconds")
    
    # Determine faster algorithm
    faster_algorithm = "Algorithm 1" if time1 < time2 else "Algorithm 2"
    performance_difference = abs(time1 - time2)
    
    logger.info(f"Faster Algorithm: {faster_algorithm}")
    logger.info(f"Performance Difference: {performance_difference:.6f} seconds")
    
    return {
        "algorithm1_time": time1,
        "algorithm2_time": time2,
        "faster_algorithm": faster_algorithm,
        "performance_difference": performance_difference,
        "sorted_list1": sorted_list1,
        "sorted_list2": sorted_list2
    }

# Example sorting algorithms for demonstration
def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)