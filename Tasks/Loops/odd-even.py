numbers = []
val = -4

while val <= 4:
    numbers.append(val)
    val += 1


for num in numbers:
    if (num == 0):
        print("0")
    elif (num % 2 == 0):
        print(f"{num} - Even")
    else:
        print(f"{num} - Odd")