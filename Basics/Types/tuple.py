print("Tuples are not mutable! We can't change and remove any element")

data = ('one', 'two', 'three') 
# or data = 'one', 'two', 'three'; without ()
# or data = tuple( ('one', 'two', 'three') )

print(data)
print(len(data))

print(data[1])
print(data[::2])

oneElementTuple = ('only one', ) # MUST add , after element

data[0] = 'Test' # we CAN'T overwrite tuple's element value
print(data)

del data[0] # we CAN'T remove any items