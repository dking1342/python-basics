# generators: generates iterable objects

def mygenerator():
    yield 1
    yield 2
    yield 3

gen = mygenerator()

# loops through the function
# for i in gen:
#     print(i)

# iterates over the function one by one
# value = next(gen)
# print(value)
# value = next(gen)
# print(value)
# value = next(gen)
# print(value)

# can be used with other methods that needs to be iterated one by one
# print(sum(gen))

def countdown(num):
    print("starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(10)
value = next(cd)
print(value)
print(next(cd))

## example
def first_n(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(first_n(10))
print(sum(first_n(10)))

# using a generator. same thing but now with a generator and being more efficient, less memory
def first_n_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(list(first_n_generator(5)))
print(sum(first_n_generator(10)))

## example 2
def fibs(limit):
    # 0 1 1 2 3 5 8 13 ...
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b,b + a

f = fibs(100)
for i in f:
    print(i)

mylist = [i for i in range(10) if i % 2 == 0] # using a list to iterate
mygen = (i for i in range(10) if i % 2 == 0) # short hand generator to iterate
mylist2 = list(mygen) # converts it to a list
for i in mygen:
    print(i)