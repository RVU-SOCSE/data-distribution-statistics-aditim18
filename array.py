import numpy as np


arr = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:", arr)


reshaped = arr.reshape(2, 3)
print("\nReshaped Array:\n", reshaped)


print("\nFirst element:", arr[0])
print("Element at [0][1]:", reshaped[0][1])


print("\nSum of elements:", np.sum(arr))
