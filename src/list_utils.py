def remove_unique_elements(my_list):
    """
    Remove unique elements from a list of integers using only built-in list methods.
    
    Args:
        my_list (list): Input list of integers
    
    Returns:
        list: A new list containing only elements that appear more than once
    """
    result = []
    for item in my_list:
        if my_list.count(item) > 1 and item not in result:
            result.append(item)
    
    return result