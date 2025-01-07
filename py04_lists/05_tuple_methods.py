# Tuple methods
#Tuple of integers
int_tuple = (1, 2, 3, 4, 5)
print(int_tuple)

#Tuple of strings
str_tuple = ("apple", "banana", "cherry")
print(str_tuple)

#Tuple of mixed datatypes
a = (1, 45, 67, 89, 34, 56, True, "Tekendra")
print(type(a))

no = a.count(45)
print(no)
print(len(a))

#Tuple of tuples
nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))
print(nested_tuple)

#Tuple of lists
list_tuple = ([1, 2, 3], ["a", "b", "c"], [True, False])
print(list_tuple)

#Tuple of dictionaries
dict_tuple = ({"name": "John", "age": 23}, {"name": "Jane", "age": 22})
print(dict_tuple)