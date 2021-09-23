
# working with try except for error handling

try:
  number = int(input("enter a number: "))
  print(number)
except:
  print("input is invalid")

try:
  value = 10/0
  print(value)
except ZeroDivisionError as err:
  print("Error: " + str(err))
except ValueError:
  print("general error")
