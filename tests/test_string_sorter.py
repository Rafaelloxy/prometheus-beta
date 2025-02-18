import pytest
from src.string_sorter import sort_strings_by_length

def test_sort_strings_by_length_normal_case():
    input_list = ['apple', 'banana', 'cherry', 'date']
    expected = ['date', 'apple', 'banana', 'cherry']
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_by_length_empty_list():
    assert sort_strings_by_length([]) == []

def test_sort_strings_by_length_same_length_strings():
    input_list = ['cat', 'dog', 'rat']
    assert sort_strings_by_length(input_list) == input_list

def test_sort_strings_by_length_mixed_lengths():
    input_list = ['a', 'longer', 'short', 'longest']
    expected = ['a', 'short', 'longer', 'longest']
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_by_length_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        sort_strings_by_length("not a list")

def test_sort_strings_by_length_invalid_list_content():
    with pytest.raises(TypeError, match="All elements must be strings"):
        sort_strings_by_length([1, 2, 3])
        
def test_sort_strings_by_length_mixed_type_list():
    with pytest.raises(TypeError, match="All elements must be strings"):
        sort_strings_by_length(['hello', 42, 'world'])