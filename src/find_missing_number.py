def find_missing_number(nums):
    """
    Find the missing number in a list of integers from 1 to n.
    
    Args:
        nums (list): A list of integers from 1 to n with one number missing.
    
    Returns:
        int: The missing number.
    
    Raises:
        ValueError: If the input list is empty or invalid.
    """
    # Check for invalid input
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the expected sum of numbers from 1 to n
    n = len(nums) + 1
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given list
    actual_sum = sum(nums)
    
    # The missing number is the difference between expected and actual sum
    return expected_sum - actual_sum