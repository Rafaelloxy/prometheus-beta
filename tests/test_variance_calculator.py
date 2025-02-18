import pytest
from src.variance_calculator import calculate_variance

def test_calculate_variance_normal_case():
    """Test variance calculation for a standard list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    assert round(calculate_variance(numbers), 4) == 2.0000

def test_calculate_variance_single_number():
    """Test variance with a single number."""
    numbers = [42]
    assert calculate_variance(numbers) == 0.0

def test_calculate_variance_negative_numbers():
    """Test variance calculation with negative numbers."""
    numbers = [-1, -2, -3, -4, -5]
    assert round(calculate_variance(numbers), 4) == 2.0000

def test_calculate_variance_mixed_numbers():
    """Test variance with mixed positive and negative numbers."""
    numbers = [-2, 0, 2]
    assert round(calculate_variance(numbers), 4) == 2.6667

def test_calculate_variance_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate variance of an empty list"):
        calculate_variance([])

def test_calculate_variance_non_numeric():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_variance(['a', 'b', 'c'])

def test_calculate_variance_mixed_numeric_types():
    """Test variance calculation with mixed numeric types."""
    numbers = [1, 2.5, 3, 4, 5]
    assert round(calculate_variance(numbers), 4) == 1.7000