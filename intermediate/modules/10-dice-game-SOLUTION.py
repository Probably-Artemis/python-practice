"""
Objective: write a dice game. Over three rounds, the user and the computer each roll two six-sided dice, and whoever has the higher total wins the round, or it is a tie. Before each roll, the user presses enter. Output both totals and the winner of every round, then the overall winner, whoever won more rounds. Split the program into at least two functions.
"""

import random


def roll_two():
    return random.randint(1, 6) + random.randint(1, 6)

def play_round(number):
    input(f"Round {number}: press enter to roll.")

    player = roll_two()
    computer = roll_two()

    print("You rolled", player, "and the computer rolled", computer)

    if player > computer:
        print("You win the round.")
        return "player"
    elif computer > player:
        print("The computer wins the round.")
        return "computer"
    print("This round is a tie.")
    return "tie"

player_wins = 0
computer_wins = 0

for number in range(1, 4):
    winner = play_round(number)
    if winner == "player":
        player_wins += 1
    elif winner == "computer":
        computer_wins += 1

if player_wins > computer_wins:
    print("You win the game!")
elif computer_wins > player_wins:
    print("The computer wins the game.")
else:
    print("The game is a tie.")