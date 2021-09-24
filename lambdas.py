# lambda- anonymous function argument: expression
from functools import reduce

# lambda function
add10 = lambda x: x + 10
print(add10(10))

# long version of the same function
def add10Func(x):
    return x + 10

# can have multiple parameters
mult = lambda x,y: x * y
print(mult(2,3))

# can be used in callback functions
# sorted
points2d = [(1,2),(30,40),(15,6)]
points_sort = sorted(points2d) # sorts based on first value
ports_sort_lam = sorted(points2d,key=lambda x: x[1]) # lambda helps function sorted, can be lambda or regular function
points_sort_sum = sorted(points2d,key=lambda x: x[0] + x[1])
print(points_sort)
print(ports_sort_lam)
print(points_sort_sum)

# map
mylist = [1,2,3,4,5]
mylist2 = map(lambda x: x * 2,mylist) # callback first then list argument
print(list(mylist2))
c = [ x * 2 for x in mylist] # short syntax to do similar map functionality
print(c)

# filter
mylist3 = [1,2,3,4,5,6]
fil = filter(lambda x: x % 2 == 0,mylist3)
print(list(fil))
fi = [ x for x in mylist3 if x % 3 == 0]
print(fi)

# reduce
red = [1,2,3,4,5]
redu = reduce(lambda acc,val: acc + val, red)
print(redu)
