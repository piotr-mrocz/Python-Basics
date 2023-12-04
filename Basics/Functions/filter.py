# filter - przeszukuje listê

listData = [ 1, 2, 3, 4, 5 ]

result = filter(lambda x: x % 2 == 0, listData)

for item in result:
    print(item)