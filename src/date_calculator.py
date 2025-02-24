import re
from datetime import datetime

def calculate_days_between_dates(date1: str, date2: str) -> int:
    """
    Calculate the number of days between two dates.

    Args:
        date1 (str): First date in 'YYYY-MM-DD' format
        date2 (str): Second date in 'YYYY-MM-DD' format

    Returns:
        int: Number of days between the two dates (absolute value)

    Raises:
        ValueError: If dates are not in the correct format or are invalid
    """
    # Validate date format using regex
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    
    # Check if dates match the exact format
    if not (date_pattern.match(date1) and date_pattern.match(date2)):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD format.")
    
    try:
        # Parse the dates, which will validate date correctness
        parsed_date1 = datetime.strptime(date1, '%Y-%m-%d')
        parsed_date2 = datetime.strptime(date2, '%Y-%m-%d')
        
        # Calculate the difference and return absolute number of days
        delta = abs((parsed_date2 - parsed_date1).days)
        
        return delta
    
    except ValueError as e:
        # Re-raise with a clear error message
        raise ValueError(f"Invalid date format. {str(e)}")