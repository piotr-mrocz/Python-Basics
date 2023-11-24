# False value
# this values after convert to boolean always return false

print("False value")
print(bool())
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool( () ))
print(bool( [] ))
print(bool( {} ))
print(bool(''))
print(bool(None))

print()

# True values 
# this values after convert to boolean always return true

print("True value")
print(bool(True))
print(bool(1)) # some number diffrent than 0
print(bool(-1))
print(bool( ('1') ))
print(bool( ['1'] ))
print(bool( {0, 1} ))
print(bool('1'))