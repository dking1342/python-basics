# threading vs multiprocessing

"""
Process: an instance of a program (e.g a python interpreter)

+ takes advantage of multiple cups and cores
+ seprate memory space -> memory is not shared between processes
+ great for cup-bound processing
+ new process is started independently from other processes
+ processes are interruptable/killable
+ one GIL for each process -> avoids GIL limitation

- heavyweight
- starting a process is slower than starting a thread
- more memory
- IPC (inter-process communication) is more complicated
"""

"""
threads: an entity within a process that can be scheduled (also known as "lightweight process")
a process can spawn multiple threads.

+ all threads within a process share the same memory
+ lightweight
+ starting a thread is faster than starting a process
+ great for I/O bound tasks

- threading is limited by GIL: only one thread at a time
- no effect for cpu bound tasks
- not interruptable/killable
- careful with race conditions
"""

"""
GIL: global interpreter lock 
- a lock that allows only one thread at a teim to execute in python

- nneded in CPython because memory management is not thread-safe

-Avoid:
- use multiprocessing
- use a different, free-threaded python implementation (Jython, IronPython)
- use python as a wrapper for third-part libraries (C/C++) -> numpy, scipy
"""

from multiprocessing import Process
from multiprocessing.spawn import freeze_support
import os
import time

processes = []
num_processes = os.cpu_count()

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

# create processes
for i in range(num_processes):
    p = Process(target=square_numbers) # args is optional using a tuple
    processes.append(p)

# start
for p in processes:
    p.start()

# join waiting for it to finish
for p in processes:
    p.join()

if __name__ == "__main__":
    freeze_support()
    print("end main")

# not working! 
# switch out process for thread to check for threading
