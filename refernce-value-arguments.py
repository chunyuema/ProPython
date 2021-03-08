# The arguments are passed in through reference
def append4(arr):
    arr.append(4)


arr = [1, 2, 3]
append4(arr)
print(arr)


# The arguments are passed in through value
def increment4(num):
    num += 4


num = 1
increment4(num)
print(num)
