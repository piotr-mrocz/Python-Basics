data = [ 0, 1, 2, 3, 4, 5 ]

for item in data:
    if item == 3:
        print(f"{item} + cintinue")
        continue
    
    print(item)

    if item == 4:
        print("break")
        break


# pass - do nothing, but we use it when we need some filling in code like this:

if 40 > 6:
    pass
else:
    pass