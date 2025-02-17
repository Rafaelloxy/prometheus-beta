import pytest
import logging
import io
import sys
from src.error_logger import log_error

# Capture log output
def capture_logs():
    log_capture_string = io.StringIO()
    handler = logging.StreamHandler(log_capture_string)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.ERROR)
    return log_capture_string, handler

# Remove log handlers to reset logging
def reset_logging(handler=None):
    if handler:
        logging.getLogger().removeHandler(handler)
    logging.getLogger().setLevel(logging.NOTSET)

# Test functions with error logging decorator
@log_error()
def divide_numbers(a, b):
    return a / b

@log_error(message="Custom error occurred during calculation")
def complex_calculation(x):
    return 10 / (x - 2)

def test_default_error_logging():
    log_capture_string, handler = capture_logs()
    
    try:
        divide_numbers(10, 0)
        pytest.fail("Expected ZeroDivisionError")
    except ZeroDivisionError:
        log_output = log_capture_string.getvalue()
        assert "Error in divide_numbers" in log_output
        assert "division by zero" in log_output
    finally:
        reset_logging(handler)

def test_custom_error_message():
    log_capture_string, handler = capture_logs()
    
    try:
        complex_calculation(2)
        pytest.fail("Expected ZeroDivisionError")
    except ZeroDivisionError:
        log_output = log_capture_string.getvalue()
        assert "Custom error occurred during calculation" in log_output
    finally:
        reset_logging(handler)

def test_error_propagation():
    # Ensure the original exception is still raised
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

def test_decorator_preserves_function_metadata():
    @log_error()
    def test_func():
        """A test function docstring"""
        pass
    
    assert test_func.__name__ == 'test_func'
    assert test_func.__doc__ == 'A test function docstring'