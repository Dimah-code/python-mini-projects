"""
This file for finding number with binary search
"""

numbers = []
length_numbers = int(input("how many number do you want to enter "))
for i in range(length_numbers):
    temp = int(input(f"Enter number {i+1} : "))
    numbers.append(temp)
n = int(input("enter a number you want to search: "))

Min = 0
Max = len(numbers) - 1
found = -1

while Min <= Max:
    Mid = (Min + Max) // 2

    if numbers[Mid] == n:
        found = Mid
        break
    elif n > numbers[Mid]:
        Min = Mid + 1
    else:
        Max = Mid - 1

if found == -1:
    print("not found")
else:
    print("the index of number is", found)
