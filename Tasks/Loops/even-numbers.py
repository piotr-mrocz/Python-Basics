numbers = ()
num = 1

while num <= 10:
    numbers += (num,) # without , Python doesn't know that this is tuple
    num += 1

for num in numbers:
    if (num % 2 == 0):
        print(num)