import json
import random
import datetime

secret=random.randint(1,10)
attempts=0

print("Welcome to this wonderful 'Guess the right number' game")

with open("scoreboard.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
name=str(input("Please insert your name: "))

while True:

    guess=int(input("Guess a number (between 1 and 10): "))
    attempts+=1

    if guess == secret:
        score_list.append({"name": str(name),"attempts": attempts, "date": str(datetime.datetime.now())})

        with open("scoreboard.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Well done, it's "+str(secret))
        print("Attempts needed: "+str(attempts))
        break

    elif guess > secret:
     print("The number is smaller than " +str(guess)+ ". Try again!")

    elif guess < secret:
     print("The number is bigger than " +str(guess)+ ". Try again!")

    else:
     print("Try again! It's not ",str(guess),"- choose a number between 1 and 10.")