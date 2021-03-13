from operator import attrgetter

# 1. using sorted function
l = [1, 2, 5, 6, 2, 4, 7, 9]
print(sorted(l))  # getting a copy of sorted array
print(l)  # [1, 2, 5, 6, 2, 4, 7, 9] original copy is not affected

# 2. using .sort() function
newL = l.sort()
print(newL)  # sort function returns None
print(l)  # [1, 2, 2, 4, 5, 6, 7, 9] original copy is sorted, this returns none

l = [1, 2, 5, 6, 2, 4, 7, 9]
l.sort(reverse=True)
print(l)


# 3. using sorted function for other data strcutures
tup = (1, 2, 5, 6, 2, 4, 7, 9)
# tup.sort() #AttributeError: 'tuple' object has no attribute 'sort'
sortedTup = sorted(tup)
print(sortedTup, type(sortedTup))


dict = {'name': 'chunyue',
        'job': 'ai engineer',
        'age': '20'}
sortedDict = sorted(dict)  # sort based on the keys, return a list
print(sortedDict, type(sortedDict))  # ['age', 'job', 'name'] <class 'list'>


# 4. use the key to specify how to sort
l1 = [-6, -3, -7, 1, 2, 3]
print(sorted(l1))  # [-7, -6, -3, 1, 2, 3]
print(sorted(l1, key=abs))  # [1, 2, -3, 3, -6, -7]


# 5. use key to specify how to make comparison
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 34, 80000)
e3 = Employee('John', 25, 75000)

employees = [e1, e2, e3]
s_employees = sorted(employees, key=lambda x: x.salary)
print(s_employees)  # [(Carl,37,$70000), (John,25,$75000), (Sarah,34,$80000)]
s_employees2 = sorted(employees, key=attrgetter('age'))
print(s_employees2)
