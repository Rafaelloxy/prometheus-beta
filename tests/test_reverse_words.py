import pytest
from src.reverse_words import reverse_words_in_string

def test_reverse_words_basic():
    assert reverse_words_in_string("Hello World") == "olleH dlroW"

def test_reverse_words_with_punctuation():
    assert reverse_words_in_string("Hello, World!") == "olleH, dlroW!"

def test_reverse_words_mixed_case():
    assert reverse_words_in_string("Hello world") == "olleH dlrow"

def test_reverse_words_uppercase():
    assert reverse_words_in_string("HELLO WORLD") == "OLLEH DLROW"

def test_reverse_words_title_case():
    assert reverse_words_in_string("Hello World") == "olleH dlroW"

def test_reverse_words_multiple_spaces():
    assert reverse_words_in_string("  Hello   World  ") == "  olleH   dlroW  "

def test_reverse_words_with_numbers_and_punctuation():
    assert reverse_words_in_string("Hello123 World!") == "olleH123 dlroW!"

def test_empty_string():
    assert reverse_words_in_string("") == ""

def test_single_word():
    assert reverse_words_in_string("Hello") == "olleH"