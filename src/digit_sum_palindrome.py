def is_digit_sum_palindrome(n: int) -> bool:
    """
    Determine if the sum of digits of a given integer is a palindrome number.

    Args:
        n (int): The input integer.

    Returns:
        bool: True if the sum of digits is a palindrome, False otherwise.
    """
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(abs(n)))
    
    # Convert digit sum to string for palindrome check
    digit_sum_str = str(digit_sum)
    
    # Check if the digit sum is a palindrome
    return digit_sum_str == digit_sum_str[::-1]