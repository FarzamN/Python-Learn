'''
point Game should loop untill user decide to terminate
1) If user enter Y
    Generate 2 rendom numbers
    print them

2) If user enter N
    print thank you message
    terminate

3) else 
    print invalid choice
'''

import random

while True:
    choice = input(f"select Y or N: ").lower()
    if choice == "y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"(result: {dice1},{dice2})")
    elif choice == "n":
        print("thank you to playing")
        break
    else: print("invalid choice")
