import os

main_folder = "practice_folder"
sub_folder1 = os.path.join(main_folder, "documents")
sub_folder2 = os.path.join(main_folder, "images")

os.makedirs(sub_folder1, exist_ok=True)
os.makedirs(sub_folder2, exist_ok=True)

print("Directories created.\n")

with open(os.path.join(sub_folder1, "notes.txt"), "w") as file:
    file.write("This is a text file")

with open(os.path.join(sub_folder1, "data.csv"), "w") as file:
    file.write("id,name\n1,Miras")

with open(os.path.join(sub_folder2, "photo.jpg"), "w") as file:
    file.write("fake image content")

print("Files and folders inside practice_folder:")
for item in os.listdir(main_folder):
    print(item)

print()

print("Finding .txt files:")
for root, dirs, files in os.walk(main_folder):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))