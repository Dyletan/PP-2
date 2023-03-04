path = r"C:\PyhtonPractice\list.txt"
count = 0
ls = ["hello", "world", "how", "are", "you"]
with open(path, 'a') as file:
    for item in ls:
        file.write(item + " ")

#check if added items from list
with open(path, 'r') as file:
    print(file.read())
