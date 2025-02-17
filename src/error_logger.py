import logging

def log_custom_error(error_message, error_level=logging.ERROR, additional_info=None):
    """
    Log a custom error message with optional additional information.
    
    Args:
        error_message (str): The primary error message to log
        error_level (int, optional): Logging level. Defaults to logging.ERROR
        additional_info (dict, optional): Additional context for the error. Defaults to None
    
    Returns:
        bool: True if logging was successful, False otherwise
    """
    try:
        # Configure basic logging if not already configured
        logging.basicConfig(
            level=logging.DEBUG, 
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        # Prepare the log message
        log_msg = error_message
        if additional_info:
            log_msg += f" | Additional Info: {additional_info}"
        
        # Log the message at the specified level
        if error_level == logging.DEBUG:
            logging.debug(log_msg)
        elif error_level == logging.INFO:
            logging.info(log_msg)
        elif error_level == logging.WARNING:
            logging.warning(log_msg)
        elif error_level == logging.ERROR:
            logging.error(log_msg)
        elif error_level == logging.CRITICAL:
            logging.critical(log_msg)
        else:
            logging.error(f"Invalid log level: {error_level}. Using default ERROR level.")
            logging.error(log_msg)
        
        return True
    except Exception as e:
        # Fallback logging in case of any logging failure
        print(f"Logging failed: {e}")
        return False