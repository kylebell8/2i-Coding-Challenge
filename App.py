def find_pairs(nums, X):
    """
    :param nums: List[int] - A sorted array of whole numbers
    :param X: int - The target sum
    :return: int - The count of pairs that sum to X
    """
    count = 0
    i, j = 0, len(nums) - 1
    
    while i < j:
        current_sum = nums[i] + nums[j]
        
        if current_sum == X:
            count += 1
            i += 1
            j -= 1
        elif current_sum < X:
            i += 1
        else:
            j -= 1
    
    return count

# Test the function
print(find_pairs([3, 4, 5, 6], 1))  # Output should be 0
print(find_pairs([0, 15, 32, 2000, 15000], 15))  # Output should be 1
print(find_pairs([1, 1, 10, 32, 41], 42))  # Output should be 2
