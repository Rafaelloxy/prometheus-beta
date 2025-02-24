def count_a_occurrences(input_string: str) -> int:
    """
    Count the number of times the character 'a' appears in the given string, 
    ignoring case sensitivity.

    Args:
        input_string (str): The input string to search for 'a' characters.

    Returns:
        int: The number of 'a' or 'A' characters in the input string.

    Examples:
        >>> count_a_occurrences("Apple")
        1
        >>> count_a_occurrences("banana")
        3
        >>> count_a_occurrences("")
        0
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.lower().count('a')