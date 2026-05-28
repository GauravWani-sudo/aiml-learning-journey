import numpy as np

#1. Integer array
arr = np.array([1,2,3], dtype='i')
print(arr.dtype)

#2. Float array
arr1 = np.array([1.1,2.2,3.3], dtype='f')
print(arr1.dtype)

#3. String array
arr2 = np.array(["a","b","c"])
print(arr2.dtype)

#4. Boolean array
arr3 = np.array([True,False,True])
print(arr3.dtype)

#5. Complex array
arr4 = np.array([1+2j,3+4j])
print(arr4.dtype)

#6. Convert int to float
arr5 = arr.astype(float)
print(arr5)

#7. Convert float to int
arr6 = arr1.astype(int)
print(arr6)

#8. Check itemsize
print(arr.itemsize)

#9. Check datatype char
print(arr.dtype.char)

#10. Create unicode array
arr7 = np.array(["hello","world"], dtype='U')
print(arr7.dtype)