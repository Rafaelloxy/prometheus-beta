def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.
    
    Args:
        sentence (str): The input sentence to find the longest word from.
    
    Returns:
        str: The longest word in the sentence. 
             If multiple words have the same maximum length, returns the first one.
             If the sentence is empty, returns an empty string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Remove leading and trailing whitespaces
    sentence = sentence.strip()
    
    # If sentence is empty, return empty string
    if not sentence:
        return ""
    
    # Split the sentence into words
    words = sentence.split()
    
    # Find the longest word (first occurrence if multiple words have same length)
    return max(words, key=len)