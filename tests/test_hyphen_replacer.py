import pytest
from src.hyphen_replacer import replace_hyphens_with_spaces

def test_replace_hyphens_with_spaces():
    # Test basic replacement
    assert replace_hyphens_with_spaces("hello-world") == "hello world"
    assert replace_hyphens_with_spaces("python-is-awesome") == "python is awesome"
    
    # Test string with no hyphens
    assert replace_hyphens_with_spaces("hello") == "hello"
    
    # Test empty string
    assert replace_hyphens_with_spaces("") == ""
    
    # Test multiple consecutive hyphens
    assert replace_hyphens_with_spaces("hello---world") == "hello   world"

def test_replace_hyphens_invalid_input():
    # Test non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_hyphens_with_spaces(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_hyphens_with_spaces(None)