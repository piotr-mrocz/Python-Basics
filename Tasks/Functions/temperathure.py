def CelsiusToFahrenheit(degrees):
    return degrees * 9 / 5 + 32

def FahrenheitToCelsius(degrees):
    return (degrees - 32) * 5 / 9

print(f"20\xB0 Celsius: {CelsiusToFahrenheit(20)}\xB0 Fahrenheit")
print(f"86\xB0 Fahrenheit: {FahrenheitToCelsius(86)}\xB0 Celsius")