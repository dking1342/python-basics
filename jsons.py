# json - javascript object notation
import json

person = {
    "name":"jon",
    "age":30,
    "city":"boston",
    "hasChildren":False,
    "titles":[
        "engineer",
        "programmer",
        "developer"
    ]
}

# dumps with an s is denoting the string
personJSON = json.dumps(person,indent=4,sort_keys=True) # a number of arguments to modify the format of the data
# print(personJSON)

# serialize python to json file
# dump without an s is working with the json file
# with open("person.json","w") as file:
#     json.dump(person,file,indent=4)

# deserialize json to python
# converts from json string to python
# loads with an s denotes working with a string
# person = json.loads(personJSON) 
# print(person)

# load without an s works with the json file
# open json file and covert to python
with open("person.json","r") as file:
    person = json.load(file)
    print(person)

# using a class to customize the json
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

user = User("jack",22)

# custom encoding function
def encode_user(obj):
    if isinstance(obj,User):
        return {"name":obj.name,"age":obj.age,obj.__class__.__name__:True}
    else:
        raise TypeError("Object of type User is not JSON serialized")
    
userJSON = json.dumps(user,default=encode_user)
print(userJSON)

# encode
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj,User):
            return {"name":obj.name,"age":obj.age,obj.__class__.__name__:True}
        return JSONEncoder.default(self,obj)

# userJSON2 = json.dumps(user,cls=UserEncoder)
userJSON2 = UserEncoder().encode(user)
print(userJSON2)

# decode
def decode_user2(dict):
    if User.__name__ in dict:
        return User(name=dict["name"],age=dict["age"])
    return dict

user2 = json.loads(userJSON2)
print(user2)

user3 = json.loads(userJSON2,object_hook=decode_user2)
print(user3)
