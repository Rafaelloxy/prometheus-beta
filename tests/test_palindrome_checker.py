import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome cases."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("radar") == True

def test_palindromes_with_spaces():
    """Test palindromes with spaces."""
    assert is_palindrome("was it a car or a cat I saw") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_palindromes_with_punctuation():
    """Test palindromes with punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("race a car") == False

def test_case_insensitivity():
    """Test case-insensitive palindrome checks."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("LEVEL") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_empty_and_single_char():
    """Test edge cases with empty and single character strings."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_alphanumeric_palindromes():
    """Test palindromes with numbers."""
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("12345") == False