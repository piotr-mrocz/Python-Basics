numbers = [0, 1, 2, 3, 4, 5, 6]

print(len(numbers))

del numbers[:2]
print(len(numbers))

if 3 in numbers:
	print("3 is in list")

print()

for element in numbers:
	print(element)