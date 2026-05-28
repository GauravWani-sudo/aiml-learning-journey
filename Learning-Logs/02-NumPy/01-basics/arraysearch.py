import numpy as np

arr = np.array([1,2,3,4,5,4,4])

#1. Find index of 4
print(np.where(arr==4))

#2. Find even numbers
print(np.where(arr%2==0))

#3. Find odd numbers
print(np.where(arr%2==1))

#4. Search sorted
print(np.searchsorted(arr,3))

#5. Multiple search
print(np.searchsorted(arr,[2,4]))

#6. Greater than 3
print(np.where(arr>3))

#7. Less than 5
print(np.where(arr<5))

#8. Equal to 1
print(np.where(arr==1))

#9. Search in 2D
arr1 = np.array([[1,2],[3,4]])
print(np.where(arr1==4))

#10. Boolean result
print(arr>3)