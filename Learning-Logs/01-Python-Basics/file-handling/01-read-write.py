file = open("sample.txt", "w")

file.write("hello world")

file.close()

file = open("sample.txt", "r")

data = file.read()

print(data)

file.close()