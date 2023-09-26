import os
import sys
import shutil
import datetime

# os methods
abspath = os.path.abspath
listdir = os.listdir

# shutil methods
copy = shutil.copy2

# sys.argv[1] is your source folder. Any photos inside subdirectories here will
# be copied to a folder at the top level of this folder called '_Gathered-Files' on execution.

# For example, 'python gather-up.py ~/Desktop/images' will search
# through all subfolders of /images and copy all files to a new top level folder.

# If there are duplicate filenames, you will be prompted to overwrite or skip by the OS.

src_folder = abspath(sys.argv[1])

print("Source Folder:" + src_folder)
print("Gathering files...")

# Create a new folder called 'Gathered' in the source folder
gathered_files_folder = src_folder + "/_Gathered-Files"
if not os.path.exists(gathered_files_folder):
    os.makedirs(gathered_files_folder)

# Walk through all subdirectories of the source folder, add files to memory
filelist = []

for root, dirs, files in os.walk(src_folder):
    for file in files:
        # ignore .DS_Store files
        if file.endswith(".DS_Store"):
            print("Skipping " + file)
            continue
        filelist.append(os.path.join(root, file))

print(filelist)

# Move all files to the new folder
try:
    for file in filelist:
        # check for duplicate names and rename if necessary
        # help from https://pythonguides.com/python-copy-file/
        head_tail = os.path.split(file)
        if os.path.exists(os.path.join(gathered_files_folder, head_tail[1])):
            print(f"{file} is a duplicate, renaming...")
            base_name = os.path.basename(file)
            new_file_name = (
                "duplicate_"
                + datetime.datetime.now().strftime("%H-%M-%S")
                + "_"
                + base_name
            )
            copied_file = os.path.join(gathered_files_folder, base_name)
            new_file = os.path.join(gathered_files_folder, new_file_name)
            os.rename(copied_file, new_file)
        copy(file, gathered_files_folder)
        print("Copied " + file)

except Exception as err:
    print(err)

print("Gathered up!")
