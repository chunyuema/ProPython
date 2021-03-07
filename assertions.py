# use assertions to provide checks of your code
# assert <condition>
# assert <condition>, <error message>

def f(a, b):
    return a+b


assert f(3, 4) == 8  # AssertionError
assert f(2, 3) == 5, "did not pass"  # This one produces nothing
assert f(2, 4) == 5, "did not pass"  # AssertionError: did not pass
