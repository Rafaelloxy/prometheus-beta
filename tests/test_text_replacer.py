import pytest
from src.text_replacer import replace_words

def test_basic_replacement():
    """Test basic word replacement"""
    assert replace_words("hello world", {"hello": "hi", "world": "earth"}) == "hi earth"

def test_partial_replacements():
    """Test when only some words are replaced"""
    assert replace_words("the quick brown fox", {"quick": "slow", "brown": "gray"}) == "the slow gray fox"

def test_no_replacements():
    """Test when no replacements are made"""
    original = "no replacements here"
    assert replace_words(original, {}) == original

def test_case_sensitive():
    """Test that replacements are case-sensitive"""
    assert replace_words("Hello WORLD", {"Hello": "Hi", "WORLD": "Earth"}) == "Hi WORLD"

def test_empty_input():
    """Test empty input string"""
    assert replace_words("", {"test": "replace"}) == ""

def test_multiple_same_replacements():
    """Test replacing multiple instances of the same word"""
    assert replace_words("dog cat dog", {"dog": "cat"}) == "cat cat cat"