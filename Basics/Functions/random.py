import random
print(random.random())


print()

print(f"Random number in list [1, 2, 3] = {random.choice([1, 2, 3])}")

print()

# random.randrange(0, 25, 5)
# start, stop, step
print(f"Random number in range = {random.randrange(0, 25, 5)}")

print()

print("Random ordered list")
listData = [ 0, 1, 2, 3, 4, 5 ]
print(listData)

random.shuffle(listData)
print(listData)

print()

print(f"Random number uniform = {random.uniform(5, 10)}")