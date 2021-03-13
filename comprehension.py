nums = [1, 2, 3, 4, 5, 6, 7, 8]

# 1. use list comprehension instead of for loop
array1 = []
for num in nums:
    array1.append(num)
print(array1)

array2 = [num for num in nums]
print(array2)


# 2. use list comprehension instead of map function
array4 = list(map(lambda num: num*num, nums))
print(array4)

array3 = [num*num for num in nums]
print(array3)


# 3. use list comprehension instead of filter
array5 = list(filter(lambda num: num % 2 == 0, nums))
print(array5)

array6 = [num for num in nums if num % 2 == 0]
print(array6)


# 4. use list comprehension to get rid of the nest for loop
array7 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(array7)


# 5. dictionary comprehension
names = ['Bruce', 'Clark', 'Peter']
heros = ['Batman', 'Superman', 'Spiderman']

dict1 = {}
for name, hero in zip(names, heros):
    dict1[name] = hero

print(dict1)

dict2 = {name: hero for name, hero in zip(names, heros)}
print(dict2)

dict3 = {name: hero for name, hero in zip(names, heros) if name != "Peter"}
print(dict3)


# 6. set comprehension
nums = [1, 1, 1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 9]
set1 = {num for num in nums}
print(set1)  # {1, 2, 3, 4, 5, 6, 7, 9}


# 7. generator expression
nums = [1, 2, 3, 4]
generator = (n*n for n in nums)
print(generator)  # <generator object <genexpr> at 0x1092d42d0>
for i in generator:
    print(i)
