# Function can take another function as an argument
# Function can also be defined within another function
# Function can be returned from another function
# Python decorators use the concept of closure

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")


ordinary()
pretty = make_pretty(ordinary)
pretty()
