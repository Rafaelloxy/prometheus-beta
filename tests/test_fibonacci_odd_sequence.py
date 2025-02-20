import pytest
from src.fibonacci_odd_sequence import generate_odd_fibonacci_sequence

def test_generate_odd_fibonacci_sequence():
    # Test zero-length sequence
    assert generate_odd_fibonacci_sequence(0) == []
    
    # Test single-element sequence
    assert generate_odd_fibonacci_sequence(1) == [1]
    
    # Test small sequences
    assert generate_odd_fibonacci_sequence(2) == [1, 1]
    assert generate_odd_fibonacci_sequence(3) == [1, 1, 2]
    assert generate_odd_fibonacci_sequence(4) == [1, 1, 2, 3]
    
    # Test sequence of length 5
    sequence = generate_odd_fibonacci_sequence(5)
    assert len(sequence) == 5
    assert all(num % 2 == 1 for num in sequence), "All numbers should be odd"
    
    # Test sequence of length 7
    sequence = generate_odd_fibonacci_sequence(7)
    assert len(sequence) == 7
    assert all(num % 2 == 1 for num in sequence), "All numbers should be odd"
    
    # Test a longer sequence
    sequence = generate_odd_fibonacci_sequence(10)
    assert len(sequence) == 10
    assert all(num % 2 == 1 for num in sequence), "All numbers should be odd"

def test_negative_input():
    with pytest.raises(ValueError, match="Length of sequence must be a non-negative integer"):
        generate_odd_fibonacci_sequence(-1)