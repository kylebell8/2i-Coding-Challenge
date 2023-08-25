# Assumptions

1. Sorted Input: The array 'nums' passed to the function is sorted in ascending order (stated in problem description)
2. Whole Numbers: The input array only contains whole numbers as stated in the problem requirement
3. Unique Pairs: Each element in the array can be used only in one pair as stated in the problem description
4. Count of Pairs: The function returns the count of such pairs that the sum up to 'X'
5. Optional Pair Lists: While not strictly required by the problem statement, the function also returns the pairs of numbers that sum up to 'X'
6. Return Types: The function returns two types of values, both a 'count' (integer value) and 'pairs' (list of tuples). Despite the problem asking for just a count fo the pairs, this design choice is assumed to be acceptable.
7. Empty Array: It is assumed that if an empty array is passed the function assumes the count of pairs is 0

## Design Choices

1. Two-Pointers Technique: The function uses a two-pointers technique to traverse through the array, this is an efficient apporach to the problem due to a relatively low time complexity.
2. Return Value: The function returns a tuple containing both the count of pairs and the pairs themselves, this design choice provides more information than just the count of pairs.
3. No External Libraries: As it is an isolated challenge, the function should not rely on any external libraries.

