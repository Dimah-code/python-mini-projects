'''
let's play X or O with computer..the real name of game is TIC TAC TOE..
'''
import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
win =[(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8),(0,4,8), (2,4,6)]
def number_hint():
    print("//game key hint")
    print(" "* 10, "1 | 2 | 3")
    print(" "* 10, "-"*9)
    print(" "* 10, "4 | 5 | 6")
    print(" "* 10, "-"*9)
    print(" "* 10, "6 | 7 | 8")
    print()
    print("-"* 36)

def show_board():
    print(" "* 10, board[0], "|", board[1], "|", board[2])
    print(" "* 10, "-"*9)
    print(" "* 10, board[3], "|", board[4], "|", board[5])
    print(" "* 10, "-"*9)
    print(" "* 10, board[6], "|", board[7], "|", board[8])

def computer_move():
    empty_blocks = [i for i in range(9) if board[i] == " "]

    for i in empty_blocks:
        board[i] = "O"
        if check_win("O"):
            return
        board[i] = " "

    for i in empty_blocks:
        board[i] = "X"
        if check_win("X"):
            board[i] = "O" 
            return
        board[i] = " "

    choice = random.choice(empty_blocks)
    board[choice] = "O"

def check_win(symbol):
    for a, b, c in win:
        if board[a] == symbol and board[b] == symbol and board[c] == symbol:
            return True
    
    return False

number_hint()
print("-"* 10, "let's play X,O", "-"* 10)

while True:
    show_board()
    try:
        player_move = int(input("choose one of the empty blocks by sending number 1-9\n 0 => EXIT\n"))-1
    except ValueError:
        print("please enter a number between 1 & 9")
        continue
    if player_move == -1:
        break
    if player_move > 8 or player_move < -1:
        print("please enter a number between 1 & 9")
        continue
    
    if board[player_move] == " ":
        board[player_move] = "X"
    else:
        print("the blocks is not empty")
        continue

    if check_win("X"):
        show_board()
        print("*"* 10, "YOU WON", "*"*10)
        break
    
    if " " not in board:
        show_board()
        print("*"* 10,"IT'S DRAW", "*"* 10)
        break

    computer_move()
    if check_win("O"):
        show_board()
        print("*"* 10, "YOU LOSE", "*"* 10)
        break

