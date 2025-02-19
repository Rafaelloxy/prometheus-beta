def two_sum(nums, target):
    """
    Find two indices in an array that add up to the target sum.
    
    Args:
        nums (list): A list of integers
        target (int): The target sum to find
    
    Returns:
        list: A list of two indices where the corresponding numbers add up to the target
               Returns an empty list if no such indices are found
    """
    # Create a dictionary to store complement values
    num_dict = {}
    
    # Iterate through the array with enumeration to keep track of indices
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            # Return the indices of the two numbers
            return [num_dict[complement], i]
        
        # Store the current number and its index
        num_dict[num] = i
    
    # If no solution is found, return an empty list
    return []