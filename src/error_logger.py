import logging
import functools

def log_error(message=None):
    """
    A decorator that logs custom error messages when an exception occurs.
    
    Args:
        message (str, optional): A custom error message to log. 
                                 If not provided, uses the default exception message.
    
    Returns:
        A decorator function that wraps the original function with error logging.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Configure basic logging if not already configured
                logging.basicConfig(
                    level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s'
                )
                
                # Use custom message if provided, otherwise use exception message
                error_message = message or str(e)
                
                # Log the error
                logging.error(f"Error in {func.__name__}: {error_message}")
                
                # Re-raise the exception to maintain original error handling
                raise
        return wrapper
    return decorator