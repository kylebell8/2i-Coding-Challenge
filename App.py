# 25/08/2023
# Description: 2i Coding Challenge - Test
# Name: Kyle Bell

def find_pairs(nums, X):

    # Function to find pairs that sum up to a target value X in a sorted list of integers.
    # Parameters:
    #   nums: List[int] - A sorted array of whole numbers
    #   X: int - The target sum
    # Returns:
    #   int - The count of pairs that sum to X

    # Initialize count to 0, which will hold the number of pairs that sum to X
    count = 0
    
    # Initialize an empty list named pairs that will store the pairs of numbers that sum to X
    pairs = []
    
    # Initialize two pointers i and j. i starts from the beginning of the list, and j starts from the end
    i, j = 0, len(nums) - 1
    
    # Continue looping as long as i is less than j
    while i < j:
        # Calculate the sum of the numbers at the current i and j indices
        current_sum = nums[i] + nums[j]
        
        # If the current sum is equal to X
        if current_sum == X:
            # Increment the count by 1
            count += 1
            
            # Append the pair (nums[i], nums[j]) to the list pairs
            pairs.append((nums[i], nums[j]))
            
            # Increment i and decrement j to move towards the center of the list
            i += 1
            j -= 1
        # If the current sum is less than X, increment i to get a larger sum
        elif current_sum < X:
            i += 1
        # If the current sum is greater than X, decrement j to get a smaller sum
        else:
            j -= 1
    
    # Return the final count and the pairs list
    return count, pairs

# Test the function
count, pairs = find_pairs([3, 4, 5, 6], 1)
print(f"Array: [3, 4, 5, 6], Target Sum: 1, Pairs: {count}, Pairs List: {pairs}") 

count, pairs = find_pairs([0, 15, 32, 2000, 15000], 15)
print(f"Array: [0, 15, 32, 2000, 15000], Target Sum: 15, Pairs: {count}, Pairs List: {pairs}")  

count, pairs = find_pairs([1, 1, 10, 32, 41], 42)
print(f"Array: [1, 1, 10, 32, 41], Target Sum: 42, Pairs: {count}, Pairs List: {pairs}")  

# Additional test cases
count, pairs = find_pairs([2, 3, 5, 6, 7], 10)
print(f"Array: [2, 3, 5, 6, 7], Target Sum: 10, Pairs: {count}, Pairs List: {pairs}") 

count, pairs = find_pairs([1, 2, 3, 5, 6], 7)
print(f"Array: [1, 2, 3, 5, 6], Target Sum: 7, Pairs: {count}, Pairs List: {pairs}")  

count, pairs = find_pairs([1, 2, 3, 8, 15, 17], 17)
print(f"Array: [1, 2, 3, 8, 15, 17], Target Sum: 17, Pairs: {count}, Pairs List: {pairs}")  

count, pairs = find_pairs([-5, -4, 0, 4, 5, 9], 4)
print(f"Array: [-5, -4, 0, 4, 5, 9], Target Sum: 4, Pairs: {count}, Pairs List: {pairs}") 

count, pairs = find_pairs([1, 1, 2, 2], 3)
print(f"Array: [1, 1, 2, 2], Target Sum: 3, Pairs: {count}, Pairs List: {pairs}") 

count, pairs = find_pairs([], 5)
print(f"Array: [], Target Sum: 5, Pairs: {count}, Pairs List: {pairs}")  


#Desired Output
#Array: [3, 4, 5, 6], Target Sum: 1, Pairs: 0, Pairs List: []
#Array: [0, 15, 32, 2000, 15000], Target Sum: 15, Pairs: 1, Pairs List: [(0, 15)]    
#Array: [1, 1, 10, 32, 41], Target Sum: 42, Pairs: 2, Pairs List: [(1, 41), (10, 32)]
#Array: [2, 3, 5, 6, 7], Target Sum: 10, Pairs: 1, Pairs List: [(3, 7)]
#Array: [1, 2, 3, 5, 6], Target Sum: 7, Pairs: 2, Pairs List: [(1, 6), (2, 5)]       
#Array: [1, 2, 3, 8, 15, 17], Target Sum: 17, Pairs: 1, Pairs List: [(2, 15)]        
#Array: [-5, -4, 0, 4, 5, 9], Target Sum: 4, Pairs: 2, Pairs List: [(-5, 9), (0, 4)] 
#Array: [1, 1, 2, 2], Target Sum: 3, Pairs: 2, Pairs List: [(1, 2), (1, 2)]
#Array: [], Target Sum: 5, Pairs: 0, Pairs List: []