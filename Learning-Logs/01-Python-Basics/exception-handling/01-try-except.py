try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print("cannot divide by zero")