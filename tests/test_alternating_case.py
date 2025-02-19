import pytest
from src.alternating_case import to_alternating_constant_case

def test_basic_alternating_case():
    assert to_alternating_constant_case("hello world") == "HELLO world"
    assert to_alternating_constant_case("python is awesome") == "PYTHON is AWESOME"

def test_single_word():
    assert to_alternating_constant_case("hello") == "HELLO"

def test_empty_string():
    assert to_alternating_constant_case("") == ""

def test_multiple_words():
    assert to_alternating_constant_case("one two three four") == "ONE two THREE four"

def test_input_type():
    with pytest.raises(TypeError):
        to_alternating_constant_case(123)
    with pytest.raises(TypeError):
        to_alternating_constant_case(None)

def test_trailing_and_leading_spaces():
    assert to_alternating_constant_case("  hello world  ") == "HELLO world"