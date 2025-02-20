import pytest
from src.anagram_finder import find_anagrams

def test_find_anagrams_basic():
    word = "listen"
    word_list = ["silent", "enlist", "hello", "world"]
    expected = ["silent", "enlist"]
    assert sorted(find_anagrams(word, word_list)) == sorted(expected)

def test_find_anagrams_case_insensitive():
    word = "Listen"
    word_list = ["SILENT", "enlist", "Hello", "World"]
    expected = ["SILENT", "enlist"]
    assert sorted(find_anagrams(word, word_list)) == sorted(expected)

def test_find_anagrams_no_matches():
    word = "python"
    word_list = ["java", "ruby", "javascript"]
    assert find_anagrams(word, word_list) == []

def test_find_anagrams_same_word_excluded():
    word = "hello"
    word_list = ["hello", "olleh", "world"]
    expected = ["olleh"]
    assert find_anagrams(word, word_list) == expected

def test_find_anagrams_empty_list():
    word = "test"
    word_list = []
    assert find_anagrams(word, word_list) == []