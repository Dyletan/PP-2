def even(n):
    count = 0
    if n%2 == 1:
        count = 0
        n-= 1
    while count <= n:
        yield count
        count += 2

n = int(input())
print(list(even(n)))