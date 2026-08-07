# imutable objects cannot be modified after creation
# int
# float
# strings
# tuples
# frozenset

a = 5 
a = 6 

first_location = id(a)
second_location = id(a)

print(first_location)
print(second_location)