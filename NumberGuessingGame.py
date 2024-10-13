'''
computer will think a number
then user will type a number
computer will tell if number is higher or lower then which computer chose

same infinity loop
of user choose !number then print invalid number

'''

'''
Optional Enhancements
• Allow the user to specify the minimum and maximum values for the number
range before the game starts. This gives the player more control over the
difficulty level.

• Implement a feature that limits the number of guesses a player can make. If
the player runs out of attempts, the game should end, and the correct number
should be revealed.

• Add a feature that keeps track of the fewest attempts it took to guess the
number correctly. The program should display this "best score" at the end of
each game. 

'''
import random

computerNum = random.randint(1,100)
guessLength = {}
while True:
    try:
        choice = int(input('guess the number: '))
        guessLength[choice] = choice
        if computerNum > choice:
            print(" too low")
        elif computerNum < choice:
          print("too high")
        elif guessLength.items() < 3:
            print(f"limit is ended result was: {computerNum}")
            break
        else:
            print("Congiralation")
            break
    except ValueError:
            print("Invalid number. Please enter a valid integer.")
