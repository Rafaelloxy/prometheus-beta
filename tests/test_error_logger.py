import pytest
import logging
import io
import logging
from src.error_logger import log_custom_error

def test_log_custom_error_basic(caplog):
    """Test basic error logging functionality"""
    caplog.set_level(logging.ERROR)
    
    log_custom_error("Test error message")
    
    assert len(caplog.records) == 1
    assert caplog.records[0].levelno == logging.ERROR
    assert "Test error message" in caplog.text

def test_log_custom_error_with_exception(caplog):
    """Test logging with an exception"""
    caplog.set_level(logging.ERROR)
    
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        log_custom_error("An error occurred", error=e)
    
    assert len(caplog.records) == 1
    assert "An error occurred" in caplog.text
    assert "ValueError" in caplog.text
    assert "Traceback" in caplog.text

def test_log_custom_error_with_context(caplog):
    """Test logging with additional context"""
    caplog.set_level(logging.ERROR)
    
    context = {"user_id": 123, "action": "login"}
    log_custom_error("Context error", additional_context=context)
    
    assert len(caplog.records) == 1
    assert "Context error" in caplog.text
    assert "user_id" in caplog.text
    assert "action" in caplog.text

def test_log_custom_error_empty_message():
    """Test that empty message raises ValueError"""
    with pytest.raises(ValueError, match="Error message cannot be empty"):
        log_custom_error("")

def test_log_custom_error_different_log_levels(caplog):
    """Test logging with different log levels"""
    caplog.set_level(logging.INFO)
    
    log_custom_error("Warning message", log_level=logging.WARNING)
    log_custom_error("Info message", log_level=logging.INFO)
    
    assert len(caplog.records) == 2
    assert caplog.records[0].levelno == logging.WARNING
    assert caplog.records[1].levelno == logging.INFO