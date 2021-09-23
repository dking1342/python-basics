
# working with functions
# function with no parameter
def greeting():
  print("Hello User")

greeting()

# function with a parameter
def greeting2(username):
  print("Hello " + username)

greeting2("Jim")

def cube(num):
  return pow(num, 3)

result = cube(4)
print(cube(3))
print(result)