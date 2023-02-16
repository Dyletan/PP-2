def isDivBy3And4(n):
    count = 0
    while count <= n:
        if(count % 3 == 0 and count % 4 == 0):
            yield count
        count += 1
print(list(isDivBy3And4(100)))