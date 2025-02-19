def replace_hyphens_with_spaces(input_string: str) -> str:
    """
    Replace hyphens in a string with spaces.
    
    Args:
        input_string (str): A string potentially containing hyphens
    
    Returns:
        str: A new string with hyphens replaced by spaces
    
    Examples:
        >>> replace_hyphens_with_spaces("hello-world")
        'hello world'
        >>> replace_hyphens_with_spaces("python-is-awesome")
        'python is awesome'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.replace('-', ' ')