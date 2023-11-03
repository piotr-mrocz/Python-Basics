# function id() returns unique identifier (memory address)

a = 1
b = 2

print(a)
print(b)
print()

print("unique identifier")
print(id(a))
print(id(b))
print()

print(a == b)
print(id(a) == id(b))


# Typu niemutowalne
# Ka�da zmiana na typach:
# float
# bool
# string
# tuple
# frozenset
# powoduje powstanie nowego obiektu, czyli tworzenie nowej warto�ci w pami�ci


# Typy mutowalne
# Ka�da zmiana na typach:
# lista
# set
# s�ownik
# powoduje zmian� w pami�ci (NIE tworzymy nowej warto�ci w pami�ci)