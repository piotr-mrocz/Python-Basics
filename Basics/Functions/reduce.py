# reduce - redukuje sekwencjê do pojedynczej wartoœci

from functools import reduce


listData = [ 1, 2, 3, 4, 5 ]
sum = reduce((lambda x, y: x + y), listData)

print(sum)