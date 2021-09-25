from threading import Thread, Lock, current_thread
from queue import Queue
import time

## example 1
def square_numbers():
    for i in range(100):
        i * i

if __name__ == "__main__":
    threads = []
    num_threads = 10
    
    # create threads
    for i in range(num_threads):
        thread = Thread(target=square_numbers) # args is optional using a tuple
        threads.append(thread)

    # start
    for t in threads:
        t.start()

    # join waiting for it to finish
    for t in threads:
        t.join()

    print("end thread")

## example 2
db_val = 0

def increase(lock):
    global db_val

    # locking you can use lock.acquire() and lock.release() or use with lock:
    with lock:
        # locking
        # lock.acquire()

        # sim db activity
        local_copy = db_val

        # processing
        local_copy += 1
        time.sleep(0.1)

        db_val = local_copy

        # unlocking
        # lock.release()

if __name__ == "__main__":
    lock = Lock()
    print(f"start value {db_val}")

    thread1 = Thread(target=increase,args=(lock,))
    thread2 = Thread(target=increase,args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"end value {db_val}")
    print("end main")

## using queues

def worker(q,lock):
    while True:
        with lock:
            value = q.get()
            ## processing
            print(f"in {current_thread().name} got {value}")
            q.task_done()

if __name__ == "__main__":
    
    q = Queue()
    lock = Lock()
    # q.put(1)
    # q.put(2)
    # q.put(3)

    # # gets the first value in the queue
    # first = q.get() # when you do this, you need to tell it do be done
    # print(first)
    # q.task_done() # completes task
    # q.join() # blocks the main thread until all elements are processed

    num_threads2 = 10
    for i in range(num_threads2):
        thread = Thread(target=worker,args=(q,lock))
        thread.daemon=True # makes the threads go in sequence otherwise it is jumbled
        thread.start()

    for i in range(1,21):
        q.put(i)
    # q.task_done()
    q.join()

    print("end main")