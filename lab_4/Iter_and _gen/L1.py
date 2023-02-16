def sqGen(n):
    count = 1
    while count <= n:
        yield count ** 2
        count += 1
n = sqGen(5)
print(type(n))