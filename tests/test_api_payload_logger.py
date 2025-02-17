import pytest
import logging
from unittest.mock import Mock, patch
from src.api_payload_logger import log_api_response_payload_size

class MockResponse:
    def __init__(self, text=None, content=None):
        self.text = text
        self.content = content.encode('utf-8') if content else None

def test_log_api_response_payload_size_with_text():
    # Test with text payload
    response = MockResponse(text="Hello, World!")
    
    with patch('logging.info') as mock_log:
        size = log_api_response_payload_size(response)
        assert size == 13
        mock_log.assert_called_once_with("API Response Payload Size: 13 bytes")

def test_log_api_response_payload_size_with_content():
    # Test with content payload
    response = MockResponse(content="API Response")
    
    with patch('logging.info') as mock_log:
        size = log_api_response_payload_size(response)
        assert size == 12
        mock_log.assert_called_once_with("API Response Payload Size: 12 bytes")

def test_log_api_response_payload_size_with_custom_logger():
    # Test with custom logger
    response = MockResponse(text="Custom Logger")
    mock_logger = Mock()
    
    size = log_api_response_payload_size(response, logger=mock_logger)
    assert size == 13
    mock_logger.info.assert_called_once_with("API Response Payload Size: 13 bytes")

def test_log_api_response_payload_size_none_response():
    # Test with None response
    with pytest.raises(TypeError, match="Response cannot be None"):
        log_api_response_payload_size(None)

def test_log_api_response_payload_size_invalid_response():
    # Test with invalid response object
    invalid_response = object()
    with pytest.raises(TypeError, match="Response does not have a valid payload"):
        log_api_response_payload_size(invalid_response)