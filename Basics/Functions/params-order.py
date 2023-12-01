# / must be in order

def printData(string, number = 10, /):
	print(string, number)

printData('Text', 5)
# printData(number = 5, string = 'Text') # error - bad order

print()

# * named params

def printNamedData(*, string, number = 10):
	print(string, number)

printNamedData(string = 'Text', number = 5)
# printNamedData('Text', 5) # error - not named params

print()

def printMixedData(float, bool, *, string, number = 10):
	print(float, bool, string, number)

printMixedData(12.5, bool = False, string = 'Text', number = 5)
printMixedData(12.5, False, string = 'Text', number = 5)
# printMixedData(12.5, False, 'Text') # error - not named params (string and number (if use) must be named)