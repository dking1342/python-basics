import sys
# tuple: ordered, immutable, allows duplicates

my_tup = ("Max", 28, "Boston") # can be made using parentheses
my_tup1 = "Joe", 12, "Chicago" # can be made like this
my_tup2 = ("Max",) # can be made this way but needs a comma otherwise string data type
my_tup3 = tuple(["max",22,"Georgia"]) # can be made with the tuple constructor

item = my_tup[0] # gets a value based on the index unless index does not exist
item1 = my_tup[-1] # gets the value from starting from the end

# my_tup[0] = "Tim" # cannot do this because tuples are immutable

# using a for/in loop with a tuple 
for index in my_tup:
    print(index)

# using a conditional to loop through a tuple for matching
if "Max" in my_tup:
    print("yes")
else:
    print("no")

# get length or count or index
my_tup4 = ('a','b','c','d')
length = len(my_tup4) # counts the length of the tuple
count_tup = my_tup4.count("a") # counts the number of values matching the search parameter
index_tup = my_tup4.index("a") # gets the index matching the search parameter

# convert tuples to a list 
my_list = list(my_tup4) # creates a list from a tuple
my_tup_again = tuple(my_list) # creates a tuple from a list

# slice methods for tuples
a = (1,2,3,4,5,6,7,8,9)
slice_tup = a[2:5] # slices from index start to end with end not included
slice_beg = a[:3] # slices from beginning to specified index values
slice_end = a[2:] # slices from index value to the end of the tuple
slice_step = a[::2] # slices using specified step value
slice_rev = a[::-1] # slices the tuple and gives reverse

# deconstructing a tuple 
my_tup5 = ("Max",28,"Boston")
name, age, city = my_tup5 # a form of deconstruction for a tuple number of elements must match tuple length
my_tup6 = (0,1,2,3,4)
i1, *i2, i3 = my_tup5 # deconstructs tuple and converts to list but * is wildcard to go from one index to another

# compare a tuple to a list 
my_list2 = [0,1,2,"hello",True]
my_tup6 = (0,1,2,"hello",True)
print(sys.getsizeof(my_list2),"bytes")
print(sys.getsizeof(my_tup6),"bytes")
# tuples take up less space than lists
# tuples are better to iterate than lists measured in time
# working with tuples can be more efficient than lists
