contacts = {
    1: 'First',
    2: 'Second',
    3: 'Third'
}

print(contacts[1])
print()

print('Show keys:')
print(contacts.keys())
print()

print('Show values:')
print(contacts.values())
print()

for key, value in contacts.items():
    print(key, " ", value)