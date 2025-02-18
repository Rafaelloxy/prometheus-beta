import pytest
from src.longest_word_finder import find_longest_word

def test_find_longest_word_basic():
    """Test finding the longest word in a simple sentence."""
    assert find_longest_word("The quick brown fox") == "quick"

def test_find_longest_word_multiple_same_length():
    """Test when multiple words have the same length, return the first one."""
    assert find_longest_word("hello world great") == "hello"

def test_find_longest_word_empty_string():
    """Test handling of an empty string."""
    assert find_longest_word("") == ""

def test_find_longest_word_whitespace_string():
    """Test handling of a string with only whitespaces."""
    assert find_longest_word("   ") == ""

def test_find_longest_word_single_word():
    """Test with a single word."""
    assert find_longest_word("programming") == "programming"

def test_find_longest_word_punctuation():
    """Test finding longest word with punctuation."""
    assert find_longest_word("Hi! How are you?") == "programming"

def test_find_longest_word_invalid_input():
    """Test handling of non-string input."""
    with pytest.raises(TypeError):
        find_longest_word(123)
    
    with pytest.raises(TypeError):
        find_longest_word(None)