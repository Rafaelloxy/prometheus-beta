from typing import List

def count_anagrams(s: str) -> int:
    """
    Count the number of distinct anagrams in the given string.
    
    An anagram is a sequence of letters that can be rearranged to form another valid sequence.
    
    Args:
        s (str): Input string containing only lowercase English letters
    
    Returns:
        int: Number of distinct anagrams in the string
    
    Raises:
        ValueError: If the input string contains characters other than lowercase English letters
    """
    # Validate input
    if not s or not all(char.islower() and char.isalpha() for char in s):
        raise ValueError("Input must be a non-empty string of lowercase English letters")
    
    # Use set to track unique sorted anagrams
    anagram_set = set()
    
    # Generate all possible substrings
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            
            # Sort the substring to identify anagrams
            sorted_substring = ''.join(sorted(substring))
            
            # Add to set of unique anagrams
            anagram_set.add(sorted_substring)
    
    return len(anagram_set)