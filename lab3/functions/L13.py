import random
def play():
    name = str(input("Hello! What is your name?\n"))

    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    count = 1
    randomm = random.randrange(1, 20)
    guess = int(input("Take a guess.\n"))
    while(guess != randomm):
        if(guess < randomm):
            print("Your guess is too low")
        if(guess > randomm):
            print("Your guess is too high")
        count += 1
        guess = int(input("Take a guess.\n"))
    print("Good job, " + name + "! You guessed my number in", count, "guesses!")