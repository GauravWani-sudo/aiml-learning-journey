import numpy as np

#1. Import Numpy and print its Version
print(np.__version__)

#2.Create a NumPy array with numbers 1 to 10.
print(np.arange(1,11))

#3.Create an array of all zeros of size 5.
print(np.zeros(5))

#4.Create an array of all ones of shape (3,3).
print(np.ones((3,3)))

#5.Create an array of even numbers from 2 to 20.
print(np.arange(2,20,2))

#6.Create a 5×5 identity matrix.
print(np.eye(5,5))

#7.Create an array using linspace() from 0 to 1 with 10 values.
print(np.linspace(0,1,10))

#8.Create an array using arange() with step size 0.5.
print(np.arange(0,5,0.5))

#9.Check the type of a NumPy array.
print(type(np.zeros(5)))

#10.Convert a Python list into a NumPy array.
lst=[1,2,3]
arr=np.array(lst)
print(arr)








































