# fruits = {'apple','orange'}
# fruits.add('grapes')
# print(fruits)

# animal = frozenset(['tiger','lion'])
# animal.add('cat')
# print(animal)


# num = {1,2,3,1,2,3,3,4,5,6}
# print(num)


# emptyset = {}
# print(type(emptyset))

# emptyset = set()
# print(type(emptyset))


# num = {1,2,3,4}
# num1 = set(num)
# print(num1)


# Set Operations
# Membership      Add
# Remove          union
# clear

# intersection    difference
# sym.difference  size
# copy

set1  = {1,2,3,4,'hello'}
print(4 in set1)

set1.add(6)
print(set1)

set1.remove(4)
print(set1)

set2 = {1,'apple'}
print(set1|set2)

set1.clear()
print(set1)