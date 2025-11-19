n = int(input("enter a number you want to search: "))
numbers = [1,3,5,7,9,10,13,15,17,19]

Min = 0
Max = len(numbers) - 1
found = -1
print(Max,Min)

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
