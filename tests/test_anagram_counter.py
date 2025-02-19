import pytest
from src.anagram_counter import count_anagrams

def test_count_anagrams_basic():
    """Test basic functionality with a simple example."""
    assert count_anagrams('abab') == 4  # unique sorted anagrams: 'a', 'b', 'ab', 'ba'

def test_count_anagrams_no_repeats():
    """Test a string with no repeated anagrams."""
    assert count_anagrams('abc') == 6  # unique sorted anagrams: 'a', 'b', 'c', 'ab', 'bc', 'abc'

def test_count_anagrams_single_char():
    """Test a single character string."""
    assert count_anagrams('a') == 1

def test_count_anagrams_same_char():
    """Test a string with the same character repeated."""
    assert count_anagrams('aaa') == 1

def test_count_anagrams_invalid_input():
    """Test invalid input raises ValueError."""
    with pytest.raises(ValueError):
        count_anagrams('')
    
    with pytest.raises(ValueError):
        count_anagrams('ABC')  # uppercase not allowed
    
    with pytest.raises(ValueError):
        count_anagrams('ab1c')  # non-letter characters not allowed

def test_count_anagrams_complex():
    """Test a more complex case with multiple unique anagrams."""
    result = count_anagrams('xyyx')
    assert result == 6  # unique sorted anagrams: 'x', 'y', 'xy', 'yx', 'xx', 'yy'