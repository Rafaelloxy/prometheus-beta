def to_alternating_constant_case(s: str) -> str:
    """
    Convert a string to alternating constant case.
    
    Args:
        s (str): Input string to be converted
    
    Returns:
        str: String converted to alternating constant case
    
    Examples:
        >>> to_alternating_constant_case("hello world")
        'HELLO world'
        >>> to_alternating_constant_case("python is awesome")
        'PYTHON is AWESOME'
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Split the string into words
    words = s.split()
    
    # Convert words to alternating constant case
    converted_words = [
        word.upper() if i % 2 == 0 else word.lower() 
        for i, word in enumerate(words)
    ]
    
    # Join the words back together
    return ' '.join(converted_words)