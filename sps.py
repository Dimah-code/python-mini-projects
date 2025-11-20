'''
sessior paper stone game let's play
'''
import random

answer = input("sessior,paper or stone?choose on of them and type: \n")

ai = random.randint(1,3)
if ai == 1 :
    computer_answer = "paper"
elif ai == 2 :
    computer_answer = "sessior"
else :
    computer_answer = "stone"

if computer_answer == answer :
    print("unlucky !!!!!!!it's DRAW!!!!!!!")
    print("computer answer= ",computer_answer)
elif computer_answer == "paper" and answer == "stone" :
    print("!!!!!!!you LOSE!!!!!!!")
    print("computer answer= ",computer_answer)
elif computer_answer == "paper" and answer == "sessior" :
    print("!!!!!!!you WON!!!!!!!")
    print("computer answer= ",computer_answer)
elif computer_answer == "sessior" and answer == "paper" :
    print("!!!!!!!you LOSE!!!!!!!")
    print("computer answer= ",computer_answer)
elif computer_answer == "sessior" and answer == "stone" :
    print("!!!!!!!you WON!!!!!!!")
    print("computer answer= ",computer_answer)
elif computer_answer == "stone" and answer == "sessior" :
    print("!!!!!!!you LOSE!!!!!!!")
    print("computer answer= ",computer_answer)
elif computer_answer == "stone" and answer == "paper" :
    print("!!!!!!!you WIN!!!!!!!")
    print("computer answer= ",computer_answer)

