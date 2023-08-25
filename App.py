# 25/08/2023
# Description: 2i Coding Challenge - Test
# Name: Kyle Bell

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

# Additional test cases
print(find_pairs([2, 3, 4, 5, 6], 10))  # Output should be 1 (4+6)
print(find_pairs([1, 2, 3, 4, 5], 6))  # Output should be 2 (1+5, 2+4)
print(find_pairs([1, 2, 4, 7, 11, 15], 15))  # Output should be 2 (4+11, 1+14)
print(find_pairs([-5, -4, 0, 4, 5], 0))  # Output should be 2 (-5+5, -4+4)
print(find_pairs([1, 1, 1, 1], 2))  # Output should be 2 (1+1 twice)
print(find_pairs([], 5))  # Output should be 0 (empty array)
