

# GET functionality
# employee_file = open("employees.txt","r")
# print(employee_file.readable()) # checks to see if file is readable / boolean
# print(employee_file.read()) # gets the contents of the file
# print(employee_file.readline()) # reads the first line / each readline would read the next line
# print(employee_file.readlines()) # gets content and puts into an array

# loops through the lines of the file
# for emp in employee_file.readlines():
#   print(emp)

######################
# POST functionality
# employee_file = open("employees.txt","a")
# employee_file.write("Oscar - Accountant\n")

# UPDATE functionality
employee_file = open("employees.txt","w")
employee_file.write("Kelly - CSR\n")

employee_file.close()
