import numpy as np

arr = np.array([1,2,3,4])

#1. Iterate 1D array
for x in arr:
    print(x)

#2. Iterate 2D array
arr1 = np.array([[1,2],[3,4]])

for x in arr1:
    print(x)

#3. Iterate elements in 2D
for x in arr1:
    for y in x:
        print(y)

#4. nditer
for x in np.nditer(arr1):
    print(x)

#5. ndenumerate
for idx,x in np.ndenumerate(arr1):
    print(idx,x)

#6. Iterate 3D array
arr2 = np.array([[[1,2],[3,4]]])

for x in np.nditer(arr2):
    print(x)

#7. Print squares
for x in arr:
    print(x**2)

#8. Print even numbers
for x in arr:
    if x%2==0:
        print(x)

#9. Count elements
count = 0
for x in arr:
    count += 1
print(count)

#10. Sum during iteration
s = 0
for x in arr:
    s += x
print(s)