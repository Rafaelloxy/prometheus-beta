def replace_words(text: str, replacements: dict) -> str:
    """
    Perform in-place text replacements using a dictionary of word replacements.
    
    Args:
        text (str): The input text to modify
        replacements (dict): A dictionary where keys are words to replace 
                             and values are their replacements
    
    Returns:
        str: The modified text with replacements applied
    
    Examples:
        >>> replace_words("hello world", {"hello": "hi", "world": "earth"})
        'hi earth'
        >>> replace_words("the quick brown fox", {"quick": "slow", "brown": "gray"})
        'the slow gray fox'
    """
    # Split the text into words
    words = text.split()
    
    # Replace words using the replacements dictionary
    replaced_words = [replacements.get(word, word) for word in words]
    
    # Join the words back into a string
    return ' '.join(replaced_words)