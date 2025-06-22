name  = input(" Type Your Name:")
print("welcome", name ,"to this adventure!")

answer =  input(
    
    "You are on a dirt road , it has come to an end  and you can go left or right . which way would you like to go? "
    
    ).lower()



if answer == "left":
    answer = input("You come to a river, Now you can walk away or you can swim . type walk to walk away or swim to swim: ").lower()
    if answer == "swim":
        print("You swim across and were eaten by a alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You loos !!!")

elif answer == "right":
    print("You fall into a hole. Game Over")

else: 
    print("Not a valid option. You loos !!!")