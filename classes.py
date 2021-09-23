
# working with classes
class Student:
  def __init__(self,name,major,gpa,is_on_probation):
    self.name = str(name)
    self.major = str(major)
    self.gpa = float(gpa)
    self.is_on_probation = bool(is_on_probation)
  
  def present(self):
    return "incoming student is " + self.name + " and studying " + self.major

student1 = Student("Jack","Music",3.90,False)
student2 = Student("Jill","Science",1.20,True)

print(student1.name)
print(student2.name)

# inheritance with classes
class Person(Student):
  def __init__(self, name, major, gpa, is_on_probation, gender):
      super().__init__(name, major, gpa, is_on_probation)
      self.gender = str(gender)
  
  def greeting(self):
    return "hello " + self.name

  def is_honor_roll(self):
    if self.gpa >= 3.5:
      return True
    else:
      return False
  
  def check_major(self):
    if self.major == "Music" or self.major == "Painting":
      return "Arts"
    else:
      return "Other type of major"

person1 = Person("Joe","Math",2.3,False,"Male")
print(person1.gender)
print(person1.greeting()) 
print(person1.present()) 
