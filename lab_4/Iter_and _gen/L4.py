def squares(a, b):
    count = a
    while count >= a and count <= b:
        if int(count**0.5)**2 == count:
            yield count
        count +=1

for x in squares(100, 1000):
    print(x)