import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

#1. Reshape into 3x4
print(arr.reshape(3,4))

#2. Reshape into 2x6
print(arr.reshape(2,6))

#3. Reshape into 4x3
print(arr.reshape(4,3))

#4. Reshape into 3D
print(arr.reshape(2,2,3))

#5. Flatten array
arr1 = np.array([[1,2],[3,4]])
print(arr1.reshape(-1))

#6. Use -1
print(arr.reshape(2,-1))

#7. Convert 2D to 1D
print(arr1.flatten())

#8. Ravel array
print(arr1.ravel())

#9. Reshape and print shape
x = arr.reshape(3,4)
print(x.shape)

