s = input()
countUp = 0
countLow = 0
for i in s:
    countUp += int(i.isupper())
    countLow += int(i.islower())
print(countUp, countLow, sep="\n")
# print(f'uppecase {sum([1 if str(i).isupper() else 0 for i in s])}')
# print(f'lowercase {sum([1 if str(i).islower() else 0 for i in s])}')    