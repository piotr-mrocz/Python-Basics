numbers = [ -3, -2, -1, 0, 1, 2, 3 ]
values = { -1 }

for num in numbers:
    if (num % 2 != 0):
        values.add(num)

for num in values:
    print(num)
