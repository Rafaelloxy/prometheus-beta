def multiply_digit_arrays(A, B):
    """
    Multiply two arrays of digits representing numbers.
    
    Args:
        A (list): First array of digits 
        B (list): Second array of digits of the same length
    
    Returns:
        list: Array of digits representing the product of the two input numbers
    
    Raises:
        ValueError: If input arrays are not of equal length or contain non-digit values
    """
    # Validate input
    if len(A) != len(B):
        raise ValueError("Input arrays must be of equal length")
    
    # Validate that all inputs are single digits
    if not all(isinstance(x, int) and 0 <= x <= 9 for x in A + B):
        raise ValueError("All elements must be single digits (0-9)")
    
    # Convert arrays to numbers
    def array_to_number(arr):
        return int(''.join(map(str, arr)))
    
    # Multiply the numbers
    product = array_to_number(A) * array_to_number(B)
    
    # Convert product back to array of digits
    return [int(digit) for digit in str(product)]