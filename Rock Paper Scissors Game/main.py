# ROCK PAPER SCISSORS GAME
from random import randrange

keepPlaying = "yes"
pScore = 0
bScore = 0

ID = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "r": 1,
    "s": 3,
    "p": 2
}

while keepPlaying in ["yes", "y"]:
    # user input and random gen
    pInput = input("Chose rock, paper or scissors: ")
    pInput = pInput.lower()
    bInput = randrange(1, 4)
    # correct input check
    if pInput in ["rock", "r", "paper", "p", "scissors", "s"]:
        # display enemy choice
        bChoice = list(ID.keys())
        print("The enemy chose " + str(bChoice[bInput - 1]) + "\n")
        # check if you won or lost
        if ID[pInput] - bInput in [-1, 2]:
            bScore += 1
            print("You lost!")
        elif ID[pInput] - bInput == 0:
            print("You tied!")
        else:
            pScore += 1
            print("You won!")
    else:
        print("That is not a valid input\n")
        continue
    # check for if the player wants to keep playing
    keepPlaying = input("\nDo you want to play again? (yes/no)\n")

print("\nFinal Score: " + str(pScore) + " - " + str(bScore))
