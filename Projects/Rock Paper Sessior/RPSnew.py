"""
1 = rock, 2 = paper, 3 = sessior

1) letting computer choose rock or paper sessior
"""

import random

while True:
    choices = ["r", "p", "s"]
    get_emoji = {"r": "🪨", "p": "📰", "s": "✂️"}
    computerChoise = random.choice(choices)
    playerChoise = input("r/p/s: ").lower()

    if playerChoise not in choices:
        print("Invalid choice, please choose 'r', 'p', or 's'.")
        continue

    print(f"Player choose: {get_emoji[playerChoise]}")
    print(f"Computer choose: {get_emoji[computerChoise]}")
    if computerChoise == playerChoise:
        print("It's a draw!")
    elif (
        (computerChoise == "r" and playerChoise == "p")
        or (computerChoise == "r" and playerChoise == "s")
        or (computerChoise == "p" and playerChoise == "s")
    ):
        print("player won")
    else:
        print("computer won")
        doContinue = input("want to continue (y/n): ").lower()
        if doContinue == "n":
            print("thanks for playing")
            break
