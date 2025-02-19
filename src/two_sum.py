def two_sum(nums, target):
    """
    Find two indices in the array that add up to the target sum.
    
    Args:
        nums (list): List of integers to search through
        target (int): Target sum to find
    
    Returns:
        list: A list containing two indices where the corresponding values add up to the target.
              Returns an empty list if no such indices are found.
    """
    # Create a dictionary to store complement values
    complement_dict = {}
    
    # Iterate through the array with enumeration to keep track of indices
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in complement_dict:
            # Return the indices of the two numbers
            return [complement_dict[complement], i]
        
        # Store the current number and its index
        complement_dict[num] = i
    
    # Return empty list if no solution is found
    return []