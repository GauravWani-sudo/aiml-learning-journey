with open("sample.txt", "w") as file:
    file.write("python file handling")

with open("sample.txt", "r") as file:
    data = file.read()

print(data)