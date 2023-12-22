import time 
import multiprocessing

def task(start, end, queue):
    result = 0
    for i in range(start, end): 
        result += 1
    queue.put(result)

def multi_process_test():     
    queue = multiprocessing.Queue()
    start = time.time()
    p1 = multiprocessing.Process(target=task, args=(0, 50000000, queue))
    p1.start()
    p2 = multiprocessing.Process(target=task, args=(50000000, 100000000, queue))
    p2.start()
    v1 = queue.get(block=True)
    v2 = queue.get(block=True)
    print(v1 + v2)
    end = time.time()
    print("Overall time for multiprocessing: ", end-start)


    