# The *args and **kwargs is a common idiom to allow arbitrary number of arguments to functions as described in the section more on defining functions in the Python documentation. *args will give all function parameters in a tuple; **args will give all function in a dictionary

def foo(*args):
    print(args)


def bar(**kargs):
    print(kargs)


foo(1, 2, 3, 4, 5)
bar(name="chunyuema", major="computer science")
