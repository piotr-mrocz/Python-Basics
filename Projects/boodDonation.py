age = int(input("Age: "))
weight = float(input("Weight: "))

if age >= 18:
    if weight >= 50:
        print("You can donate blood")
    else:
        print("You need to gain weight")
else:
    print("You are not adult")