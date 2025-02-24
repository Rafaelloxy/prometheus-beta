import pytest
from src.count_a_occurrences import count_a_occurrences

def test_count_a_occurrences_basic():
    """Test basic functionality of counting 'a' occurrences."""
    assert count_a_occurrences("apple") == 1
    assert count_a_occurrences("banana") == 3
    assert count_a_occurrences("APPLE") == 1

def test_count_a_occurrences_mixed_case():
    """Test mixed case scenarios."""
    assert count_a_occurrences("AbAcAdA") == 4
    assert count_a_occurrences("AaAaAaAa") == 8

def test_count_a_occurrences_empty_string():
    """Test with empty string."""
    assert count_a_occurrences("") == 0

def test_count_a_occurrences_no_a():
    """Test string with no 'a' characters."""
    assert count_a_occurrences("hello") == 0
    assert count_a_occurrences("HELLO") == 0

def test_count_a_occurrences_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        count_a_occurrences(123)
    with pytest.raises(TypeError):
        count_a_occurrences(None)
    with pytest.raises(TypeError):
        count_a_occurrences(["a", "b", "c"])