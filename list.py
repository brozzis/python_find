
# -- 

from os import walk

mypath = u"."
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

print (f)

# -- 

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print (onlyfiles)

# -- 
# List all .txt files in a specified directory + subdirectories

print ("List all .txt files in a specified directory + subdirectories")
import os

path = '.'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)


print("List all directories in a specified directory + subdirectories")
import os

path = mypath

folders = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for folder in d:
        folders.append(os.path.join(r, folder))

for f in folders:
    print(f)


print("Glob: List all .txt files in a specified directory + subdirectories (**).")


import glob

path = mypath

files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]

for f in files:
    print(f)


print("Glob: List all DIRS specified directory + subdirectories (**).")

import glob

folders = [f for f in glob.glob(path + "**/", recursive=True)]

for f in folders:
    print(f)


