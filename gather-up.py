import os
import sys
import shutil

# os methods
abspath = os.path.abspath
listdir = os.listdir

# shutil methods
move = shutil.move

# sys.argv[1] is your source folder. Any photos inside subdirectories here will
# be copied to a folder at the top level of this folder called '_Gathered-Files' on execution.

# For example, 'python gather-up.py ~/Desktop/images' will search
# through all subfolders of /images and move all files to the top level.

# If there are duplicate filenames, you will be prompted to overwrite or skip by the OS.

# need to make it work for folders with a space in the name
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
        filelist.append(os.path.join(root, file))

# Move all files to the new folder
try:
    for file in filelist:
        # move file if it doesn't start with a period
        if file.endswith(".DS_Store"):
            print("Skipping " + file)
            continue
        else:
            move(file, gathered_files_folder)
            print("Moved " + file)

except Exception as err:
    print("Error moving some files: " + err)

print("Gathered up!")
