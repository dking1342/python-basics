# asterisks: use cases, multiplication, multiple values, args, kwargs, tuples, unpacking or merging objects

# uses in repeating or math operations
result = 5 * 7 # used as a multiplication operator
result2 = 5 ** 4 # used as a power operator
mylist = [0] * 10 # creates a list with a length of ten with 10 zeroes
mylist2 = [0,1] * 10 # same but now it will repeat 0,1
mytup = (0) * 10 # creates a tuple of repeating zeroes for a length of 10
mystr = "A" * 10 # creates a string of length 10 that repeats "A"

# args and kwargs, unpacking, single asterisk for keyword and positional arguments
def foo(a,b,*args,**kwargs): # positional and keyword arguments
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])

foo(1,2,3,4,5,six=6,seven=7)

def foo2(a,b,*,c,d=4): # anything after * is a keyword argument
    print(a,b,c)
foo2(1,2,c=3)

# deconstructing kind of, unpacking
numbers = [1,2,3,4,5,6]
tupl = (1,2,3,4,5) # this will turn into a list if it is unpacked
*beginning,last = numbers # the * can be used to go at beginning, middle or last
# beginning,*middle,last = numbers
# beginning, *last = number 
print(beginning)
print(last)

mytuple = (1,2,3,4,5)
mylist3 = [6,7,8,9]
myset = { 1,2,3}
mydict = {"a":1,"b":2}
mydict2 = {"c":3,"d":4}
new_dict = {**mydict,**mydict2} # merge multiple dicts into one new dictionary
new_list = [*mytuple, *mylist3,*myset] # merge into one new list
print(new_list,new_dict)
