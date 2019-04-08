
# -- 

from os import walk
import glob
import os
from os import listdir
from os.path import isfile, join

def walk_dir():
    mypath = u"."
    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
        break

    print (f)

# -- 

def walk_local_files():
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    print (onlyfiles)


def walk_recursive_files():
    print ("List all .txt files in a specified directory + subdirectories")

    path = '.'

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

    for f in files:
        print(f)




def walk_dirs():
    print("List all directories in a specified directory + subdirectories")
    path = mypath

    folders = []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for folder in d:
            folders.append(os.path.join(r, folder))

    for f in folders:
        print(f)




def glob_files(path):
    print("Glob: List all .txt files in a specified directory + subdirectories (**).")

    files = [f for f in glob.glob(path + "**/*", recursive=True)]

    print("ho trovato: ", len(files), " files")
    return files
    


def glob_dirs(path):
    print("Glob: List all DIRS specified directory + subdirectories (**).")

    folders = [f for f in glob.glob(path + "**/", recursive=True)]

    for f in folders:
        print(f)



if __name__ == '__main__':
    files = glob_files("./")

    # import os   
    conta = {}
    for f in files:
        filename, file_extension = os.path.splitext(f)
        conta[file_extension] = conta.get(file_extension,0)+1

    ## from collections import Counter
    ## Counter()

    from collections import OrderedDict
    dd = OrderedDict(sorted(conta.items(), key=lambda x: x[1], reverse=True) )

    i = 0
    for k, v in dd.items():
        print(k, v)
        i += 1
        if i > 40: 
            break

    def off():
        for k, v in conta.items():
            if v>1:
                print(k, v)

    #for f in files:
    #    print(f)

