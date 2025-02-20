def remove_duplicate_chars(input_string):
    """
    Remove duplicate characters from the input string while preserving the original order.
    
    Args:
        input_string (str): A lowercase string to remove duplicates from.
    
    Returns:
        str: A string with duplicate characters removed, keeping the first occurrence.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input contains non-lowercase characters.
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Check input contains only lowercase characters
    if not input_string.islower():
        raise ValueError("Input must contain only lowercase characters")
    
    # Use a set to track seen characters while preserving order
    seen = set()
    result = []
    
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)