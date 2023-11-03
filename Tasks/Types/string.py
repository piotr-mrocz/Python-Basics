name = input("Write Your name: ")
lastName = input("Write Your lastname: ")
city = input("Write Your city: ")

print("\n-----------------\n")

city = city[::(len(city) - 1)]
print(f"{name} {lastName} lives in {city} ({city})")