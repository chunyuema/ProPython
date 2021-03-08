l = [1, 2, 3, 4]

# Performing mathematical operations on the entire list
l2 = [x**2 for x in l]
d2 = {x: x**2 for x in l}
print(l2, d2)

# Combining multiple lists into one
a = [1, 2, 3]
b = [7, 8, 9]
print([(x+y) for (x, y) in zip(a, b)])  # [8, 10, 12]
print([(x, y) for x in a for y in b])
# [(1, 7), (1, 8), (1, 9), (2, 7), (2, 8), (2, 9), (3, 7), (3, 8), (3, 9)]

# Flatten a list
my_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
flattened = [x for temp in my_list for x in temp]
# output => [10, 20, 30, 40, 50, 60, 70, 80, 90]
