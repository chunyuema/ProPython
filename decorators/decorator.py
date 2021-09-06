import time
import math


def track_time(func):

    def func1(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time take in: ", func.__name__, end-begin)

    return func1


@track_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))


factorial(10)
