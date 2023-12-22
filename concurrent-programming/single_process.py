import time

def single_process_test():
    start = time.time()
    # this is done through one thread working
    result = 0
    for i in range(100000000):
        result += 1
    print(result)

    end = time.time()
    print("Overall time = ",  end - start)