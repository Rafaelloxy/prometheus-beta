import pytest
from src.remove_duplicates import remove_duplicate_characters

def test_remove_duplicate_characters_basic():
    # Test basic duplicate removal
    assert remove_duplicate_characters('hello') == 'helo'
    assert remove_duplicate_characters('aabbcc') == 'abc'
    assert remove_duplicate_characters('abcabc') == 'abc'

def test_remove_duplicate_characters_empty_string():
    # Test empty string
    assert remove_duplicate_characters('') == ''

def test_remove_duplicate_characters_no_duplicates():
    # Test string with no duplicates
    assert remove_duplicate_characters('python') == 'python'

def test_remove_duplicate_characters_single_character():
    # Test single character string
    assert remove_duplicate_characters('a') == 'a'

def test_remove_duplicate_characters_invalid_input():
    # Test error handling for non-string input
    with pytest.raises(ValueError, match='Input must be a string'):
        remove_duplicate_characters(123)
    
    # Test error handling for non-lowercase input
    with pytest.raises(ValueError, match='Input must contain only lowercase characters'):
        remove_duplicate_characters('Hello')
        remove_duplicate_characters('WORLD')
        remove_duplicate_characters('MixedCase')