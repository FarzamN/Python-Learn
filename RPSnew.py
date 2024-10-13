"""
1 = rock, 2 = paper, 3 = sessior

1) letting computer choose rock or paper sessior
"""

import random

while True:
    computerChoise = random.choice(["r", "p", "s"])
    playerChoise = input("r/p/s: ").lower()

    def get_emoji(choice):
        if choice == "r":
            return "🪨"
        elif choice == "p":
            return "📰"
        elif choice == "s":
            return "✂️"

    # Display both choices with emojis
    print(f"Computer chose: {get_emoji(computerChoise)}")
    print(f"Player chose: {get_emoji(playerChoise)}")

    if playerChoise not in ["r", "p", "s"]:
        print("Invalid choice, please choose 'r', 'p', or 's'.")
        continue
    if computerChoise == playerChoise:
        print("It's a draw!")
    elif (
        (computerChoise == "r" and playerChoise == "p")
        or (computerChoise == "p" and playerChoise == "S")
        or (computerChoise == "r" and playerChoise == "s")
    ):
        print("player won")
    else:
        print("computer won")
        doContinue = input("want to continue (y/n): ").lower()
        if doContinue == "n":
            print("thanks for playing")
            break
