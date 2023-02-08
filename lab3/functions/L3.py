def solve(numheads, numlegs):
    chick = numheads
    rab = 0
    while(numlegs > 0):
        if(numheads == rab+chick and rab*4+chick*2 == numlegs):
            print("There are", rab, "rabbits and", chick, "chickens")
            break
        else:
            rab += 1
            chick -= 1

# solve(35, 94)