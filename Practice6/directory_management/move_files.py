# directory_management/move_files.py

import os
import shutil

source_dir = os.path.join("practice_folder", "documents")
target_dir = os.path.join("practice_folder", "backup")

os.makedirs(target_dir, exist_ok=True)

source_file = os.path.join(source_dir, "notes.txt")
copied_file = os.path.join(target_dir, "notes_copy.txt")
moved_file = os.path.join(target_dir, "data.csv")

# Copy file
if os.path.exists(source_file):
    shutil.copy(source_file, copied_file)
    print(f"Copied {source_file} to {copied_file}")
else:
    print("Source file for copying not found")

# Move file
csv_file = os.path.join(source_dir, "data.csv")
if os.path.exists(csv_file):
    shutil.move(csv_file, moved_file)
    print(f"Moved {csv_file} to {moved_file}")
else:
    print("Source file for moving not found")