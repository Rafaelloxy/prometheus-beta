def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within a given array of integers.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Kadane's algorithm
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new subarray
        current_sum = max(num, current_sum + num)
        
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum