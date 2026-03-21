
filename = "sample.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File:")
        print(content)
except FileNotFoundError:
    print("File not found")