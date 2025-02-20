import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic functionality of removing duplicates."""
    assert remove_duplicate_chars('abracadabra') == 'abrc'
    assert remove_duplicate_chars('hello') == 'helo'
    assert remove_duplicate_chars('aabbccdd') == 'abcd'

def test_remove_duplicate_chars_empty_string():
    """Test with an empty string."""
    assert remove_duplicate_chars('') == ''

def test_remove_duplicate_chars_no_duplicates():
    """Test with a string that has no duplicates."""
    assert remove_duplicate_chars('python') == 'python'

def test_remove_duplicate_chars_single_char():
    """Test with a single character string."""
    assert remove_duplicate_chars('a') == 'a'

def test_remove_duplicate_chars_invalid_input():
    """Test error handling for invalid inputs."""
    # Non-string input
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    
    # Non-lowercase input
    with pytest.raises(ValueError):
        remove_duplicate_chars('Hello')
    with pytest.raises(ValueError):
        remove_duplicate_chars('WORLD')
    with pytest.raises(ValueError):
        remove_duplicate_chars('Mix3dC4se')