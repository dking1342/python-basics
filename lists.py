
# lists are ordered, mutable, allows duplicates
my_list = ["banana","cherry","apple"]
print(my_list)

# duplicates allowed
my_list2 = [5,True,"apple",5]
print(my_list2)

item = my_list[0]
print(item)

last_item = my_list[-1]
print(last_item)

# loop through a list
for index in my_list:
    print(index)

# check if value is in the list
if "banana" in my_list:
    print("yes")
else:
    print("no")

# methods for lists

# length of the list
length = len(my_list)
print(length)

# adds value to end of list
my_list.append("lemon")
print(my_list)

# adds value to specific index
my_list.insert(1,"blueberry")
print(my_list)

# removes a value from the end of the list
item = my_list.pop()
print(item)
print(my_list)

# removes value from the list but will show error if value is not in the list
cherry = my_list.remove("cherry")
print(cherry)

# removes all values from the list
my_list.clear()
print(my_list)

# updates the list in reverse order
my_list2.reverse()
print(my_list2)

# updates the list and sorts in ascending order
my_list3 = [1,3,4,2,6,3]
my_list3.sort()
my_list4 = sorted(my_list3)
print(my_list3,my_list4)

# creates a new list and populates the list with value and length 
my_list5 = [0] * 5
print(my_list5)

# creating new list by combining other lists into one list
my_list6 = [1,2,3,4,5]
my_list7 = [5,6,7,8]
my_list8 = my_list6 + my_list7
print(my_list8)

# updates list using slice to go from one index to the other index
my_list9 = [1,2,3,4,5,6,7,8,9]
my_list10 = my_list9[1:5] # goes from index 1 to index 5 and gets inbetween
my_list11 = my_list9[1:] # goes from first index used to the end of the list
my_list12 = my_list9[:5] # goes from the beginning of the list to the specified index
my_list13 = my_list9[::2] # provides the step amount to slice/skip to and outputs the values
my_list14 = my_list9[::-1] # another way to reverse a list
print(my_list14)

# creating copies of lists
lyst = ["banana","cherry","blueberry"]
last = [1,2,3,4,5]
# doing it this way will make a copy but any update in first list will be seen by copied list 
lyst_copy = lyst # copies but will show any changes to original list
lyst_copy2 = lyst.copy() # copies and will not show changes to original list
lyst_copy3 = list(lyst) # copies using the list constructor
lyst_copy4 = lyst[:] # copies using the slice method
lyst_copy5 = [i * i for i in last] # uses a for/in loop to iterate the list and perform action
print(lyst_copy5)
