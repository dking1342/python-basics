# copying: shallow vs deep
import copy
# - shallow copy: one level deep, only references of nested child objects
# - deep copy: full independent copy

## examples of not copying but rather having a variable reference another variable
# mutable example
org = 5 # declare org variable
cpy = org # cpy will be a new variable with the same reference as org. not a copy
cpy = 6 # this will create a new variable because int is mutable. not the same for immutable
print(cpy,org)

# immutable example
mylist = [1,2,3]
cpy2 = mylist # does not make copy
cpy2[0] = -10 # updates both the original and the other global variable
print(cpy2)
print(mylist) # now the original has a value of -10 at the 0 index

# nested example
nested_list = [[1,2,3],[4,5,6]]
cpy3 = copy.copy(nested_list) # uses copy package and method but it cannot reach nested values
cpy3[0][1] = -10 # updated both original and copy as copy is a reference to the original
print(nested_list) # same values
print(cpy3) # same values

## examples of actual copying both deep and shallow
# shallow copy
shallow_original = [1,2,3,4]
copy_shallow = copy.copy(shallow_original) # using the copy package and the copy method
copy_shallow2 = shallow_original.copy() # another way to copy a list
copy_shallow3 = list(shallow_original) # using the list constructor to make a copy
copy_shallow4 = shallow_original[:] # using the slice method
copy_shallow[0] = -100 # this will not update the copy_shallow variable as it is different than shallow_original
print(shallow_original) # different than copy
print(copy_shallow) # different than original

# deep copy
deep_original = [[1,2,3,4],[5,6,7,8,9]]
copy_deep = copy.deepcopy(deep_original) # deepcopy method is used for nested original values
copy_deep[0] = -100
print(deep_original)
print(copy_deep)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Company:
    def __init__(self,boss,employee):
        self.boss = boss
        self.employee = employee

p4 = Person("jill",33)
p5 = Person("joe",44)

company = Company(p4,p5)
company_clone = copy.copy(company) # makes a shallow copy but will not work with nested values
company_clone.boss.age = 66 # updated both variables due to it being nested
print(company_clone.boss.age) # same value as it is a nested value
print(company.boss.age) # same value as it is a nested value

company_clone_nested = copy.deepcopy(company) # makes a deep copy that will work
company_clone_nested.boss.age = 88 # assigns to copy variable
print(company_clone_nested.boss.age) # different value than original
print(company.boss.age) # different value than copy

p1 = Person("jack",22)
p2 = p1 # not an actual copy
p2.age = 12
print(p1.age,p2.age) # values will be the same because the reference is updated and renders for both

p3 = copy.copy(p1) # copy package and method copies original into new variable. shallow copy
p3.age = 11
print(p1.age,p3.age) # different values as they are separate variables

