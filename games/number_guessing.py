import random
import time


def hint(user: int, computer: int) -> str:
    if user < computer:
        return "Hint: Your number is less than computers'"
    else:
        return "Hint: Your number is more than computers'"

def difficulty() -> int:
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty = int(input("Choose difficulty (1, 2, 3): "))
    if difficulty == 1:
        return 25, "easy"
    elif difficulty == 2:
        return 45, "medium"
    elif difficulty == 3:
        return 70, "hard"

score = 1000
loss_point, game_type = difficulty()
user_number = -1
computer_number = random.randint(1, 100)
game_over = 400

print("="*60)
print(f"You have {score} points")
print(f"Each mistake costs {loss_point} points.")
print("="*60)

while user_number != computer_number:
    user_number = int(input("Guess a number between 1 and 100: "))
    if user_number == computer_number:
        print("You guessed right!")
        break
    else:
        print("You guessed wrong. Try again!")
        print(hint(user_number, computer_number))
    score -= loss_point
    print(f"You have {score} point")
    time.sleep(1.4)
    if score < game_over:
        print("You lost!!")
        print(f"Your points less than {game_over}")
        print(f"Computer number: {computer_number}")