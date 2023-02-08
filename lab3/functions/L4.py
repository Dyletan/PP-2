def filter_prime(listOfNum):
    ls = [int(x) for x in listOfNum.split()]
    return list(filter(lambda x: all(x%i != 0 for i in range(2,int(x**0.5)+1)) and x != 1, ls))


# print(filter_prime("1 2 3 4 5 6 7 8 9"))