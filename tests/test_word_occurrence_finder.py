import pytest
from src.word_occurrence_finder import find_word_occurrences

def test_find_word_occurrences_basic():
    text = "hello world hello python hello"
    target_word = "hello"
    expected = [(0, "hello"), (12, "hello"), (25, "hello")]
    assert find_word_occurrences(text, target_word) == expected

def test_find_word_occurrences_single_occurrence():
    text = "testing a unique word"
    target_word = "unique"
    expected = [(14, "unique")]
    assert find_word_occurrences(text, target_word) == expected

def test_find_word_occurrences_no_occurrence():
    text = "this is a test string"
    target_word = "missing"
    assert find_word_occurrences(text, target_word) == []

def test_find_word_occurrences_empty_string():
    text = ""
    target_word = "hello"
    assert find_word_occurrences(text, target_word) == []

def test_find_word_occurrences_invalid_input():
    with pytest.raises(TypeError):
        find_word_occurrences(123, "hello")
    
    with pytest.raises(TypeError):
        find_word_occurrences("hello world", 123)

def test_find_word_occurrences_case_sensitive():
    text = "Hello hello HELLO"
    target_word = "hello"
    expected = [(6, "hello")]
    assert find_word_occurrences(text, target_word) == expected