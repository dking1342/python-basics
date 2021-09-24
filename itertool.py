# itertools: product, permutations, combinations, accumulate, groupby, and infinte iterators
from itertools import accumulate, combinations, combinations_with_replacement, count, cycle, groupby, permutations, product, repeat
import operator

# product
iter = [1,2]
iter1 = [3,4]
prod = product(iter,iter1)
prod2 = product(iter,iter1,repeat=2) # repeats the iterable for each index
print(list(prod))

# permutations
mystr = "hey"
mylist = list("".join(mystr))
print(list(permutations(mylist))) # using for string
perm = [1,2,3]
perm_calc = permutations(perm,2) # second argument can tell how many values in each permutation
print(list(perm_calc)) # using with num

# combinations
com = [1,2,3,4]
comb = combinations(com,2) # second argument tells the length of each combination value
combr = combinations_with_replacement(com,2)
print(list(comb)) # possible combinations
print(list(combr)) # possible combinations with replacements

# accumulations
accum = [1,20,3,4]
acc = accumulate(accum)
acctimes = accumulate(accum,func=max)
print(list(acc)) # adds all values then goes through each iteration
print(list(acctimes)) # adds all values then goes through each iteration and performs function

# groupby
gby = [1,2,3,4,5]
def smaller_than_three(x):
    return x < 3
group_obj = groupby(gby,key=smaller_than_three)
# for/in loop to find values of group
for key,value in group_obj:
    print(key,list(value))

group_obj2 = groupby(gby,key=lambda x: x<4)
for key,value in group_obj2:
    print(key,list(value))

persons = [
    {"name":"tim","age":25},
    {"name":"jack","age":25},
    {"name":"jill","age":40},
    {"name":"jon","age":50}
]
persons_less_than = groupby(persons,key=lambda x: x["age"] < 41)
persons_same_value = groupby(persons,key=lambda x: x["age"])
for key,value in persons_less_than:
    print(key,list(value))
for key,value in persons_same_value:
    print(key,list(value))

# infinite iterators

# count
for i in count(10):
    print(i)
    if i == 15:
        break

# cycle
a = [1,2,3]
for i in cycle(a):
    print(i) # need to break to stop iterations

# repeat
a1 = [1,2,3]
for i in repeat(a1,3): # second argument tells the number of repeats
    print(i)
