import os
#program to list only directories
path = r"C:\PyhtonPractice"
files_and_directories = os.listdir(path)
for item in files_and_directories:
    #os.path.join() joins the path and the item we are iterating through to create a full path
    if os.path.isdir(os.path.join(path, item)):
        print(item)
print()
#program to list directories AND files in a specified path
for item in files_and_directories:
    print(item)
print()
#program to list only files
for item in files_and_directories:
    #join() joins the path and the item we are iterating through to create a full path
    if os.path.isfile(os.path.join(path, item)):
        print(item)