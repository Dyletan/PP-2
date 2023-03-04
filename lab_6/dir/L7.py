import os
path_original = r"C:\PyhtonPractice\list.txt"
path_copy = r"C:\PyhtonPractice\copy.txt"
with open(path_original, "r") as original:
    with open(path_copy, "w") as copy:
        for line in original:
            copy.write(line)

#check if copied
with open(path_copy, "r") as copy:
    print(copy.read())