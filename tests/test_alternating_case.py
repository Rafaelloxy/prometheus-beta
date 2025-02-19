import pytest
from src.alternating_case import convert_to_alternating_case

def test_convert_to_alternating_case_basic():
    assert convert_to_alternating_case("hello") == "HeLlO"
    assert convert_to_alternating_case("python") == "PyThOn"

def test_convert_to_alternating_case_empty_string():
    assert convert_to_alternating_case("") == ""

def test_convert_to_alternating_case_single_char():
    assert convert_to_alternating_case("a") == "A"
    assert convert_to_alternating_case("B") == "B"

def test_convert_to_alternating_case_mixed_input():
    assert convert_to_alternating_case("HeLLo") == "HeLlO"
    assert convert_to_alternating_case("wORlD") == "WoRlD"

def test_convert_to_alternating_case_spaces_and_symbols():
    assert convert_to_alternating_case("hello world") == "HeLlO WoRlD"
    assert convert_to_alternating_case("hello, world!") == "HeLlO, WoRlD!"