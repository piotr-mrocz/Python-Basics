list = ['text', 12, 'text2', 99.7]

print(list)

# select element/elsments
print(list[0])

print(len(list))
print(list[-1])

print(list[0:2])

print(list[2:])
print(list[::2])

# update element
list[2] = 'Some test'
print(list)

# remove element
del list[2]
print(list)

# check if data exists in list
print(12 in list)
print(123 in list)

# for
for element in list:
    print(element)

# more lists
list = [['one', 'two', 'three'], ['banan', 'aple']]
print(list)

print(list[0][1]) # first table second value
print(list[1][0]) # second table first element

# concat lists
list1 = [1, 2, 3]
list2 = [9, 8, 7]

list = list1 + list2
print(list)

print(list * 2)

# add to list
list.append(5)