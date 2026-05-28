import numpy as np

arr = np.array([5,3,1,4,2])

#1. Sort ascending
print(np.sort(arr))

#2. Sort descending
print(np.sort(arr)[::-1])

#3. Sort strings
arr1 = np.array(["banana","apple","cherry"])
print(np.sort(arr1))

#4. Sort booleans
arr2 = np.array([True,False,True])
print(np.sort(arr2))

#5. Sort 2D array
arr3 = np.array([[3,2,1],[6,5,4]])
print(np.sort(arr3))

#6. Row-wise sort
print(np.sort(arr3,axis=1))

#7. Column-wise sort
print(np.sort(arr3,axis=0))

#8. Argsort
print(np.argsort(arr))

#9. Largest element
print(np.sort(arr)[-1])

#10. Smallest element
print(np.sort(arr)[0])