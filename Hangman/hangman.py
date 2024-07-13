# HANGMAN
from random import randrange

# hangman stages
hangmanVisual = ["""
          
          
          
          
           """, """
          
          
          
          
        ===""", """
          
         |
         |
         |
        ===""", """
     +---+
         |
         |
         |
        ===""", """
     +---+
     o   |
         |
         |
        ===""", """
     +---+
     o   |
     |   |
         |
        ===""", """
     +---+
     o   |
    /|   |
         |
        ===""", """
     +---+
     o   |
    /|\  |
         |
        ===""", """
     +---+
     o   |
    /|\  |
    /    |
        ===""", """
     +---+
     o   |
    /|\  |
    / \  |
        ==="""]

words = open('words.txt','r').read().split()

# chose a random word from list
cW = words[randrange(0, len(words))]
wrong = 0
word = ""
usedList = []

# create the hidden word
for i in cW:
    word += "_"


# find indexes of given character in a string
def find(string, ch):
    return [j for j, ltr in enumerate(string) if ltr == ch]


while wrong < 9 and word != cW:

    # user input
    pIn = input("Enter a letter: ")

    # check if input is alphabetical and length is 1
    if pIn.isalpha() and len(pIn) == 1:
        pIn = pIn.lower()

        # check if input has already been used
        if pIn in usedList:
            print("This letter has already been used")
            continue
        else:
            usedList.append(pIn)

            # check if the letter is in the chosen random word
            if pIn in cW:
                indexes = find(cW, pIn)
                for index in indexes:
                    word = word[:index] + pIn + word[index + 1:]
            else:
                wrong += 1

        print(hangmanVisual[wrong])
        print(" " + word + "\n")
    else:
        print("This input is invalid")
        continue

# check if the player won or lost
if word == cW:
    print(f""" \n\n
    ****************************************

        You Win! The word was {cW}

    ****************************************
    """)
else:
    print(f""" \n\n
    ****************************************

        You Lose! The word was {cW}

    ****************************************
    """)
