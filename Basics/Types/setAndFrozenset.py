# unordered values ​​in one set
# values ​​cannot be repeated

set = {0, 3, 5, 3, 23}

# add new value
set.add(20)

#remove value
set.discard(23)

for value in set:
    print(value)

# we CAN'T add and remove new value into Frozenset

frozenSet = frozenset({0, 1, 2})
frozenSet.add(5) # throw an eception