# MONOTONIC STATIC
def nextGreaterElement(nums):
    stack = []
    res = [-1]*len(nums)
    for i in range(len(nums)-1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])
    return res


nums = [2, 1, 2, 4, 3]
res = nextGreaterElement(nums)
# print(res)


def decodeString(s):
    stack = []
    curr_num = ""
    curr_str = ""
    for i in s:
        if i == "[":
            stack.append(curr_str)
            stack.append(int(curr_num))
            curr_num = curr_str = ""
        elif i == "]":
            num = stack.pop()
            prev_str = stack.pop()
            curr_str = prev_str + curr_str*num

        elif i.isdigit():
            curr_num += i
        else:
            curr_str += i
    return curr_str


def removeNums(num, k):
    stack = []
    for d in num:
        while stack and k and stack[-1] > d:
            k -= 1
            stack.pop()
        stack.append(d)
    if k:
        stack = stack[:-k]
    return "".join(stack).lstrip("0")


num = '265417'
print(removeNums(num, 3))
