number = 10

def printNumber():
    number = 20
    print(number)
  
printNumber()
print(number)

def printNumber2():
    global number
    number = 30
    print(number)

printNumber2()    
print(number)