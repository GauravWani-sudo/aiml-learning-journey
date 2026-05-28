import numpy as np

#1. Shape of 1D array
arr = np.array([1,2,3,4])
print(arr.shape)

#2. Shape of 2D array
arr1 = np.array([[1,2],[3,4]])
print(arr1.shape)

#3. Shape of 3D array
arr2 = np.array([[[1],[2]],[[3],[4]]])
print(arr2.shape)

#4. Number of dimensions
print(arr2.ndim)

#5. Size of array
print(arr2.size)

#6. Length of array
print(len(arr))

#7. Create custom shape
arr3 = np.zeros((2,3,4))
print(arr3.shape)

#8. Total elements
print(arr3.size)

#9. Itemsize
print(arr3.itemsize)

#10. Check dimensions
print(arr3.ndim)