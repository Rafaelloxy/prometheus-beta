def rotate_left(arr, n):
    """
    Rotate an array to the left by n positions.
    
    Args:
        arr (list): The input array to be rotated
        n (int): Number of positions to rotate left
    
    Returns:
        list: A new array rotated to the left
    
    Raises:
        TypeError: If input is not a list or n is not an integer
        ValueError: If n is negative
    """
    # Validate input types
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(n, int):
        raise TypeError("Rotation amount must be an integer")
    
    # Handle empty or single-element arrays
    if len(arr) <= 1:
        return arr.copy()
    
    # Handle negative rotations
    if n < 0:
        raise ValueError("Rotation amount must be non-negative")
    
    # Normalize rotation amount to avoid unnecessary full rotations
    n = n % len(arr)
    
    # Perform rotation
    return arr[n:] + arr[:n]