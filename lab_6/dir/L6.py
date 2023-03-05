import os
path = r"C:\PyhtonPractice\folder"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in upper:
    os.chdir(path)
    open(letter + ".txt", 'a').close()