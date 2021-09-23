
# while loops
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("end of loop")

# secret_word = "dog"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#   if guess_count < guess_limit:
#     guess = input("guess a word: ")
#     guess_count += 1
#   else:
#     out_of_guesses = True

# if out_of_guesses:
#   print("you lose!")
# else:
#   print("you win")

# for loops
for letter in "denver broncose":
  print(letter)

friends = ["Jim","Karen","Kevin"]
for friend in friends:
  print(friend)

for x in range(10):
  print(x)

for num in range(3,10):
  print(num)

for num in range(1,30,3):
  print(num)

for friend in range(len(friends)):
  print(friends[friend])

for index in range(10):
  if index == 0:
    print("first")
    break
  else:
    print(index)

def exponents(base_num, power_num):
  result = 1
  for index in range(power_num):
    result = result * base_num
  return result

x = exponents(2,5)
print(x)

num_grid = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [0]
]
print(num_grid[0][2])

# nested for loop
for row in num_grid:
  for col in row:
    print(col)
