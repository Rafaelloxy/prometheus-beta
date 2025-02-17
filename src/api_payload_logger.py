import logging
import json

def log_api_response_payload_size(response, logger=None):
    """
    Log the size of an API response payload.
    
    Args:
        response: API response object with a .text or .content attribute
        logger: Optional custom logger. If None, uses the default logging module
    
    Returns:
        int: Size of the payload in bytes
    
    Raises:
        TypeError: If response is None or does not have a valid payload
        ValueError: If payload cannot be processed
    """
    # Validate input
    if response is None:
        raise TypeError("Response cannot be None")
    
    # Determine payload 
    try:
        # Try to get payload text/content 
        if hasattr(response, 'text'):
            payload = response.text
        elif hasattr(response, 'content'):
            payload = response.content.decode('utf-8')
        else:
            raise TypeError("Response does not have a valid payload")
        
        # Calculate payload size
        payload_size = len(payload)
        
        # Use provided logger or default logging
        if logger is None:
            logger = logging
        
        # Log the payload size
        logger.info(f"API Response Payload Size: {payload_size} bytes")
        
        return payload_size
    
    except (AttributeError, TypeError) as e:
        raise TypeError(f"Unable to process response payload: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error logging payload size: {str(e)}")