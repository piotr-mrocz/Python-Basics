number = input("Write some number: ")
print(type(number))

number = int(number)
print(type(number))

number = float(number)
print(type(number))

number = str(number)
print(type(number))
print()

num = input("Write some number: ")
print(num)
print(f'You wrote {num}')
print('Second version of print: You wrote ', num)
print()

tuple = (1, 2, 3)
print(type(tuple))

tuple = list(tuple)
print(type(tuple))

tuple = set(tuple)
print(type(tuple))

tuple = frozenset(tuple)
print(type(tuple))