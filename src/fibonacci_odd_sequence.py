def generate_odd_fibonacci_sequence(n):
    """
    Generate a Fibonacci sequence of length n containing only odd numbers.
    
    Args:
        n (int): Non-negative integer representing the length of the sequence.
    
    Returns:
        list: A list of n odd Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Length of sequence must be a non-negative integer")
    
    # Special case handling for small sequences
    if n == 0:
        return []
    if n == 1:
        return [1]
    
    # Initialize the sequence with the first two odd Fibonacci numbers
    sequence = [1, 1]
    
    # Generate subsequent odd Fibonacci numbers
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    
    return sequence