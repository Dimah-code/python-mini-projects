def judge(true, choice, num, hp):
    mydict = {"1": str(num), "2": "hip", "3": "hop", "4": "hiphop", "0": "exit"}
    if true == mydict[choice]:
        return mydict[choice], hp
    elif choice == "0":
        return "exit", hp
    else:
        hp -= 1
        print(f"INCORRECT!! correct answer is {true}")
        print(f"{hp} hp remaining")
        return mydict[choice], hp


def machine(num):
    if num % 3 == 0 and num % 5 == 0:
        return "hiphop"
    elif num % 5 == 0:
        return "hop"
    elif num % 3 == 0:
        return "hip"
    else:
        return str(num)


def playerchoice(num, hp):
    print("1. number")
    print("2. hip")
    print("3. hop")
    print("4. hiphop")
    print("0. End the game")

    choice = input("Enter your choice: ")
    true = machine(num)
    result, hp = judge(true, choice, num, hp)
    return result, hp


hp = 3
end_game = False
start = 0

while not end_game:
    start += 1
    machine_choice = machine(start)
    print(f"Machine: {machine_choice}")

    start += 1
    player_choice, hp = playerchoice(start, hp)
    print(f"Your choice: {player_choice}")
    if player_choice == "exit" or hp == 0:
        end_game = True
