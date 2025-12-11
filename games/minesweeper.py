'''
simple Minesweeper game code for learning how does it work
'''
import random
import time
import threading
import os


def create_board(size=5,mines=5):
    board = [["□" for _ in range(size)] for _ in range(size)]
    mine_positions = set()
    while len(mine_positions) < mines:
        mine_positions.add((
            random.randint(0,size-1),
            random.randint(0,size-1)
        ))
           
    return board, mine_positions

def print_board(board):
    print(f"            | ⏱️ TIME: {minutes}:{elapsed_time:02} |")
    size = len(board)
    print("\n   ", " ".join(f"{i:2}" for i in range(size)))
    
    print("   ", "---" * size)

    for r in range(size):
        row = " ".join(f"{cell:2}" for cell in board[r])
        print(f"{r:2} | {row}")
    
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def neighbors_count(r, c, mine_positions, size):
    neighbors = [
    (r-1,c-1), (r-1,c), (r-1,c+1),
    (r,c-1),            (r,c+1),
    (r+1,c-1), (r+1,c), (r+1,c+1)
    ]
    adjacent_mines_count = 0
    for nr,nc in neighbors:
       if 0 <= nr < size and 0 <= nc < size:
           if (nr,nc) in mine_positions:
               adjacent_mines_count += 1
            
    return adjacent_mines_count

def flag_cell(r, c, board):
    
    if board[r][c] not in ["□","🚩"]:
        return False
    
    board[r][c] = "🚩" if board[r][c] == "□" else "□"
    return True
   
        

def open_cell(r, c, board, mine_positions, size, visited):
    
    if (r,c) in visited:
        return True
    visited.add((r,c))
        

    if (r, c) in mine_positions:
        for br,bc in mine_positions:
            board[br][bc] = "💣" 
        board[r][c] = "💥"
        print_board(board)
        print("\n💥 BOOM! You hit a mine. Game over.") 
        return False
    
    count = neighbors_count(r, c, mine_positions, size)
    board[r][c] = str(count)
    
    if count == 0 :
        neighbors = [
    (r-1,c-1), (r-1,c), (r-1,c+1),
    (r,c-1),            (r,c+1),
    (r+1,c-1), (r+1,c), (r+1,c+1)
    ]
        for nr, nc in neighbors:
            if 0 <= nr < size and 0 <= nc < size:
                open_cell(nr, nc, board, mine_positions, size, visited)
    
    return True

elapsed_time = 0
stop_time = False
minutes = 0

def live_time():
    global elapsed_time
    global minutes
    while not stop_time:
        time.sleep(1)
        elapsed_time += 1
        
        if elapsed_time == 60:
            minutes += 1
            elapsed_time = 0
                
        
        

size = 5
mines = 5
visited = set()
board,mine_positions = create_board(size)
time_thread = None
print("!the mines were planted!")


while True:
    clear()
    print_board(board)
    user_command = input("Enter you choice:(open/flag row col)\n EXIT= 0\n").split()
    
    if user_command[0] == "0":
        stop_time = True
        print("GOOD BYE!")
        break
    
    action = user_command[0].lower()
    if action not in ["open", "flag"]:
        print("invalid command,e.g:open 1 2")
        time.sleep(2)
        continue
    
    try:
        r = int(user_command[1])
        c = int(user_command[2])
           
    except (ValueError,IndexError):
        print("invalid command,e.g:open 1 2")
        time.sleep(1.5)
        continue
    
    if not (0 <= r < size and  0 <= c < size ):
        print("out of range")
        continue
    if time_thread == None:
        stop_time = False
        time_thread = threading.Thread(target=live_time)
        time_thread.start()
    
    if action == "open":  
        result = open_cell(r, c, board, mine_positions, size, visited)
        if not result:
            stop_time = True
            time_thread.join()
            print(f"\n           ⏱️ FINAL TIME: {minutes}:{elapsed_time:02} ")
            break
    elif action == "flag":
        result = flag_cell(r, c, board)
        if not result:
            print("you can't plant a flag on oppend cells!")
            continue
    
    if len(visited) == size * size - mines:
        stop_time = True
        time_thread.join()
        print_board(board)
        print("\n🎉 Congratulations! You won!")
        print(f"\n           ⏱️ FINAL TIME: {minutes}:{elapsed_time:02} ")
        break