import pytest
from src.palindrome_validator import is_palindrome

def test_basic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_empty_and_single_char():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_mixed_case_palindromes():
    assert is_palindrome("Madam") == True
    assert is_palindrome("RaceCar") == True

def test_with_numbers():
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("123 321") == True

def test_special_characters():
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("race a car") == False

def test_unicode_characters():
    # This handles basic unicode support, but might need more comprehensive testing
    assert is_palindrome("Madam, I'm Adam!") == True