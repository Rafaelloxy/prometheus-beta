class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

def reverse_list_with_stack(input_list):
    """
    Reverse the order of elements in a list using a Stack data structure.
    
    Args:
        input_list (list): A list of integers to be reversed.
    
    Returns:
        list: A new list with elements in reversed order.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Handle empty or None input
    if not input_list:
        return []
    
    # Create a stack and push all elements
    stack = Stack()
    for item in input_list:
        stack.push(item)
    
    # Pop elements to create reversed list
    reversed_list = []
    while not stack.is_empty():
        reversed_list.append(stack.pop())
    
    return reversed_list