# content managers: tool for resource management

# opening an external file then writing to it * recommended
with open("filename.txt","w") as file:
    file.write("some text")

# opening an external file then writing to it * not recommended
file = open("notes.txt","w")
try:
    file.write("some text")
finally:
    file.close()

from threading import Lock
lock = Lock()

lock.acquire()
# do something that is thread safe
# need to release before continuing on
lock.release()

# recommended way of working with lock as it acquires and releases automatically
# with lock:
#     # do something here

class ManagedFile:
    def __init__(self,filename):
        print("init")
        self.filename = filename

    def __enter__(self):
        print("enter")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self,exc_type,exc_value,exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"exception has been handled")
        # print(f"exc: {exc_type} {exc_value}")
        print("exit")
        return True

with ManagedFile("notes.txt") as file:
    print("do some stuff")
    file.write("some text")
    file.something()

print("continuing")

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename,"w")
    try:
        yield f
    finally:
        f.close()

with open_managed_file("notes.txt") as f:
    f.write("some text")
