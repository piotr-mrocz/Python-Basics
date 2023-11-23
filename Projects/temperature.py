isRaining = False
haveUmbrella = False
temperature = 14

if temperature >= 40 or temperature <= 0:
    print("Stay at home")
elif temperature > 0 and temperature < 10 and haveUmbrella and isRaining:
    print("Take an umbrella")
elif not isRaining and temperature >= 10:
    print("You can go outside without any umbrella")
else:
    print("Just stay at home")


#the best way to check if value is true: 
#    if haveUmbrella

#the best way to check if value is false:
#    if not haveUmbrella