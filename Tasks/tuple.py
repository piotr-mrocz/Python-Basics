numbers = 50, 100, 150, 200, 250;

print(type(numbers))
print(len(numbers))
print()

# last element
print(numbers[(len(numbers) - 1)])
print(numbers[-1])
print()

print(numbers[1:4])
print(numbers[-3])
print()


expenses = 100, 200, 300, 400, 500, 600;
expensesSum = 0

for element in expenses:
    expensesSum += element

print(expensesSum)