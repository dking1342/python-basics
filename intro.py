from math import * # import a module

# first program
print("Hello World")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# data types and variables
# data types
# string
# int
# boolean
# functions

# variables
character_name = "John" # string
character_age = "70" # string
character_year = 1990
is_male = True
is_female = False

# print function
print("There was a man named " + character_name)
print("He was " + character_age + " years old")

# change the variable
character_name = "Mike" # string
print("He liked his name " + character_name)
print("He didn't like the age " + character_age)

# working with strings
print("david king")
print("hello\nworld") # \n used to make a new line
print("Denver \"Broncos\"") # \ used similar to regex
phrase = "Denver Broncos"
print(phrase + " are the best")

# built in functions
# python has a list of built in functions
print(phrase.lower()) # function used to lower case the string
print(phrase.isupper()) # function used to check if it is upper case
print(phrase.upper().isupper()) # you can chain the functions
print(len(phrase)) # length of the string
print(phrase[2]) # returns the string of the index value
print(phrase.index("r")) # returns the index value of the first value
print(phrase.replace("e","o")) # returns the replaced values similar to regex replace

# working with numbers
print(4)
print(3 + 4.5)
print(2.30927)
print(3 * 4 + 5)
print(10 % 3)
my_num = 5
my_num_2 = -5
print(my_num)
print(str(my_num))
print(abs(my_num_2))
print(pow(my_num,5)) # exponents
print(max(5,10))
print(min(3,6))
print(round(3.2349740))
print(floor(2.34))
print(ceil(2.463))
print(sqrt(25))

