import os
path = r"C:\PyhtonPractice"
if os.access(path, os.F_OK):
    #os.path.split() splits the path into a pair of a last path name and everythong leading up to it
    dir, file = os.path.split(path)
    print(f"The directory portion of the path is: {dir}")
    print(f"The filename portion of the path is: {file}")
else:
    print(f"The path {path} does not exist")