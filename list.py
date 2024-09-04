#  A list is an ordered collection of items(element) which can be of different types. 
#  List are mutable, meaning they can be cahnged after their creation.

#create a list/array

# l = [1,2,3,4,5,6,7]
# a =  ['a','b','c']
m = [1,2,3, 'a','b','c']

# accessing elements
print(m[0])

#slicing 
print(m[1:4])

# Methods
# append: if we want to add something at the end of the list
m.append(4)
print(m)

m.remove('a')
print(m)
