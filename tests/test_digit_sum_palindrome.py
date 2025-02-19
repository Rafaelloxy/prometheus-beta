import pytest
from src.digit_sum_palindrome import is_digit_sum_palindrome

def test_digit_sum_palindrome():
    # Test cases with palindrome digit sums
    assert is_digit_sum_palindrome(11) == True    # 1+1 = 2 (palindrome)
    assert is_digit_sum_palindrome(123) == False  # 1+2+3 = 6 (not a palindrome)
    assert is_digit_sum_palindrome(44) == True    # 4+4 = 8 (palindrome)

def test_digit_sum_palindrome_zero_and_single_digit():
    # Test edge cases with zero and single-digit numbers
    assert is_digit_sum_palindrome(0) == True     # 0 is a palindrome
    assert is_digit_sum_palindrome(5) == True     # 5 is a palindrome
    
def test_digit_sum_palindrome_negative_numbers():
    # Test negative numbers
    assert is_digit_sum_palindrome(-11) == True   # abs(1+1) = 2 (palindrome)
    assert is_digit_sum_palindrome(-123) == False # abs(1+2+3) = 6 (not a palindrome)

def test_digit_sum_palindrome_large_numbers():
    # Test large numbers
    assert is_digit_sum_palindrome(1234) == False  # 1+2+3+4 = 10 (not a palindrome)
    assert is_digit_sum_palindrome(9999) == True   # 9+9+9+9 = 36 (not a palindrome)