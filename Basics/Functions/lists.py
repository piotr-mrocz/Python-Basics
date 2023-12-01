def AddTolistData(listData): # listData is not changed outside this function
    print(f"Before: {listData}")
    listData = [ 1, 2, 3 ]
    print(f"After: {listData}")


listData = [10]

print("Without changes")
AddTolistData(listData)
print(f"Original: {listData}")
print()


def AddTolistDataAndChange(listData):
    print(f"Before: {listData}")
    listData = [ 1, 2, 3 ]
    print(f"After: {listData}")
    return listData

print("With changes")
listData = AddTolistDataAndChange(listData)
print(f"Original: {listData}")

print()

def AppendItem(listData):
    listData.append(50)

print("Append item to the listData")
AppendItem(listData)
print(f"Original: {listData}")