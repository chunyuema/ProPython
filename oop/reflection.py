class Animal(object):
    def __init__(self, name):
        self.name = name


class Bear(Animal):
    pass


myBear = Bear("bear")
print(type(myBear))
print(isinstance(myBear, Animal))
print(isinstance(myBear, Bear))
print(issubclass(Bear, Animal))
