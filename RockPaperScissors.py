'''
1 for Rock 
2 for Paper
3 for Scissor
'''
import random


computer = random.choice([1,2,3])
you = input("Choose a Value: ")

options = {"r":1, "p": 2, "s": 3}
RevOptions = {1:"r", 2:"p" , 3:"s"}

player = options[you]
print(f"computer chose {RevOptions[computer]} you chose {RevOptions[player]}")
if (computer == player):
    print("Game Drew")
else:
    if(computer == 1 and player == 2):
        print("You Win")
    elif(computer == 2 and player == 1):
        print("Computer Win")
    elif(computer == 1 and player == 3):
        print("Computer Win")
    elif(computer == 3 and player == 1):
        print("You Win")
    elif(computer == 3 and player == 2):
        print("computer Win")
    elif(computer == 2 and player == 3):
        print("You Win")
    else:
        print("Some Thing went wrong")



