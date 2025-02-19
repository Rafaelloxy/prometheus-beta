import pytest
from src.unique_substrings import get_unique_substrings

def test_unique_substrings_basic():
    result = get_unique_substrings("abc")
    expected = set(['a', 'b', 'c', 'ab', 'bc', 'abc'])
    assert set(result) == expected

def test_unique_substrings_empty_string():
    result = get_unique_substrings("")
    assert result == []

def test_unique_substrings_single_char():
    result = get_unique_substrings("x")
    assert set(result) == set(['x'])

def test_unique_substrings_repeated_chars():
    result = get_unique_substrings("aaa")
    expected = set(['a', 'aa', 'aaa'])
    assert set(result) == expected

def test_unique_substrings_invalid_input():
    with pytest.raises(TypeError):
        get_unique_substrings(123)

def test_unique_substrings_complex_string():
    result = get_unique_substrings("hello")
    expected = set(['h', 'e', 'l', 'o', 'he', 'el', 'll', 'lo', 'hel', 'ell', 'llo', 'hell', 'ello', 'hello'])
    assert set(result) == expected