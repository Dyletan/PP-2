from itertools import permutations

def findPer(string):
    words = [''.join(perm) for perm in permutations(string)]
    print(set(words))

# string = str(input())