import pytest
from src.prime_filter import filter_primes

def test_filter_primes_positive_numbers():
    # Test with positive prime and non-prime numbers
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13]
    expected = [2, 3, 5, 7, 11, 13]
    assert filter_primes(input_list) == expected

def test_filter_primes_negative_numbers():
    # Test with negative prime and non-prime numbers
    input_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -11, -13]
    assert filter_primes(input_list) == []

def test_filter_primes_mixed_numbers():
    # Test with mixed positive and negative numbers
    input_list = [-7, -4, 2, 3, 4, 5, 6, 7, 11]
    expected = [2, 3, 5, 7, 11]
    assert filter_primes(input_list) == expected

def test_filter_primes_empty_list():
    # Test with an empty list
    assert filter_primes([]) == []

def test_filter_primes_no_primes():
    # Test with a list containing no prime numbers
    input_list = [1, 4, 6, 8, 9, 10]
    assert filter_primes(input_list) == []

def test_filter_primes_only_primes():
    # Test with a list containing only prime numbers
    input_list = [2, 3, 5, 7, 11, 13]
    assert filter_primes(input_list) == input_list