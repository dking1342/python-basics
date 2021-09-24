# strings: ordered, immutable, text representation
mystr = "hello" # can be made with single or double quotes surrounding the value
mystr2 = 'hello' # be careful when using single and double quote, use escape or alternate the quotes
mystr3 = """hello hello """ # this is string on multiple lines
mystr4 = "hello \
world" # escape to go to new line but no spaces in the next line

# get string value/s 
mystr5 = "hello"
char = mystr5[1] # gets the value from the index of the search paramter
char2 = mystr5[-1] # gets values starting from the end of the string
# mystr5[0] = "z" # cannot update string this way because strings are immutable
slice = mystr5[1:5] # gets slice of string from first and end index
slice2 = mystr5[1:] # gets slice of string from first index to end of string
slice3 = mystr5[:4] # gets slice of string from beginning of string to the end index
slice4 = mystr5[::2] # gets slice of string in step amounts denoted by search paramter
slice5 = mystr5[::-1] # gets slice from end of string in steps, ::-1 is way to reverse the string

# concat string 
mystr6 = "tommy boy"
mystr7 = "bucs"
mynum = 1
myfloat = 1.5
# different ways to concatanate strings together
sentence = mystr6 + " " + mystr7
sentence2 = mystr6, mystr7
sentence3 = f"{mystr6} {mystr7}" # f-string new
sentence9 = f"{mynum} {myfloat}" # f-string new
sentence4 = "football team is %s" % mystr7 # %s is for string
sentence5 = "football team is %d" % mynum # %s is for integer
sentence6 = "football team is %.2f" % myfloat # %s is for float
sentence7 = "football team is {}".format(mystr7) # newer way 
sentence8 = "fooball team is {:.2f}".format(myfloat)
sentence8 = "fooball team is {:.2f}".format(mynum,myfloat)

# looping through strings
for index in mystr:
    print(index)

# conditional looping
if "e" in mystr:
    print("yes")
else:
    print("no")

# methods for strings 
mystr8 = "  hello  "
mystr8 = mystr8.strip() # removes whitespace, assign to original since string is immutable
mystr9 = "hello"
mystr9.upper() # converts string to uppercase
mystr9.lower() # convers to lowercase
mystr9.startswith("he") # boolean checks if string starts with search parameter
mystr9.endswith("he") # boolean checks if string ends with search parameter
mystr9.find("o") # gets the first index that matches search parameter
mystr9.count("o") # finds the count of search paramter
mystr9.replace("o","g") # replaces string with new value

# converting string to other data types 
mystr10 = "how are you doing"
mylist = mystr10.split() # creates a list of values split by space or search parameter
mylist2 = ["hello","world"]
mystr11 = " ".join(mylist2) # converts list to string by value in quotes
mylist3 = ["a"] * 6 # creates a list of value with length of value
mystr12 = " ".join(mylist3) # converts list to string using join
index = 0
mylist4 = [index] * 10
print(mylist4)

# formatting string 

