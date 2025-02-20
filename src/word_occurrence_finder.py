def find_word_occurrences(text, target_word):
    """
    Find all occurrences of a target word in a given text.
    
    Args:
        text (str): The input text to search in.
        target_word (str): The word to find occurrences of.
    
    Returns:
        list: A list of tuples containing (character_position, occurrence)
    """
    # Validate inputs
    if not isinstance(text, str) or not isinstance(target_word, str):
        raise TypeError("Both text and target_word must be strings")
    
    # Split the text into words
    words = text.split()
    
    # Track results and current character position
    occurrences = []
    current_position = 0
    
    # Iterate through words to find matches
    for word in words:
        # Add space to character position for words after the first
        if current_position > 0:
            current_position += 1
        
        # Check if current word matches target
        if word == target_word:
            occurrences.append((current_position, word))
        
        # Update current position
        current_position += len(word)
    
    return occurrences