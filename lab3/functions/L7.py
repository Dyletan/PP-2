import re
def det(l):
    string = ""
    for ch in l:
        string += str(ch)
    print(string)
    if "33" in string: return True
    else: return False
    
# l = [1, 3, 1, 3, 3]
# print(det(l))