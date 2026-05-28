import numpy as np

arr = np.array([1,2,3,4])

#1. Create copy
x = arr.copy()

#2. Modify original
arr[0] = 100

print(arr)
print(x)

#3. Create view
y = arr.view()

#4. Modify original
arr[1] = 200

print(arr)
print(y)

#5. Check base
print(x.base)
print(y.base)

#6. Modify view
y[2] = 300
print(arr)

#7. Modify copy
x[1] = 500
print(arr)
print(x)

#8. Memory sharing
print(y.base is arr)

#9. Check if copy shares memory
print(x.base is arr)

#10. Demonstrate shallow behavior
z = arr.view()
z[0] = 999
print(arr)