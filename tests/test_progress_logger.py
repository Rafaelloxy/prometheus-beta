import pytest
import time
import io
import sys
from src.progress_logger import DynamicProgressBar, log_with_progress

def test_dynamic_progress_bar_initialization():
    """Test initialization of DynamicProgressBar"""
    total = 100
    progress = DynamicProgressBar(total)
    
    assert progress.total == 100
    assert progress.prefix == 'Progress:'
    assert progress.suffix == 'Complete'
    assert progress.decimals == 1
    assert progress.length == 50

def test_dynamic_progress_bar_update(capsys):
    """Test progress bar update method"""
    total = 10
    progress = DynamicProgressBar(total)
    
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Simulate progress updates
    for i in range(total + 1):
        progress.update(i)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check captured output
    output = captured_output.getvalue()
    assert '100.0%' in output
    assert 'Elapsed:' in output
    assert 'Remaining:' in output

def test_log_with_progress():
    """Test log_with_progress generator"""
    test_list = list(range(5))
    
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Use log_with_progress
    processed_list = list(log_with_progress(test_list, prefix='Test Progress:'))
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check results
    assert processed_list == test_list
    
    output = captured_output.getvalue()
    assert '100.0%' in output
    assert 'Test Progress:' in output

def test_log_with_progress_custom_parameters():
    """Test log_with_progress with custom parameters"""
    test_list = list(range(3))
    
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Use log_with_progress with custom parameters
    processed_list = list(log_with_progress(test_list, prefix='Custom:', length=20, fill='#'))
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check results
    assert processed_list == test_list
    
    output = captured_output.getvalue()
    assert '100.0%' in output
    assert 'Custom:' in output
    assert '#' in output  # Custom fill character