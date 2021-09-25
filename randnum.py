# random numbers
import random
import secrets

# some random methods
myrand = random.random() # selects any random number
myrand1 = random.uniform(1,10) # randomly select from range
myrand2 = random.randint(1,10) # start or end can be chosen
myrand3 = random.randrange(1,10) # end cannot be chosen
myrand4 = random.normalvariate(0,1) # picks a random number of mean and standard deviation from statistics

# random with lists
mylist = list("abcdigieoig")
myrand5 = random.choice(mylist) # picks one random value from the list
myrand6 = random.sample(mylist,3) # second argument tells how many unique random values to retrieve
myrand7 = random.choices(mylist,k=3) # second argument tells how many random values. can be duplicate values returned
random.shuffle(mylist) # shuffles the list

# creating a random list using seed method. not recommended for security reasons. use secret package
random.seed(1)
print(random.random())
print(random.randint(1,10))

# working with secrets
mysec = secrets.randbelow(10) # produce random int from 0 to upper bound
mysec1 = secrets.randbits(4) # produces random with certain number of bits
mylist2 = list("ajoiageohi")
mysec2 = secrets.choice(mylist2) # chooses random from list

#### numpy is another package that can produce random stuff

