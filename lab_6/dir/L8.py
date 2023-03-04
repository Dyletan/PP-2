import os
os.chdir(r"C:\PyhtonPractice")

#create a file we want to delete
open("ready_to_delete.txt", 'a').close()

#check if the file was created
print(os.listdir())

#delete
path = r"C:\PyhtonPractice\ready_to_delete.txt"
os.remove(path)

#check if deleted
print(os.listdir())