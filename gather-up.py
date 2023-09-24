import os
import sys
import shutil

# os methods
abspath = os.path.abspath
listdir = os.listdir

# shutil methods
move = shutil.move

# sys.argv[1] is your source folder. Any photos inside subdirectories here will
# be copied to a folder at the top level of this folder called 'Gathered Images' on execution.

# For example, 'python gather-up.py ~/Desktop/images' will search
# through all subfolders of /images and move all files to the top level.

# If there are duplicate filenames, you will be prompted to overwrite or skip by the OS.

src_folder = abspath(sys.argv[1])

print("Source Folder:" + src_folder)
print("Gathering images...")

# Create a new folder called 'Gathered Images' in the source folder
gathered_images_folder = src_folder + "/_Gathered-Images"
if not os.path.exists(gathered_images_folder):
    os.makedirs(gathered_images_folder)

# Walk through all subdirectories of the source folder, add files to memory
filelist = []

for root, dirs, files in os.walk(src_folder):
    for file in files:
        filelist.append(os.path.join(root, file))

print(filelist)

# Move all files to the new folder
for file in filelist:
    move(file, gathered_images_folder)
