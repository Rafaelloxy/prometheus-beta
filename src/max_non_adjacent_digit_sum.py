def max_non_adjacent_digit_sum(number: int) -> int:
    """
    Find the maximum sum of non-adjacent digits in a positive integer.
    
    A non-adjacent digit sum means selecting digits that are not next to each other
    to maximize the total sum.
    
    Args:
        number (int): A positive integer to analyze
    
    Returns:
        int: Maximum sum of non-adjacent digits
    
    Raises:
        ValueError: If the input is not a positive integer
    
    Examples:
        >>> max_non_adjacent_digit_sum(3241)  # Possible max: 7 (3+4)
        7
        >>> max_non_adjacent_digit_sum(9876)  # Possible max: 15 (9+6)
        15
    """
    # Validate input
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Convert number to string for easy digit manipulation
    digits = [int(d) for d in str(number)]
    n = len(digits)
    
    # Handle small input cases
    if n <= 1:
        return digits[0]
    
    # Initialize dynamic programming array
    dp = [0] * n
    
    # First two digits - take the max
    dp[0] = digits[0]
    dp[1] = max(digits[0], digits[1])
    
    # Build optimal solution
    for i in range(2, n):
        # At each step, we have two choices:
        # 1. Include current digit + max sum two steps back
        # 2. Skip current digit and take max sum from previous step
        dp[i] = max(digits[i] + dp[i-2], dp[i-1])
    
    # Return the maximum sum
    return dp[-1]