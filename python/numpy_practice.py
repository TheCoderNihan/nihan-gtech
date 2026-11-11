# NumPy (Numerical Python) is a library used for numerical calculations and working with arrays.
# It is faster and better than normal Python lists for mathematical operations.
# Used in Machine learning, AI development, Scientific applications, Financial calculations etc
# Numpy Arrays can have 0D(numbers), 1D(List), 2D(matrix), 3D(multiple 2D arrays)

import numpy as np

numbers = np.array([10, 20, 30, 40, 50])
print(numbers[0]); print(numbers[-1]) #indexing

# Using Numpy, we can do mathematical calculations directly on arrays
a = np.array([10, 20, 30])
b = np.array([2, 10, 5])
print(a + b) # Sum of corresponding the array elements. Arrays should be of equal no.of elements; else error
print(a - b)
print(a * b)
print(a / b)

# NumPy also supports comparisons. This is useful when filtering numerical data
print("Comparison: ", a > 20)

# NumPy provides several built-in functions for mathematical calculations
print("Sum: ", np.sum(numbers))
print("Mean: ", np.mean(numbers))
print("Maximum: ", np.max(numbers))
print("Minimum: ", np.min(numbers))
print("Median: ", np.median(numbers))
print("Standard Deviation: ", np.std(numbers))
print("Variance: ", np.var(numbers))
print("Square Root: ", np.sqrt(numbers))
print("Sorted Array: ", np.sort(numbers))


