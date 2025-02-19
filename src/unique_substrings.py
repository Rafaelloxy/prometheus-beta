def get_unique_substrings(input_string):
    """
    Takes a string as input and returns an array of all unique substrings.
    
    Args:
        input_string (str): The input string to generate substrings from.
    
    Returns:
        list: A list of unique substrings.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        return []
    
    unique_substrings = set()
    
    # Generate all possible substrings
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            unique_substrings.add(input_string[i:j])
    
    return list(unique_substrings)