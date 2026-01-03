# variables 
first_name = "john"
last_name = "snow"
country = "India"
city ="Anycity"
age = 30
is_married = False
skills = ["Python" , "docker" , "kubernates" , "Linux" , "Tensorflow"]

personal_info ={
    first_name :"john",
    last_name :"snow",
    country :"India",
    age : 24
    

}
print("\n\n")
print('Hello world') # hello world is an argument to the built in fuction print
print("hello",",","world","!" "")

# printing values stored in variables 
print("First_name : ",first_name)
print("First name length : " ,len(first_name))
print("Last Name : ",last_name)
print("Last name length : " ,len(last_name))
print("City : " ,city)
print("Country : " ,country)
print("Is Married : ",is_married)
print("Skills : ",skills)
print("Personal info :",personal_info)
print("\n\n")

# declaring multiple variables

first_name , last_name ,age, is_student = "Max" , "Muller" ,34, True
print("First Name : ",first_name)
print("Last Name : ",last_name)
print("Age : ",age)
print("Is Student : ",is_student)
print("\n\n")

# getting user_input

#name = input("What is your name ? :")
#age = input ("What is your age ? :")

#print("Your name is ",name)
#print("Your age is " ,age)

# Data Types

first_name = "Steve"
last_name = "Little"
age = 24

print ("First Name : ",type(first_name))

print("Last Name : ",type(last_name))

print("Age : ",type(age))

print("tuple" ,type((1,2,3,4)))

print("set : ",type({1,23,334,343,23}) )

print("List : ",type(["apple" ,"banana" ,"cherry"]) )

print("Dict : ",type({"Age ": 23,"can_dance" : False}))

print("Complex : ",type((7+4j)))

print("Bool" ,type(False))

# zip

print("Zip" ,type(zip([1,2],[3,4])))
print("\n\n")

# casting : converting one variable type to another
# num to float
num_int = 10
print("Num Int type : ",type(num_int))
num_float = float(num_int)
print("Num float : ",type(num_float))

# flaot to num

float_pi = 3.14
print(int(float_pi))# removes decimal points which can cause incorrect value estimation

# int to string

num_length = 240
str_length = str(num_length)
print(type(str_length))

# str to int 
# it only works if str > float > int

breath_str = "10.45"

breath_float = float(breath_str)
print(breath_float)
breath_int = int(breath_float)
print(breath_int)

# str to list 
# to convert a string to a list 

company = "Abacus"
company_list = list(company)
print(company_list)

"""
Exercises: Level 1

    Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
    Write a python comment saying 'Day 2: 30 Days of python programming'
    Declare a first name variable and assign a value to it
    Declare a last name variable and assign a value to it
    Declare a full name variable and assign a value to it
    Declare a country variable and assign a value to it
    Declare a city variable and assign a value to it
    Declare an age variable and assign a value to it
    Declare a year variable and assign a value to it
    Declare a variable is_married and assign a value to it
    Declare a variable is_true and assign a value to it
    Declare a variable is_light_on and assign a value to it
    Declare multiple variable on one line

Exercises: Level 2

    Check the data type of all your variables using type() built-in function
    Using the len() built-in function, find the length of your first name
    Compare the length of your first name and your last name
    Declare 5 as num_one and 4 as num_two
    Add num_one and num_two and assign the value to a variable total
    Subtract num_two from num_one and assign the value to a variable diff
    Multiply num_two and num_one and assign the value to a variable product
    Divide num_one by num_two and assign the value to a variable division
    Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    Calculate num_one to the power of num_two and assign the value to a variable exp
    Find floor division of num_one by num_two and assign the value to a variable floor_division
    The radius of a circle is 30 meters.
        Calculate the area of a circle and assign the value to a variable name of area_of_circle
        Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
        Take radius as user input and calculate the area.
    Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
    Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

"""