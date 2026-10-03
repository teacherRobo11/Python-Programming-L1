# ==========================================
# PYTHON LEVEL 1 - DAY 9
# MISSION 09 - ROCK PAPER SCISSORS
# ==========================================

import random

print("==============================")
print("    ROCK PAPER SCISSORS")
print("==============================")

choices = ["rock", "paper", "scissors"]

player = input("Choose rock, paper, or scissors: ")

computer = random.choice(choices)

print()
print("You chose:", player)
print("Computer chose:", computer)

# TODO:
# Compare player and computer choices


# TODO:
# Decide who wins


print("==============================")
print("          GAME OVER")
print("==============================")