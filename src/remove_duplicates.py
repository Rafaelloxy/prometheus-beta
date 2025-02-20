def remove_duplicate_characters(input_string):
    """
    Remove duplicate characters from a lowercase string while preserving order.
    
    Args:
        input_string (str): A lowercase string to remove duplicates from
    
    Returns:
        str: A string with duplicate characters removed, keeping first occurrence
    
    Raises:
        ValueError: If input is not a lowercase string
    """
    # Validate input is a string of lowercase characters
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
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