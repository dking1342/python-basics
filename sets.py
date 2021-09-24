# sets: unordered, mutable, no duplicates
# just single values, not key/value pairs
myset = { 1,2,3 } # cannot have duplicates
myset1 = set([1,2,3]) # create set using the set constructor
myset2 = set("hello") # shows only unique values. nice trick to show the number of unique values
myset3 = set() # creates an empty set

myset.add(4) # updates the set with the add method
myset.discard(3) # removes the value of the search parameter, no error if not found
myset2.clear() # removes the entire set
myset1.pop() # removes the first value in the set

# looping through sets 
# for/in loop
for index in myset:
    print(index)

# conditional search to get value in search parameter
if 3 in myset:
    print("yes")
else:
    print("no")

# unions, intersection, difference - do not modify, will create a new set
odds = {1,3,5,7,9}
evens = {2,4,6,8,0}
primes = {2,3,5,7}

union = odds.union(evens) # merged the two sets
intersection = odds.intersection(primes) # shows the values in separate sets that intersect
diff = evens.difference(primes) # shows the values that do not intersect in separate sets
diff2 = evens.symmetric_difference(primes) # returns all values except duplicates from sets
evens.update(primes) # updates the set that are found in the other set, same will not show
evens.intersection_update(primes) # updates the values found in both set
evens.difference_update(primes) # updates the values that are not found in both set
evens.symmetric_difference_update(primes) # another way to do it, removes dups

# supersets and subsets
odds2 = {1,3,5,7,9}
evens2 = {2,4,6,8,0}
primes2 = {2,3,5,7}
odds2.issubset(evens2) # boolean value that tells if one set is the subset of another set
odds2.issuperset(evens2) # boolean value if one set has all values of the other
odds.isdisjoint(evens2) # boolean is there are no intersecting values and is null

# copying sets 
myset_org = { 1,2,3,4 }
myset_copy = myset_org # will copy but it will modify if original changes
myset_copy2 = myset_org.copy() # will copy and will be unique of the original

# frozen set - makes the set immutable
myset_frozen = frozenset([1,2,3,4]) # cannot change after creating it


