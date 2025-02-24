import logging
import time
import pytest
from src.function_logger import log_execution

# Create a custom logger for testing
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.DEBUG)

class TestFunctionLogger:
    def test_basic_function_logging(self, caplog):
        """Test that basic function logging works"""
        @log_execution(logger=test_logger)
        def test_func():
            return "success"
        
        caplog.set_level(logging.INFO)
        result = test_func()
        
        assert result == "success"
        assert "Starting execution of test_func" in caplog.text
        assert "Finished execution of test_func" in caplog.text
    
    def test_function_with_args(self, caplog):
        """Test logging with function arguments"""
        @log_execution(logger=test_logger)
        def test_func_with_args(x: int, y: int):
            return x + y
        
        caplog.set_level(logging.DEBUG)
        result = test_func_with_args(3, 4)
        
        assert result == 7
        
        # Check for debug level logs containing arguments
        debug_logs = [record for record in caplog.records if record.levelno == logging.DEBUG]
        assert any("Args: (3, 4), Kwargs: {}" in record.message for record in debug_logs)
    
    def test_exception_logging(self, caplog):
        """Test logging of exceptions"""
        @log_execution(logger=test_logger)
        def test_func_with_exception():
            raise ValueError("Test exception")
        
        caplog.set_level(logging.ERROR)
        
        with pytest.raises(ValueError, match="Test exception"):
            test_func_with_exception()
        
        assert "Exception in test_func_with_exception" in caplog.text
    
    def test_execution_time_logging(self, caplog):
        """Test that execution time is logged"""
        @log_execution(logger=test_logger)
        def slow_func():
            time.sleep(0.1)  # Simulate a slow operation
        
        caplog.set_level(logging.INFO)
        slow_func()
        
        # Check if execution time is logged
        assert "Execution time:" in caplog.text
        
        # Extract the logged execution time
        time_log = [record for record in caplog.records if "Execution time:" in record.message][0].message
        # Extract the time value
        exec_time = float(time_log.split(":")[1].strip().split()[0])
        
        # Verify the execution time is close to the sleep duration
        assert 0.09 < exec_time < 0.2