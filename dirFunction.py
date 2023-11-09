# in Python is special funcion: dir
# this function show every function depends on type

print("STRING")
someString = "something and somehow"
print(dir(someString))

# and now we know we can use some function. For example title
print(someString.title())
print()

print("OBJECT")
someObject = [ 0, 1, 2 ]
print(dir(someObject))

# and now we can use function clear or something else
print(someObject)

# clear
someObject.clear()
print(someObject)