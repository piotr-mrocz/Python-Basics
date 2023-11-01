weight = 86.6
height = 1.6

bmi = weight / (height * height)

print("BMI: ", bmi)

if (bmi <= 18.5) :
    print("Underweight")
elif (bmi >= 24.9) :
    print("Overwight")
else:
    print("OK")