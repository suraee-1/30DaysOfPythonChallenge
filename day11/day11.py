# fuctions
def generate_full_name():
    first_name = "John"
    last_name ="Snowman"
    space = " "
    fullname = first_name + space +last_name
    print(fullname)

generate_full_name()# calling the fuction

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one +num_two
    print(total)

add_two_numbers()

# functions returning a value part 1

# functions return a value using the return statement

def generate_full_name():
   first_name="John"
   last_name ="Sparrow"
   space =" "
   full_name = first_name +space+last_name
   return full_name

print(generate_full_name())

def add_two_numbers():
    num_one = 3
    num_two =5
    sum = num_one +num_two
    return sum
print(add_two_numbers())

# function with parametres  -- inputing in functions 

def greetings(name):
    message = name + ", welcome to Python for Everyone!"
    return message
print(greetings("Jav"))

def add_ten(num):
    ten = 10
    return num +10

print(add_ten(10))

def square_number(num):
    return num **2

print(square_number(12))

import math
def area_of_circle(radius):
    return math.pi *radius **2

print(area_of_circle(10))

def sum_of_numbers(num):
    sum =0
    for num in range(1,num+1):
        sum+=num
    return sum
print(sum_of_numbers(100))


# Two parametre functions 

def generate_full_name(first_name,last_name):
    space = " "
    full_name = first_name + space +last_name
    return full_name

print(generate_full_name("Xav","In"))

def two_sum(num_one,num_two):
    return num_one +num_two

print(two_sum(3,5))

def calculate_age (current_year,birth_year):
    return current_year - birth_year
print(calculate_age(2026,1995))

def weight_of_object(mass,gravity):
    return str(mass*gravity) + "N"

print(weight_of_object(100,10))

# passing arguments with key and value


