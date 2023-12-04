# map - przyjmuje funkcjê, ktor¹ wywo³a na wszystkich elementach parametru

listData = [1,2,3,4]

result = map(lambda x: x * 2, listData)

for item in result:
    print(item)