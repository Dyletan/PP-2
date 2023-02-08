def spy_game(nums):
    string = ""
    for ch in nums:
        if ch == 0 or ch == 7:
            string += str(ch)
    if "007" in string: return True
    else: return False

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7])) 
# print(spy_game([1,7,2,0,4,5,0])) 