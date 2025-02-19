import re

def reverse_words_in_string(s):
    """
    Reverse the order of each word in a string while maintaining original capitalization and punctuation.
    
    Args:
        s (str): Input string to be processed
    
    Returns:
        str: String with words reversed while preserving capitalization and punctuation
    """
    # Split the string into words and punctuation
    pattern = re.compile(r'(\w+|\W+)')
    tokens = pattern.findall(s)
    
    # Process only word tokens
    for i in range(len(tokens)):
        if tokens[i].isalpha():
            # Determine the original capitalization
            if tokens[i].istitle():
                tokens[i] = tokens[i][::-1].title()
            elif tokens[i].isupper():
                tokens[i] = tokens[i][::-1].upper()
            else:
                tokens[i] = tokens[i][::-1]
    
    # Reassemble the string
    return ''.join(tokens)