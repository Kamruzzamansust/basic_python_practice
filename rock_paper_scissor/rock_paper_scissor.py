import random 

user_wins = 0
computer_wins = 0

while True:
    user_input = input("input Rock/Paper/Scissor or Q to Quit: ").lower()
    if user_input == "q":
        break
    if user_input not in ['rock','paper','scissor']:
        continue
    random_number = random.randint(0,3)
   # print(random_number)
    choice = None
    if random_number == 1:
        choice = 'rock'
    elif random_number == 2:
        choice =="paper"
    else:
        choice == "scissor"

    if choice == user_input:
     print("You win !")
     user_wins +=1
    else:
     computer_wins+=1
     print("you lost!")
     

print("GoodBye !!!!!")
print("you wins ", user_wins)
print("computer wins",computer_wins)

    