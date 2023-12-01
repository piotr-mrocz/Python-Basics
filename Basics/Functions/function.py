# def - define new function

def addNumbers(number1, number2):
    return number1 + number2;


print(addNumbers(1, 2))
print(addNumbers(1, 5))
print(addNumbers(1, 10))

print()

def showSum(number1, number2):
    sum = number1 + number2

    if sum > 3:
        return

    print(f"Suma: {sum}")

showSum(1, 1)
showSum(1, 7)