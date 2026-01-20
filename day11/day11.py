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

#If we pass the arguments with key and value, the order of the arguments does not matter.

def print_name(first_name,last_name):
    space =" "
    print(f"{first_name}{space}{last_name}")

print_name(first_name="Ay",last_name="Xin")

def add_two_num(first_num,second_num):
    return first_num+second_num
print(add_two_num(first_num=1,second_num=78))

# function with a return value part 2
# if a function does not return a value it returns none by default


def demo():
    ...
x = demo()
print(x)# prints the default value i.e. none

def print_name(first_name):
    return first_name

print(print_name("John"))

# returning a list

def check_even(number):
    even=[]
    for num in range(number+1): 
        if num%2 == 0:
            even.append(num)
    return even

print(check_even(10))

# function with default parametres

def greet(name="Peter"):
    print(f"Welcome, {name} to the 30 days coding challenge.")

greet()

# arbitrary number of arguments
# if we do not know the total number of arguments that are passed we use the arbitrary number of args
# by using greet(*name) 

def sum_all_nums(*nums):
    sum=0
    for num in nums:
        sum+=num
    return sum

print(sum_all_nums(1,23,43,43))

def generate_groups(teams,*args):
    print(teams, end=" ")
    for i in args:
        print(i ,end=" ")
    print("")

generate_groups("Team 1 ","John","Peter")

# Dictionary unpacking

def greetings(name,location):
    print(f"Hello {name} ,how is the weather in {location} ?")

greetings("John","Sili")

my_dict = {"name":"Peter","location":"Fiji"}
greetings(**my_dict)

# passing functions as parameter
def add(num1,num2):
    return num1 + num2
def print_sum(sum):
    print(sum)
print_sum(add(3,5))