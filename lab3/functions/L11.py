def isPalindrome(string):
    for i in range(int(len(string)/2)):
        if(string[i] != string [-(i+1)]):
            return False
    return True

# string = str(input())
# print(isPalindrome(string))