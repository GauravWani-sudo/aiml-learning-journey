import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

#1. Split into 2 parts
print(np.array_split(arr,2))

#2. Split into 4 parts
print(np.array_split(arr,4))

#3. Unequal split
print(np.array_split(arr,3))

#4. Split 2D array
arr1 = np.array([[1,2],[3,4],[5,6],[7,8]])
print(np.array_split(arr1,2))

#5. Horizontal split
print(np.hsplit(arr1,2))

#6. Vertical split
print(np.vsplit(arr1,2))

#7. Split columns
print(np.hsplit(arr1,2)[0])

#8. Access split parts
x = np.array_split(arr,2)
print(x[0])

#9. Number of splits
print(len(x))

#10. Shape after split
print(x[0].shape)