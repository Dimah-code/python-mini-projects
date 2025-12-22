"""
Birthday paradox or birthday porblem
Simulation birthdays to show the birthday paradox
"""

from datetime import date, timedelta
from random import randint


def get_birthdays(number_of_birthdays) -> list:
    """
    Returns a list of number random date objects for birthdays

    :param number_of_birthdays: Number of birthdays that computer must create
    :return: list of random birthdays
    :rtype: list
    """

    birthdays = []

    for i in range(number_of_birthdays):
        start_year = date(2025, 1, 1)

        random_day_number = timedelta(randint(0, 364))

        birthday = start_year + random_day_number
        birthdays.append(birthday)

    return birthdays


def get_match(birthdays: list) -> date:
    """
    Returns the date object or a birthday that occurs more than once

    :param birthdays: List of random birhtdays
    :type birthdays: list
    :return: The date object or a birthday that occurs more than once
    :rtype: date
    """

    if len(birthdays) == len(set(birthdays)):
        return None

    for first, first_birthday in enumerate(birthdays):
        for second, second_birthday in enumerate(birthdays[first + 1 :]):
            if first_birthday == second_birthday:
                return first_birthday


MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Nov",
    "Oct",
    "Dec",
)

while True:
    print("How many birthdays shell I generate? (Max 100)")
    response = int(input(">"))

    if response >= 100:
        continue
    break

print("Here are", response, "birthdays:")
birthdays = get_birthdays(response)

for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ", end="")
        month_name = MONTHS[birthday.month - 1]
        date_text = f"{month_name} {birthday.day}"
        print(date_text, end="")
print("\n\n")

match = get_match(birthdays)

print("In this simulation, ", end="")
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = f"{month_name} {match.day}"
    print("Multiple people have a birthday on", date_text)
else:
    print("There are no matching birthdays.")

print()


# Run through 100000 simulations
print("Generating", response, "random birthdays 100,000 times...")
input("Press Enter to begin...")

print("Let's run another 100,000 simulation")
simulation_match = 0

for i in range(100_000):
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = get_birthdays(response)
    if get_match(birthdays) != None:
        simulation_match = simulation_match + 1

print("100,000 simulations run")

probability = round(simulation_match / 100_000 * 100, 2)

print("Out of 100,000 simulations of", response, "people, there was a")
print("matching birthday in that group", simulation_match, "times. This means")
print("that", response, "people have a", probability, "% chance of")
print("having a matching birthday in their group.")
print("That's probably more than you would think!")
