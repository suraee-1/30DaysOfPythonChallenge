#higher order functions 
# either the function takes an argument as a function or returns a functions

def add(a,b):
    return a+b

print(add)
addition = add 
print(addition)
print(addition(2,3))

"""
okay that means 
def add(a,b):
 return a+b
addition = add
print(addition(2,3)
so that means variables and functions are stored in memory when the function is created 
and creates a memory address 
we can assign the memory address to some variable like addition 
such that the variable acts like the same function coz internally 
python thinks it is just pointing at the same memory address


In Python, a function name is just a variable pointing to a function object.
"""

# function as a parameter
numbers = [1,2,4,5,6,7,8,9,10]

def total(numbers): # normal function
    return sum(numbers) # a function using the built in sum

print(total(numbers))

def higher_order_function(function,lst):
    total = function(lst)
    return total

print(higher_order_function(total,numbers))


# function as a return value
def square(num):
    return num*num
def cube(num):
    return num**3
def absolute(num):
    if num >=0:
        return num
    else :
        return -num
def higher_of(type):

    if type == "square":
       return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute

sq = higher_of("square")
print(sq(2))
cb = higher_of("cube")
print(cb(2))
abs = higher_of("absolute")
print(abs(-9))

# python closure  - Python allows a nested function to access the outer scope of the enclosing function.

"""okay let me teach u 
# closure in python 
# when inner variable is dependent to outer variable in a  nested function
# python stores the outer variable - i think it stores as a normal variable which will never die
# def add_ten():
 ten = 10  # this is the outer variable 
  def add(num): it calls the inner function
   return add+num # it returns the sum if function is called
  return add # the object is passed
"""
def add_ten():
    ten =10
    def add(num):
        return ten+num
    return add

closure_result = add_ten()
print(closure_result(10))
print(closure_result(5))
