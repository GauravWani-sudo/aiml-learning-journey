import numpy as np

#1. Access the first element of an array.
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr[0])

#2. Access the last element using negative indexing.
print(arr[-1])

#3. Extract the first 5 elements from an array.
print(arr[0:5])

#4. Reverse an array using slicing.
print(arr[::-1])

#5. Extract alternate elements from an array.
print(arr[::2])

#6. Create a 2D array and access element at row 2, column 3.
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1[1,2])

#7. Extract the first row from a matrix.
print(arr1[0])

#8. Extract the last column from a matrix.
print(arr1[:,-1])

#9. Slice a 3×3 submatrix from a 5×5 matrix.
arr1=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print(arr1[0:3,0:3])

#10. Replace the third element of an array with 100.
arr[2]=100
print(arr)