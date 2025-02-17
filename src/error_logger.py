import logging
import traceback
from typing import Optional, Any

def log_custom_error(message: str, 
                     error: Optional[Exception] = None, 
                     log_level: int = logging.ERROR, 
                     additional_context: Optional[dict] = None) -> None:
    """
    Log a custom error message with optional additional details.
    
    Args:
        message (str): The custom error message to log
        error (Optional[Exception]): Optional exception object to include traceback
        log_level (int): Logging level, defaults to logging.ERROR
        additional_context (Optional[dict]): Optional dictionary of additional context
    
    Raises:
        ValueError: If message is empty
    """
    # Validate input
    if not message:
        raise ValueError("Error message cannot be empty")
    
    # Configure logging to output to console
    logging.basicConfig(level=logging.DEBUG, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Create logger
    logger = logging.getLogger(__name__)
    
    # Prepare log details
    log_details = message
    
    # Add traceback if error is provided
    if error:
        log_details += f"\nException: {type(error).__name__}"
        log_details += f"\nTraceback: {traceback.format_exc()}"
    
    # Add additional context if provided
    if additional_context:
        log_details += f"\nContext: {additional_context}"
    
    # Log the message
    logger.log(log_level, log_details)