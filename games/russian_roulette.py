'''
let's play russian roulette who will alive?
'''
import random
import time
import os

def random_shot(shot):
    gun_shot = random.randint(1,shot)
    gun_trigger = random.randint(1,shot)
    if gun_shot == gun_trigger:
        return True
    else:
        return False

def loading_time():
    bar = ["□"]*12
    for i in range(len(bar)):
        bar[i] = "▪"
        bar_str = "".join(bar)
        percent = int(((i+1) / len(bar))*100)
        print(f"\r loading: {bar_str} {percent}%", end=" ", flush=True)
        time.sleep(0.3)
    print()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
shot = 7
while True:
    clear()
    print("_"* 10, "russian roulette", "_"* 10)
    print(f"remianing cartridge: {shot}", " "* 10, "it's your turn\n")
    
    try:
        user_answer = input("Enter 's' to shot \n or 'x' to run away!")
        action = user_answer.lower()
    
        if action[0] not in ['s', 'x']:
            print("invalid answer!scard?")
            time.sleep(2)
            continue
    except (ValueError, IndexError):
        print("invalid answer!just say 's' or 'x'!")
        time.sleep(2)
        continue
    
    if action == 'x':
        print("hey man no way to escape,comeback to table!")
        time.sleep(2)
        continue
    elif action == 's':
        die = random_shot(shot)
        shot -= 1
        if die:
            print( "ᡕᠵデᡁ᠊╾━ ✷ your brain")
            print("war cartridge!you died!")
            break
        else:
            print("🔫 blank cartridge,do you want some water?\n")
            loading_time()
            
    print(" "* 10, "it's computer turn", " "* 10)
    computer_die = random_shot(shot)
    shot -= 1
    if computer_die:
        print( "ᡕᠵデᡁ᠊╾━ ✷ cpu")
        print("war cartridge!computer's cpu Exploded!")
        break
    else:
        print("🔫 blank cartridge,computer alived\n")
        loading_time()
        
         