def calculate_variance(numbers):
    """
    Calculate the variance of a list of numbers.
    
    Args:
        numbers (list): A list of numbers to calculate variance for.
    
    Returns:
        float: The variance of the input numbers.
    
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input contains non-numeric values.
    """
    if not numbers:
        raise ValueError("Cannot calculate variance of an empty list")
    
    # Validate input is numeric
    try:
        numbers = [float(num) for num in numbers]
    except (TypeError, ValueError):
        raise TypeError("All elements must be numeric")
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate variance (average of squared differences from mean)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    
    return variance