"""
rock paper scissors game let's play
"""

import random

end = True
player_point = 0
computer_point = 0
while end:
    print("AI =", computer_point, "YOU =", player_point)
    answer = input("rock,paper and scissors?choose on of them and type: \n")

    if answer == "scissors":
        pass
    elif answer == "paper":
        pass
    elif answer == "rock":
        pass
    else:
        print("you did't choose invalid answer")
        continue

    ai = random.randint(1, 3)
    if ai == 1:
        computer_answer = "paper"
    elif ai == 2:
        computer_answer = "scissors"
    else:
        computer_answer = "rock"

    if computer_answer == answer:
        print("unlucky !!!!!!!it's DRAW!!!!!!!")
        print("computer answer= ", computer_answer)
    elif computer_answer == "paper" and answer == "rock":
        print("!!!!!!!you LOSE!!!!!!!")
        computer_point += 1
        print("computer answer= ", computer_answer)
    elif computer_answer == "paper" and answer == "scissors":
        print("!!!!!!!you WON!!!!!!!")
        player_point += 1
        print("computer answer= ", computer_answer)
    elif computer_answer == "scissors" and answer == "paper":
        print("!!!!!!!you LOSE!!!!!!!")
        computer_point += 1
        print("computer answer= ", computer_answer)
    elif computer_answer == "scissors" and answer == "rock":
        print("!!!!!!!you WON!!!!!!!")
        player_point += 1
        print("computer answer= ", computer_answer)
    elif computer_answer == "rock" and answer == "scissors":
        print("!!!!!!!you LOSE!!!!!!!")
        computer_point += 1
        print("computer answer= ", computer_answer)
    elif computer_answer == "rock" and answer == "paper":
        print("!!!!!!!you WIN!!!!!!!")
        player_point += 1
        print("computer answer= ", computer_answer)
    if computer_point == 3:
        print("!!!!!!the computer is the finalist WINNER!!!!!!!")
        end = False
    elif player_point == 3:
        print("!!!!!!!you are the finalist WINNER!!!!!!!")
        end = False
print("!!!!!!! AI =", computer_point, "YOU =", player_point, "!!!!!!!")
