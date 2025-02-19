def convert_to_alternating_case(text: str) -> str:
    """
    Convert a string to alternating upper case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: A string with alternating uppercase characters.
    
    Examples:
        >>> convert_to_alternating_case("hello")
        'HeLlO'
        >>> convert_to_alternating_case("python")
        'PyThOn'
        >>> convert_to_alternating_case("")
        ''
    """
    if not text:
        return text
    
    return ''.join(char.upper() if i % 2 == 0 else char.lower() 
                   for i, char in enumerate(text))