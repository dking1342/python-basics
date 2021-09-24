# collections: counter, named tuple, ordered dictionary, default dictionary, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

# counter
mystr = "aabbeeff" # can be any interable data type
mycounter = Counter(mystr)
print(mycounter) # returns dict with key/value pairs
print(mycounter.keys()) # outpus dict of keys
print(mycounter.values()) # outputs dict of values
print(mycounter.items()) # outputs dict with tuples
print(mycounter.most_common(1)) # outputs dict with tuple of most common value
print(list(mycounter.elements())) # returns as a list

# named tuples
Point = namedtuple("Point","x,y")
pt = Point(1,2)
print(pt)
print(pt.x, pt.y)

# ordered dictionary - for older python versions, new versions built in with dictionary
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
print(ordered_dict) # returns ordered dictionary in tuples

# default dictionary
default_dict = defaultdict(int)
default_dict["a"] = 1
default_dict["b"] = 2
default_dict["c"] = 3
print(default_dict) # returns default dictionary with type specified
print(default_dict["a"]) # gets single value from search paramter

# deque
d = deque()
d.append(1) # inserts value to end of deque
d.append(2) # inserts value to end of deque
d.append(3) # inserts value to end of deque
d.appendleft(5) # inserts value to the beginning of deque
d.pop() # removes last value from deque
d.extend([4,5,6]) # inserts list to end of deque
d.extendleft([7,8,9]) # inserts list to beginning of deque in reverse order
d.rotate(1) # rotates all values to the right
d.rotate(2) # rotates all values to the right by search parameter
d.rotate(-3) # rotates all values to the left by search paramter

print(d)
