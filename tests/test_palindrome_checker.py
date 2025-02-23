import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("hello") == False

def test_case_insensitive():
    """Test that function is case-insensitive"""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A") == True

def test_palindrome_with_spaces():
    """Test palindromes with spaces"""
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("race a car") == False

def test_palindrome_with_punctuation():
    """Test palindromes with punctuation"""
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_empty_and_single_char():
    """Test empty string and single character"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_numbers():
    """Test palindromes with numbers"""
    assert is_palindrome("12321") == True
    assert is_palindrome("123") == False

def test_mixed_characters():
    """Test palindromes with mixed alphanumeric characters"""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22c1a") == False

def test_whitespace_only():
    """Test strings with only whitespace"""
    assert is_palindrome("   ") == True