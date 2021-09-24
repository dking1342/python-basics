# dictionary: key-value pairs, unordered, mutable 

mydict = {"name":"david","age":30, "city":"boston"}
mydict2 = dict(name="Jack",age=22,city="new york") # using the dictionary constructor

value = mydict["name"] # bracket notation to find value from a key search parameter
mydict["name"] = "jack" # updates value of key/value pair
# mydict["email":"jack@example.com"] # updated the dictionary with new key/value pair ???

# del mydict["email"] # deletes a key/value pair using the key search parameter
mydict.pop("name") # deletes a key/value pair using the key search parameter
mydict.popitem() # deletes the last inserted key/value pair

# gets values of dictionary using conditional loop
if "name" in mydict2:
    print(mydict2["name"])

# gets the values of the dictionary using try/except 
try:
    print(mydict2["name"])
except:
    print("error")

# looping through dictionary 
# for/in loop to find key/value pairs together
for key in mydict2:
    print(key)

# for/in loop to find keys
for key in mydict2.keys():
    print(key)

# for/in loop to find values
for value in mydict2.values():
    print(value)

# for/in loop to separate out the key and value and display each separately
for key, value in mydict2.items():
    print(key, value)

# copying dictionary 
# copy but changes if original changes 
mydict_copy = mydict2

# copy of original and can be changed without changes to other dictionary
mydict_copy2 = mydict2.copy()

# copy of original using the dict constructor
mydict_copy3 = dict(mydict2)

# creates a new dictionary from a value (string, list, etc) and second paramter sets the value
mylist = ["jim","jack","jill"]
mylist2 = ["green","blue","red"]
print(mydict2.fromkeys(mylist,"blue"))

# method to merge dictionaries and updates the dictionary the is being updated into the other
mydict4 = {"name":"jill","age":30,"city":"appleton"}
mydict5 = {"name":"jon","age":40,"city":"green bay", "email":"jon@example.com"}
mydict4.update(mydict5)
print(mydict5)

# key types can be any 
# key can be a number or tuple
mydict6 = {3:9,6:36,9:81}
value = mydict6[3] # will get the key that has the same value as the search parameter
mytup = (8,7)
mydict7 = { mytup: 15 } # inserting tuple is possible as the key
mylist3 = [8,7]
# mydict8 = { mylist3: 15 } # this is not possible to have a list as the key


