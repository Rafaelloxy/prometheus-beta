"""
Test suite for file_reader module.
"""

import os
import pytest
import tempfile

from src.file_reader import read_text_file

def test_read_existing_text_file():
    """Test reading a normal text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_file.write("Hello, world!")
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == "Hello, world!"
        finally:
            os.unlink(temp_file.name)

def test_read_empty_file():
    """Test reading an empty file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == ""
        finally:
            os.unlink(temp_file.name)

def test_nonexistent_file():
    """Test reading a nonexistent file."""
    with pytest.raises(FileNotFoundError):
        read_text_file("nonexistent_file.txt")

def test_invalid_input_types():
    """Test invalid input types."""
    with pytest.raises(TypeError):
        read_text_file(None)
    
    with pytest.raises(TypeError):
        read_text_file(123)

def test_empty_path():
    """Test empty file path."""
    with pytest.raises(ValueError):
        read_text_file("")
    
    with pytest.raises(ValueError):
        read_text_file("   ")

def test_directory_path():
    """Test attempting to read a directory."""
    with pytest.raises(IsADirectoryError):
        read_text_file(".")  # Current directory