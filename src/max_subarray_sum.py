def max_non_overlapping_subarray_sum(arr):
    """
    Calculate the maximum sum of a non-overlapping subarray.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: Maximum sum of a non-overlapping subarray
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    n = len(arr)
    if n == 1:
        return max(0, arr[0])
    
    # Dynamic programming approach
    # dp[i] represents the maximum sum of non-overlapping subarrays ending at index i
    dp = [0] * n
    dp[0] = max(0, arr[0])
    dp[1] = max(dp[0], arr[1], arr[1] + dp[0])
    
    for i in range(2, n):
        # Two choices:
        # 1. Take current element and the best sum from before last index
        # 2. Skip current element and take best previous sum
        dp[i] = max(arr[i] + dp[i-2], dp[i-1])
    
    return dp[n-1]