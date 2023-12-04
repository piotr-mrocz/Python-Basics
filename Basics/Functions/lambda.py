#one line function
sum = lambda a,b: a + b

print("Add")
print(sum(1, 2))
print(sum(5, 10))
print(sum(12, 5))

print()
print("Multiple")

def multiple(n):
    return lambda a: a * n

doubler = multiple(2) # 2 will be remeber by n

print(doubler(3))
print(doubler(6))
print(doubler(1))