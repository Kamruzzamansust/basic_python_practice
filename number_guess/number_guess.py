import random 


top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    print('Your Upper Number Number is ', top_of_range)
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()


random_number = random.randint(0,top_of_range)

while True:
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please type a number next time.')
        continue

    if guess == random_number:
        print("You got it!")
        break
    elif guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")