import pytest
from src.stack_list_reversal import reverse_list_with_stack, Stack

def test_stack_implementation():
    """Test basic Stack operations"""
    stack = Stack()
    assert stack.is_empty() == True
    
    stack.push(1)
    assert stack.is_empty() == False
    
    item = stack.pop()
    assert item == 1
    assert stack.is_empty() == True
    
    with pytest.raises(IndexError):
        stack.pop()

def test_reverse_list_basic():
    """Test reversing a basic list of integers"""
    input_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list_with_stack(input_list)
    assert reversed_list == [5, 4, 3, 2, 1]

def test_reverse_list_empty():
    """Test reversing an empty list"""
    input_list = []
    reversed_list = reverse_list_with_stack(input_list)
    assert reversed_list == []

def test_reverse_list_single_element():
    """Test reversing a list with a single element"""
    input_list = [42]
    reversed_list = reverse_list_with_stack(input_list)
    assert reversed_list == [42]

def test_reverse_list_negative_numbers():
    """Test reversing a list with negative numbers"""
    input_list = [-1, -2, -3, -4, -5]
    reversed_list = reverse_list_with_stack(input_list)
    assert reversed_list == [-5, -4, -3, -2, -1]

def test_reverse_list_mixed_numbers():
    """Test reversing a list with mixed positive and negative numbers"""
    input_list = [-10, 0, 5, -3, 7]
    reversed_list = reverse_list_with_stack(input_list)
    assert reversed_list == [7, -3, 5, 0, -10]