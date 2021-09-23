# import from your own files
from data import feet_in_mile, beatles, greeting

# import from python
# import random

# import from other python creators
# using pip like npm to download package modules

def inches_in_mile(feet):
  return feet * 12

print(inches_in_mile(feet_in_mile))
print(beatles)

for beatle in beatles:
  print(beatle)

print(greeting("Jack"))