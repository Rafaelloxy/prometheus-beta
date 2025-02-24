def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a contiguous subarray with length k.

    Args:
        arr (list): A list of integers.
        k (int): The length of the subarray.

    Returns:
        int: The maximum sum of a contiguous subarray of length k.

    Raises:
        ValueError: If k is greater than the length of the array or k is not a positive integer.
    """
    # Validate input
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer")
    
    if k > len(arr):
        raise ValueError("k cannot be greater than the length of the array")
    
    # Special case: if array is empty
    if not arr:
        return 0
    
    # Initial window sum
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Sliding window approach
    for i in range(k, len(arr)):
        # Remove the first element of previous window and add the new element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum