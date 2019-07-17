
import random

secret=random.randint(1,10)
attempts=0

print("Welcome to this wonderful 'Guess the right number' game")

with open("scoreboard.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Top score (attempts): " + str(best_score))

while True:

    guess=int(input("Guess a number (between 1 and 10): "))
    attempts+=1

    if guess == secret:
        if attempts < best_score:
            with open("scoreboard.txt", "w") as score_file:
                score_file.write(str(attempts))
        print("Well done, it's "+str(secret))
        print("Attempts needed: "+str(attempts))
        break

    elif guess > secret:
     print("The number is smaller than " +str(guess)+ ". Try again!")

    elif guess < secret:
     print("The number is bigger than " +str(guess)+ ". Try again!")

    else:
     print("Try again! It's not ",str(guess),"- choose a number between 1 and 10.")