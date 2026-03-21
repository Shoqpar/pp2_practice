import shutil
import os

source_file = "sample.txt"
copy_file = "sample_copy.txt"
backup_file = "sample_backup.txt"

# Copy file
if os.path.exists(source_file):
    shutil.copy(source_file, copy_file)
    print(f"{source_file} copied to {copy_file}")
else:
    print(f"{source_file} does not exist")

# Backup file
if os.path.exists(source_file):
    shutil.copy(source_file, backup_file)
    print(f"{source_file} backed up as {backup_file}")
else:
    print(f"{source_file} does not exist")

# Delete copied file safely
if os.path.exists(copy_file):
    os.remove(copy_file)
    print(f"{copy_file} deleted safely")
else:
    print(f"{copy_file} not found, nothing to delete")