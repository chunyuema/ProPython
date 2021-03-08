# Generator: Functions that return an iterable set of items are called generators.

def sqaure(nums):
    res = []
    for num in nums:
        res.append(num*num)
    return res


# This currently returns a list
newNums = sqaure([1, 2, 3, 4])
print(newNums)


# Convert into generator
def sqaureYield(nums):
    for num in nums:
        yield (num*num)


newNums = sqaureYield([1, 2, 3, 4])
print(newNums)  # <generator object sqaureYield at 0x10cbb6f50>
# print(next(newNums))  # 1
# print(next(newNums))  # 4
# print(next(newNums))  # 9
# print(next(newNums))  # 16
# generator generates one res at a time

# use for loops in generators
# for num in newNums:
#     print(num)

# convert generator into a list
print(list(newNums))  # [1,4,9,16]

# generator is better than the list since sometimes when dealing with large amount of data, generator would give out better performance => generators do not hold the data in memeory, it holds everything off until it is asked for the next data
