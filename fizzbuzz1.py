print("Welcome to fizzbuzz! Let's play a new game - you can play as often as you want.")
while True:
        while True:
            try:
                enter = int(input("Pick a number between 1 and 100:"))
                if 1 <= enter <= 100:
                    for number in range(1, enter + 1):
                        if number % 3 == 0 and number % 5 == 0:
                            print("fizzbuzz")
                        elif number % 3 == 0:
                            print("fizz")
                        elif number % 5 == 0:
                            print("buzz")
                        else:
                            print(number)
                    break
                else:
                    print("Pleas try again and choose a number between 1 and 100. ")
            except ValueError:
                print("Please insert a number. ")
