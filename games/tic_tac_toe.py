'''
let's play X or O with computer..the real name of game is TIC TAC TOE..
'''
import random
import os
import time

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
win =[(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8),(0,4,8), (2,4,6)]
player_point = 0
computer_point = 0

def game_menu():
    clear()
    print("*"* 36)
    print(" "* 10, "TIC TAC TOE\n")
    print()
    print("1.EASY")
    print("2.NORMAL")
    print("3.HARD")
    print("*"* 36)
     
    while True:
        try:
            game_dificulty = int(input("choose the game dificulty you want to play 1-3 \n"))
        except ValueError:
            print("enter valid number 1-3")
            continue
        if game_dificulty > 3 or game_dificulty < 1:
            print("enter valid number 1-3")
            continue
        return game_dificulty
    
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def number_hint():
    clear()
    print("//game key hint")
    print(" "* 10, "1 | 2 | 3")
    print(" "* 10, "-"*9)
    print(" "* 10, "4 | 5 | 6")
    print(" "* 10, "-"*9)
    print(" "* 10, "7 | 8 | 9")
    print()
    print("-"* 36)
    time.sleep(3.5)

def reset_board():
    if computer_point == 3 or player_point == 3:
        pass
    else:
        for i in range(9):
            board[i] = " "


def show_board():
    print(" "* 10, board[0], "|", board[1], "|", board[2])
    print(" "* 10, "-"*9)
    print(" "* 10, board[3], "|", board[4], "|", board[5])
    print(" "* 10, "-"*9)
    print(" "* 10, board[6], "|", board[7], "|", board[8])

def computer_move(dificulty):
    empty_blocks = [i for i in range(9) if board[i] == " "]
    if dificulty == 1:
        choice = random.choice(empty_blocks)
    elif dificulty == 2:
        choice = normal_move(empty_blocks)
    elif dificulty == 3:
        choice = hard_move(empty_blocks)
    
    board[choice] = "O"

def normal_move(empty_blocks):
    
    for i in empty_blocks:
        board[i] = "O"
        if check_win("O"):
            board[i] = " "
            return i
        board[i] = " "

    for i in empty_blocks:
        board[i] = "X"
        if check_win("X"): 
            board[i] = " "
            return i
        board[i] = " "

    return random.choice(empty_blocks)
    

def hard_move(empty_blocks):
    
    if board[4] == " ":
        return 4  
     
    for i in empty_blocks:
        board[i] = "O"
        if check_win("O"):
            board[i] = " "
            return i
        board[i] = " "

    for i in empty_blocks:
        board[i] = "X"
        if check_win("X"): 
            board[i] = " "
            return i
        board[i] = " "
        
    betweens = [i for i in [1,3,5,7] if board[i] == " "]
    if (board [0] == "X" and board [8] == "X") or (board [2] == "X" and board [6] == "X"):    
        return random.choice(betweens)  
    
     
    corners = [i for i in [0,2,6,8] if board[i] == " "]
    if corners:
        return random.choice(corners)

    return random.choice(empty_blocks)
    


def check_win(symbol):
    for a, b, c in win:
        if board[a] == symbol and board[b] == symbol and board[c] == symbol:
            return True
    
    return False


dificulty = game_menu()
number_hint()
print("-"* 10, "let's play X,O", "-"* 10)

turn = random.choice(["player", "computer"])

while True:
    clear()
    print(" "* 4, "computer= ", computer_point," "* 4, "you= ",player_point)
    show_board()
    if computer_point == 3:
        print("*"* 10, "oh,sorry!computer is the finalist winner", "*"* 10)
        
        break
    
    if player_point == 3:
        print("*"* 10, "great..you are the finalist winner", "*"* 10)
        break
    
    if turn == "player":
        print("*" * 10, "now your turn", "*" * 10)
        try:
            player_move = int(input("choose one of the empty blocks by sending number 1-9\n 0 => EXIT\n"))-1
        except ValueError:
            print("please enter a number between 1 & 9")
            time.sleep(2.5)
            continue
        
        if player_move == -1:
            break
        
        if player_move > 8 or player_move < -1:
            print("please enter a number between 1 & 9")
            time.sleep(2.5)
            continue
        
        if board[player_move] == " ":
            board[player_move] = "X"
        else:
            print("the blocks is not empty")
            time.sleep(2.5)
            continue

        if check_win("X"):
            clear()
            show_board()
            print("*"* 10, "YOU WON", "*"*10)
            time.sleep(2.5)
            player_point += 1
            reset_board()
            turn = random.choice(["player","computer"])
            continue
        
        if " " not in board:
            clear()
            show_board()
            print("*"* 10,"IT'S DRAW", "*"* 10)
            time.sleep(2.5)
            reset_board()
            turn = random.choice(["player","computer"])
            continue
        
        turn = "computer"
    else:
        print("*" * 10, "computur turn", "*" * 10)
        time.sleep(2.5)
        computer_move(dificulty)
        if check_win("O"):
            clear()
            show_board()
            print("*"* 10, "YOU LOSE", "*"* 10)
            time.sleep(2.5)
            reset_board()
            computer_point += 1
            turn = random.choice(["player","computer"])
            continue
        
        if " " not in board:
            clear()
            show_board()
            print("*"* 10,"IT'S DRAW", "*"* 10)
            time.sleep(2.5)
            reset_board()
            turn = random.choice(["player","computer"])
            continue
        
        turn = "player"
    
    
