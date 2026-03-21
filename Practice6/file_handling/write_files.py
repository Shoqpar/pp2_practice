
filename = "sample.txt"

with open(filename, "w") as file:
    file.write("Nurali,85\n")
    file.write("Arman,90\n")
    file.write("Nurzhan,78\n")


with open(filename, "a") as file:
    file.write("Aizhan,92\n")
    file.write("Damir,88\n")


print("Final file content:")
with open(filename, "r") as file:
    content = file.read()
    print(content)