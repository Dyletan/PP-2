import os
path = r"C:\PyhtonPractice\folder"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in upper:
    os.chdir(path)
    os.mkdir(letter + ".txt")