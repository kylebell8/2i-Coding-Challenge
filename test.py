#Make something more complicated, make an array of 10 random numbers and print out the mean of the array.
#Make a function that takes an array as an argument and returns the mean of the array.

import numpy as np

def mean(array):
    return np.mean(array)

array = np.random.rand(10)
print(array)
print(mean(array))

