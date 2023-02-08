def uniqq(l):
    b = list()
    for i in range(len(l)):
        if l[i] not in b:
            b.append(l[i])
    return(b)

# print(uniqq([1,1,2,3,3,4,7,5,4,2,1,7, "a", "b", "a"]))