# reduce - redukuje sekwencj� do pojedynczej warto�ci

from functools import reduce


listData = [ 1, 2, 3, 4, 5 ]
sum = reduce((lambda x, y: x + y), listData)

print(sum)