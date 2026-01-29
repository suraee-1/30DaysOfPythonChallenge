# list compresions is a compact way of creating a list from a sequence 
# [expression for i in iterable if condition]

odd_num =[i for i in range(0,21) if i%2!=0]
print(odd_num)

#language = "python"
language = "Python"
lst =list(language)
print(type(lst))
print(lst)

# second way
lst_language = [_ for _ in language]
print(lst_language)

# genrating numbers

numbers = [_ for _ in range(0,11)]
print(numbers)

# possible to do mathematical equations during iteration
squares = [i*i for i in range(0,11)]
print(squares)

# it is possible for list of tuples
numbers_tpl =[(i,i*i) for i in range(0,31)]
print(numbers_tpl)

# list comprehensions with an if statement
# generating even numbers 
even_number =[i for i in range(0,11) if i%2==0]
print(even_number)

# generating odd numbers
odd_number = [i for i in range(0,11) if i%2!=0]
print(odd_number)

# filtering out positive numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_numbers =[i for i in numbers if i >0]
print(positive_numbers)

# filtering out positive and even number from the list
positive_even_numbers = [i for i in numbers if i>0 and i % 2 ==0]
print(positive_even_numbers)

# flatening a two dimensional array 

list_of_list =[[1,2,3],
               [4,5,6],
               [7,8,9]]
flatened_list = [numbers for row in list_of_list for numbers in row]
print(flatened_list)
print("\n\n\n")
# lambda functions
# it is a type of functions without a name 
# it can take make arguments but only one expression

# named funcitons
def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(2,4))

#changing the above function to a lambda function

add_two_number = lambda a,b :a+b
print(add_two_number(2,3))

# self invoking lambda function

print((lambda a,b :a+b)(5,6))

# square 
square = lambda a : a*a 
print(square(4))

# cube
cube = lambda a :a**3
print(cube(5))

#multiple varibale
multiple_variable = lambda a,b,c : b**2 - 4*a*c
print(multiple_variable(1,2,3))

# lamda function inside another function
def power(x):
    return lambda n : n**x
print(power(2)(3))
print(power(5)(2))