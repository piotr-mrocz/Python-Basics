#is and is not - this operators compare memories

data1 = [ 1, 2, 3 ]
data2 = [ 1, 2, 3 ]

print("is")
print(data1 is data2)
print(data1 is data1)

print()

print("is not")
print(data1 is not data2)
print(data1 is not data1)