print("welcome to my computer quiz! ")

playing = input("Do you want to play? ")
score  = 0

if playing.lower() == "yes":
    print("Let's play The Game!!!!!!!!!!!!!!!")
else: 
    quit()

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
    score -= 0.5

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 0.5
answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    score -= 0.5

print("Your Total Score is : ", score)




