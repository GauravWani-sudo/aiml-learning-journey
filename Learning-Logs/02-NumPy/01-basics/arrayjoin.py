import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

#1. Concatenate arrays
print(np.concatenate((arr1,arr2)))

#2. Stack vertically
print(np.vstack((arr1,arr2)))

#3. Stack horizontally
print(np.hstack((arr1,arr2)))

#4. Stack depth-wise
print(np.dstack((arr1,arr2)))

#5. Column stack
print(np.column_stack((arr1,arr2)))

#6. Row stack
print(np.row_stack((arr1,arr2)))

#7. Join 2D arrays
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.concatenate((a,b),axis=0))

#8. Horizontal join
print(np.concatenate((a,b),axis=1))

#9. Stack multiple arrays
print(np.stack((arr1,arr2)))

#10. Check shape after join
x = np.hstack((arr1,arr2))
print(x.shape)