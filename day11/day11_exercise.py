#Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(num1,num2):
    return num1+num2

print(add_two_numbers(4,5))

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
import math
def area_of_circle(radius):
    area = math.pi * radius**2
    return area
print(area_of_circle(10))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*numbers):
    try :
        sum =0
        for num in numbers:
           sum+=num
        return sum
    except TypeError:
        return "Invalid Input"

print(add_all_nums(1,2,3,4,5,"sf"))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(celcius):
    return (celcius*9/5) + 32
print(convert_celsius_to_fahrenheit(0))

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month= month.lower()
    summer = ["june","july","august"]
    spring =["march","april","may"]
    autumn = ["september","october","november"]
    winter = ["december","january","february"]

    if month in summer:
        return "summer"
    elif month in spring :
        return "spring"
    elif month in autumn :
        return "autumn"
    elif month in winter :
        return "winter"
    else :
        return "Invalid Input"
    
print(check_season("january"))

#Write a function called calculate_slope which return the slope of a linear equation
 

def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Slope is undefined"
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(x1=10,x2=20,y1=12,y2=20))

#Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a,b,c):
    if a == 0:
        return "Not a quadratic equation"
    discriminant = b**2 -4*a*c
    if discriminant > 0:
        x1 = (-b+math.sqrt(discriminant))/(2*a)
        x2 = (-b-math.sqrt(discriminant))/(2*a)
        return x1,x2
    elif discriminant ==0:
        x =-b/(2*a)
        return x
    else :
        return "No real roots exits."
    

print(solve_quadratic_eqn(1,-3,2))

#Declare a function named print_list. 
# It takes a list as a parameter and it prints out each element of the list.

def print_list(items):
    for item in items:
        print(item)

fruits = ["apple","banana","lemon"]
print_list(fruits)

#Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(items):
    i = len(items)
    j=0
    reverse =[]
    while i > 0:
        reverse.append(items[i-1])
        i-=1
        j+=1
    return reverse
print(reverse_list(fruits))

def reverse_list(items):
    i = len(items)
    reverse = [None] * i
    j = 0

    while i > 0:
        reverse[j] = items[i-1]
        i -= 1
        j += 1

    return reverse
print(reverse_list(fruits))
        
#Declare a function named capitalize_list_items.
#  It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(items):
    capitalized =[]
    for item in items:
        capitalized.append(item.capitalize())
    return capitalized
print(capitalize_list_items(fruits))

#Declare a function named add_item. 
# It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(item_list,item):
    item_list.append(item)
    return item_list
print(add_item(fruits,"mango"))

#Declare a function named remove_item. It takes a list and an item parameters.
#  It returns a list with the item removed from it.
def remove_item(item_list,remove_item):
    item_list.remove(remove_item)
    return item_list
print(remove_item(fruits,"apple"))

#Declare a function named sum_of_numbers.
# It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(numbers):
    sum = 0
    for number in range(numbers+1):
        sum+=number
    return sum
print(sum_of_numbers(5))
print(sum_of_numbers(100))

#Declare a function named sum_of_odds. 
# It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(numbers):
    total= 0
    for number in range(numbers+1):
        if not number%2 ==0:
            total+=number
    return total
print(sum_of_odds(10))

#Declare a function named sum_of_even. 
# It takes a number parameter and it adds all the even numbers in that - range

def sum_of_even(numbers):
    total = 0
    for number in range(numbers+1):
        if number%2 ==0:
            total+=number
    return total
print(sum_of_even(10))

# level 2
#Declare a function named evens_and_odds . 
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(number):
    even = 0
    odd = 0

    for num in range(number+1):
       if num%2 == 0:
         even+=1
       else:
           odd+=1

    return (f"The number of even numbers is {even},\nThe number if odd numbers is {odd}.")
print("\n")
print(evens_and_odds(100))

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    total = 1
    for number in range(1,num+1):
        total*=number
    return total
print(factorial(5))

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(item):
    if not item :
        return True
    return False
print(is_empty("na"))

#Write different functions which take lists. They should calculate_mean, 
# calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
from collections import Counter

def statistics(lst):
    
    if is_empty(lst):
        return "No items exits"
    values = {}
    values["mean"] =calculate_mean(lst)
    values["mod"] = calculate_mod(lst)
    values["cal_range"] = calculate_range(lst)
    values["variance"] = f"{calculate_variance(lst):3f}"
    values["std"] = f"{cal_standart_dev(lst):3f}"
    return values


def calculate_mean(lst):
    total = 0
    for i in lst:
        total+=i
    return total/len(lst)

def calculate_mod (lst):
    mod = max(lst,key=lst.count) # got this method from stack overflow
    return mod

def calculate_range(lst):
    min_value =min(lst)
    max_value = max(lst)
    return max_value -min_value

def calculate_variance(lst):
    squared_difference=calculate_squared_difference(lst)
    variance = squared_difference/len(lst)
    return variance

def calculate_squared_difference(lst):
    mean = calculate_mean(lst)
    total_squared_difference = 0
    for i in lst:
        total_squared_difference += (i-mean)**2
    return total_squared_difference

def cal_standart_dev(lst):
    variance = calculate_variance(lst)
    std = (variance) ** 0.5
    return std

def calculate_median(lst):
    sorted_list = sorted(lst)
    length_list = len(sorted_list)
    mid = length_list//2
    if length_list % 2 != 0:
       return sorted_list[mid]
    else :
        mid_minus_1 = mid-1
        return (sorted_list[mid] + sorted_list[mid_minus_1] )/2
print(statistics([]))

# Write a function called greet which takes a default argument, name. 
# If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.

def greet(name = "Guest"):
    print(f"Hello, {name}")
greet()
greet("adam")