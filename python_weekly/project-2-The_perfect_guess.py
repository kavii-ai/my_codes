# The Perfect Guess game:) thats weekly project

import random

randno = random.randint(1,50)
# print(randno)
userguess = None
guesses = 0

while (userguess!=randno):
    userguess = int(input("Enter your guess:"))
    guesses += 1
    if userguess==randno:
        print("congradulations !! you guess it right,you are a winner.")
    else:
        if(userguess>randno):
            print("you guessed it wrong !! Enter a smaller number")
        else:
            print("you guessed it wrong !! Enter a larger number")


print(f"you guess the number in ::{guesses} guesses")

with open("highscore.txt","r") as f:
    highscore = int(f.read())

if (guesses<highscore):
    print("you have just broken the highscore!!")
    with open("highscore.txt","w") as f:
        f.write(str(guesses))
