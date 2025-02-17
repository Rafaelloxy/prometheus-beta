import logging
import pytest
import io
import sys

from src.error_logger import log_custom_error

def test_log_custom_error_default():
    """Test default error logging"""
    # Capture log output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.ERROR)
    
    # Log an error
    result = log_custom_error("Test error message")
    
    # Check results
    assert result is True
    log_output = log_capture.getvalue()
    assert "Test error message" in log_output
    assert "ERROR" in log_output

def test_log_custom_error_with_additional_info():
    """Test logging with additional information"""
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.DEBUG)
    
    additional_info = {"user_id": 123, "action": "login"}
    result = log_custom_error("Authentication failed", additional_info=additional_info)
    
    assert result is True
    log_output = log_capture.getvalue()
    assert "Authentication failed" in log_output
    assert "user_id" in log_output
    assert "action" in log_output

def test_log_custom_error_different_levels():
    """Test logging at different levels"""
    log_levels = [
        (logging.DEBUG, "Debug message"),
        (logging.INFO, "Info message"),
        (logging.WARNING, "Warning message"),
        (logging.ERROR, "Error message"),
        (logging.CRITICAL, "Critical message")
    ]
    
    for level, message in log_levels:
        log_capture = io.StringIO()
        logging.basicConfig(stream=log_capture, level=logging.DEBUG)
        
        result = log_custom_error(message, error_level=level)
        
        assert result is True
        log_output = log_capture.getvalue()
        assert message in log_output

def test_log_custom_error_invalid_level():
    """Test logging with an invalid level"""
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.DEBUG)
    
    result = log_custom_error("Invalid level test", error_level=999)
    
    assert result is True
    log_output = log_capture.getvalue()
    assert "Invalid log level" in log_output
    assert "Invalid level test" in log_output