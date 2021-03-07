import copy

l = [1, 2, 3]
new_l = l
# 4568492864 4568492864 both reference to one object in the memory
print(id(new_l), id(l))
new_l[0] = "changed"
print(l)  # ['changed', 2, 3] the original list is modified

# COPY will make a copy of the object
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
new_list[1] = ["what", "is", "this"]
print("Old list:", old_list)
# Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print("New list:", new_list)
# New list: [[1, 1, 1], ['what', 'is', 'this'], [3, 3, 3]]

# COPY still reference each element of the object, change it to deepcopy to avoid issues below
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
old_list[1][1] = 'AA'
print("Old list:", old_list)
# Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
print("New list:", new_list)
# New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]


# DEEPCOPY will create a new object that is completely independent from the original one
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)
old_list[1][1] = 'AA'
print("Old list:", old_list)
# Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
print("New list:", new_list)
# New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]


d1 = {"a": 1}
d2 = copy.copy(d1)
print(d2)
d2["a"] = 2
print(d1)
d2.update({"b": 2})
print(d1, d2)
d1.