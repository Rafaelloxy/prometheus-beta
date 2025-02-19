import pytest
from src.list_reverser import reverse_list_with_stack, Stack

def test_stack_basic_operations():
    stack = Stack()
    assert stack.is_empty() == True
    
    stack.push(1)
    assert stack.is_empty() == False
    
    item = stack.pop()
    assert item == 1
    assert stack.is_empty() == True

def test_reverse_list_with_stack():
    # Test normal list
    input_list = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    assert reverse_list_with_stack(input_list) == expected

def test_reverse_empty_list():
    # Test empty list
    assert reverse_list_with_stack([]) == []

def test_reverse_single_element_list():
    # Test single element list
    input_list = [42]
    assert reverse_list_with_stack(input_list) == [42]

def test_reverse_large_list():
    # Test large list
    input_list = list(range(1000))
    expected = list(reversed(input_list))
    assert reverse_list_with_stack(input_list) == expected

def test_reverse_list_with_negative_numbers():
    # Test list with negative numbers
    input_list = [-1, -2, -3, 0, 1, 2, 3]
    expected = [3, 2, 1, 0, -3, -2, -1]
    assert reverse_list_with_stack(input_list) == expected

def test_stack_pop_empty_raises_error():
    # Test popping from an empty stack raises an error
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()