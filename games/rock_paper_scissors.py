"""
rock paper scissors game let's play
"""

import random
import time

def menu():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

def validation(answer: int) -> bool:
    valid_answers = [1, 2, 3, 0]
    if answer in valid_answers:
        return True
    else:
        return False

options_dict = {1: "Rock", 2: "Paper", 3: "Scissors"}

ROCK = 1
PAPER = 2
SCISSORS = 3

end = True
player_point = 0
computer_point = 0

while end:
    print("\t Computer:", computer_point, "You:", player_point)
    menu()
    try:
        player = int(input("Choose your option: \n"))
    except Exception as e:
        print("Enter a valid number 1, 2, 3")
        time.sleep(1)
        continue

    if not validation(player):
        print("You choose wrong option! Try again")
        time.sleep(1)

    computer = random.randint(1, 3)

    if computer == player:
        print("Woah! This round of play was tied!")
        print("Computer answer:", options_dict[computer])
    elif (
        (computer == ROCK and player == SCISSORS) or (computer == PAPER and player == ROCK) or
        (computer == SCISSORS and player == PAPER)
    ):
        print("You LOST! Did you lose to a computer?")
        computer_point += 1
        print("computer answer:", options_dict[computer])
    elif (
        (player == ROCK and computer == SCISSORS) or (player == PAPER and computer == ROCK)
        or (player == SCISSORS and computer == PAPER)
    ):
        print("You WON! Well Played!")
        player_point += 1
        print("computer answer:", options_dict[computer])

    if computer_point == 3:
        print("*"*30, "Computer WON! embarrassing", "*"*30)
        end = False
    elif player_point == 3:
        print("*"*30, "You WON! Congrats", "*"*30)
        end = False

print("\t Computer:", computer_point, "You:", player_point)
