"""
Bagels. A deductive logic game where you must guess a number based on clues
"""

import random


NUM_DIGITS = 3
MAX_GUESSES = 20


def title():
    """
    Navbar of game
    """
    print(
        f"\nI'm thinking of a {NUM_DIGITS} digit number \
          with no repeated digits "
    )
    print("=" * 30 + " RULES " + "=" * 30)
    print("\tWhen I say: \t That means:")
    print("\tPico \t\t One digit is correct but in the wrong position")
    print("\tFermi \t\t One digit is correct and in the right position")
    print("\tBagels \t\t No digit is correct")


def main():
    """
    Main loop of bagels game
    """
    title()
    while True:
        secret_number = make_secret_number()

        print("I have thought up a number.")
        print(f"You have {MAX_GUESSES} guesses to get it!")

        guess_count = 1

        guess_loop(secret_number, guess_count)

        print("Do you want to play again? (y/n) ")

        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for Playing!")


def get_clues(guess: str, secret_number: str) -> str:
    """
    Returns a string with the pico, fermi, bagels clues for a guess

    :param guess: The number that the user guessed
    :type guess: str
    :param secret_number: The number that the computer generated
    :type secret_number: str
    :return: Clue for user
    :rtype: str
    """
    if guess == secret_number:
        return "You got it!!!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append("Fermi")
        elif guess[i] in secret_number:
            clues.append("Pico")

    if len(clues) == 0:
        return "bagels"
    else:
        return " ".join(clues)


def make_secret_number() -> str:
    """
    Returns a string made up of NUM_DIGITS unique random digits.

    :return: Random number in string type
    :rtype: str
    """

    numbers = list("0123456789")
    random.shuffle(numbers)

    secret_number = ""

    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])
    return secret_number


def guess_loop(secret_number: str, guess_count: int):
    while guess_count <= MAX_GUESSES:

        guess = guess_validator(guess_count)

        clues = get_clues(guess, secret_number)
        print(clues)

        guess_count += 1

        if guess == secret_number:
            break
        if guess_count > MAX_GUESSES:
            print("You ran out of guesses!")
            print(f"The answer was {secret_number}")


def guess_validator(guess_count: int) -> str:
    guess = ""

    while len(guess) != NUM_DIGITS or not guess.isdecimal():
        print(f"Guess #{guess_count}: ")
        guess = input("> ")
    return guess


if __name__ == "__main__":
    main()
