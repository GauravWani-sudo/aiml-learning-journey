import numpy as np

arr = np.array([10,15,20,25,30,35])

#1. Filter even numbers
x = arr[arr%2==0]
print(x)

#2. Filter odd numbers
print(arr[arr%2!=0])

#3. Greater than 20
print(arr[arr>20])

#4. Less than 30
print(arr[arr<30])

#5. Boolean mask
mask = arr>20
print(mask)

#6. Use boolean mask
print(arr[mask])

#7. Multiple conditions
print(arr[(arr>10) & (arr<30)])

#8. Filter divisible by 5
print(arr[arr%5==0])

#9. Remove specific value
print(arr[arr!=25])

#10. Unique values
print(np.unique(arr))