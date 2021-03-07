# Tuple is immutable
l1 = [1, 2, 3, 4]
t1 = (1, 2, 3, 4)
l1[0] = 2
# t1[0] = 2  # TypeError: 'tuple' object does not support item assignment

# Tuples cannot be copied but list can be copied
names = ("name1", "name2")
copyNames = tuple(names)
print(copyNames)
print(copyNames is names)  # True

names = ["name1", "name2"]
copyNames = list(names)
print(copyNames is names)  # False

# Tuple has a smaller size and hence faster than list
tuple_names = ('Nicholas', 'Michelle', 'Alex')
list_names = ['Nicholas', 'Michelle', 'Alex']
print(tuple_names.__sizeof__())
print(list_names.__sizeof__())

# Tulles are used for a couple of elements that can be of different types whereas lists are usually used to store the same type of data => only semantic
