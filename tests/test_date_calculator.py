import pytest
from src.date_calculator import calculate_days_between_dates

def test_calculate_days_between_dates_same_date():
    """Test calculating days between the same date returns 0."""
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_consecutive_days():
    """Test calculating days between consecutive dates."""
    assert calculate_days_between_dates('2023-01-01', '2023-01-02') == 1

def test_calculate_days_between_dates_different_years():
    """Test calculating days between dates in different years."""
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1

def test_calculate_days_between_dates_large_gap():
    """Test calculating days between dates with a large gap."""
    assert calculate_days_between_dates('2020-01-01', '2023-01-01') == 1096

def test_calculate_days_between_dates_order_independent():
    """Test that order of dates doesn't matter."""
    assert calculate_days_between_dates('2023-01-02', '2023-01-01') == 1
    assert calculate_days_between_dates('2023-01-01', '2023-01-02') == 1

def test_calculate_days_between_dates_invalid_format():
    """Test that invalid date formats raise a ValueError."""
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates('2023/01/01', '2023-01-02')
    
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates('2023-1-1', '2023-01-02')

def test_calculate_days_between_dates_invalid_date():
    """Test that invalid dates raise a ValueError."""
    error_cases = [
        '2023-02-30',  # Invalid day for February
        '2023-13-01',  # Invalid month
        '2023-00-01',  # Invalid month
        '2023-01-00',  # Invalid day
        '2023-01-32'   # Invalid day for January
    ]
    
    for invalid_date in error_cases:
        with pytest.raises(ValueError, match="Invalid date format"):
            calculate_days_between_dates(invalid_date, '2023-01-01')