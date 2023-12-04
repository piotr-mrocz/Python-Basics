names = [ 'Ola', 'Ania', 'Kasia' ]

print("map")
names = list(map(lambda x: f'{x} Kowalska', names))

for name in names:
    print(name)
    
print()
print("filter")

names = list(filter(lambda x: len(x) > 12, names))

for name in names:
    print(name)