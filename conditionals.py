
# working with conditionals
is_male = True
is_tall = True

if is_male or is_tall:
  print("You are a male or you are tall")
else:
  print("You are not a male or you are not tall")

if is_male and is_tall:
  print("You are tall and male")
else:
  print("You are not male and tall")

if is_male:
  print("you are a male")
elif is_male and not(is_tall):
  print("you are male and not tall")
else:
  print("you are not a male")

def max_num(num1,num2,num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3

print(max_num(5,4,30))

def match_str(str1, str2, str3):
  if str1 == "dog":
    return str1
  elif str2 != "cat":
    return str2
  else:
    return str3

print(match_str("cow","cat","frog"))
