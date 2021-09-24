# exceptions: errors and exceptions

# syntax errors
# a = 5 print(a) #syntax error
# print(a)) # syntax error

# type errors
# a = 5 + "10" # type error

# module errors
# import errosnso # module does not exist

# name error
# a = 5
# b = c # c is not defined

# file error
# f = open("somefile.txt") # no file exists

# value error
# a = [1,2,3]
# a.remove(1) # fine
# a.remove(4) # value error becuase it does not exists

# index error
# a = [1,2,3]
# a[4] # index 4 does not exists
# a = {"name":"Max"}
# a["age"] # age key does not exist

# exception
# x = -5
# x = 5
# if x < 0:
#     raise Exception("x should be positive")

# assert statement
# x = -5
# assert(x >= 0), "x is not positive"

# handle exceptions
# from typing import final


try:
    a = 5 / 0
except:
   print("error happened")

try:
    a = 5 / 0
except Exception as e:
   print(e)

try:
    a = 5 / 0
    b = a + "10"
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("everything is fine")
finally:
    print("finally code for clean up code")
    
# custom error exceptions
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("value too small", x)
    else:
        print(f"x is {x}")

try:
    test_value(101)
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)

