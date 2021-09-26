"""
- the difference between arguments and paramters
- positional and keyword arguments
- default arguments - variable-length arguments (*args and **kwargs)
- container unpacking into function arguments
- local vs global arguments
- paramter passing (by value or by reference?)
"""

def print_name(name): # name is the parameter
    print(name)

print_name("jack") # jack is the argument

def foo(a,b,c,d=10): # a, b, c are paramters and d has a default value. default value must be at the end
    print(a,b,c)

# keyword vs positional arguments
foo(a=1,b=2,c=3) # default values for arguments. keyword arguments. does not need to be in order
foo(1,b=2,c=3) # same as above except some are keyword arguments. cannot put keyword argument after positional argument
foo(1,2,3,4) # can have d paramter showing or not. 

# variable length
def foo2(a,b,*args,**kwargs): # *args can have any number of positional arguments, **kwargs can have any number of keyword arguments
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])

foo2(1,2,3,4,5,six=6, seven=7) # a,b parameters with multiple args and kwargs, args or kwargs can be negated also

# enforced keyword arguments
def foo3(a,b,*,c,d): # before * are positional and after * are keyword arguments
    print(a,b,c,d)

foo3(1,2,c=3,d=4)

def foo4(*args, c,d): # args can be first but only keyword arguments afterwards
    for arg in args:
        print(arg)
    print(c,d)

foo4(3,4,5,c=1,d=2)

# unpack arguments
def foo5(a,b,c):
    print(a,b,c)

mylist = [0,1,2]
mytup = (3,4,5)
mydict = {"a":123,"b":234,"c":456}

foo5(*mylist) # length of list or tuple must match number of parameters
foo5(*mytup) # length of list or tuple must match number of parameters
foo5(**mydict) # length must match and keys of dictionary must match parameter values

# local vs global variables
def foo6():
    global number # if global is not declared then there will be an error due to scope of local vs global
    number = 3 # now this will work because it has been declared as a global variable
    x = number # local variable within the function
    # number = 5 # this will cause an error because now number is a local variable that is different than global variable
    print(f"number inside function {x}")

number = 1 # global variable
foo6()

# parameter value passing
# mutable types can be changed inside function
# immutable types cannot be changed. immutable objects within a mutable object can be changed
def foo7(x):
    x = 5 # now this is being reassigned, but it will not change. x will be a local variable

var = 10 # var is int and cannot be changed
foo7(var)
print(var)

def foo8(mylist):
    # mylist = [200,300,400] # reassigned but it will cause it to be a local variable so no change to global variable
    # mylist = mylist + [200,300,400] # this will not change the global variable as it is being newly created and now is a local variable
    mylist += [200,300,400] # can make the change as this is appending to the parameter
    mylist.append(4) # reassigned and it will change. mylist will revert to the global variable
    mylist[0] = -100 # reassigned and it will change. the global variable will be changed

mylis = [1,2,3] # lists are mutable so mylist will be changed with this append
foo8(mylis)
print(mylis)

