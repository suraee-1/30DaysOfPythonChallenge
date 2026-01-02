# Day 1 of python challenge 
print(2+3) #addition
print(2-3) # substraction
print(4*3) # multiplication
print(4/3) # division
print(3%2) # modulus (prints remainder) prints in a float 
print(10//2) # floor (prints quotient) 10/2 = 5 rem = 0 quo = 5 prints in int if two operants are int else float

# printing types 

print(type(10))
print(type(3.14))
print(type("name"))
print(type(["hi","hello","hey"])) # list
print(type(("hi","hello"))) # Tuple :cannot be changed after it is created
print(type({"name" :"john","age" :25 }))# key and value pair
print(type(True))
print(type(7+5j))
# what u see below is a multi line comment
"""Exercise: Level 1

    Check the python version you are using
    Open the python interactive shell and do the following operations. The operands are 3 and 4.
        addition(+)
        subtraction(-)
        multiplication(*)
        modulus(%)
        division(/)
        exponential(**)
        floor division operator(//)
    Write strings on the python interactive shell. The strings are the following:
        Your name
        Your family name
        Your country
        I am enjoying 30 days of python
    Check the data types of the following data:
        10
        9.8
        3.14
        4 - 4j
        ['Asabeneh', 'Python', 'Finland']
        Your name
        Your family name
        Your country

Exercise: Level 2

    Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

Exercise: Level 3

    Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
    Find an Euclidian distance between (2, 3) and (10, 8)
"""
print("\n\n") # \n is for new line
# exercise 1 

print(3+4) 
print(3-4)
print(3*4)
print(3%4) # prints 3 coz quotient
print(3/4)
print(3 ** 4)
print(3//4)

print("\n\n")
# exercise 3 printing types of inputs
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(["Asabenesh" ,"Python","Finland"]))
print(type("Your name")) # privavy reasons didn't mention
print(type("Your fmaily name"))
print(type("Your country"))


# exercise 3
age = 24 # integer
is_student =True # bool
pi = 3.1415 # float
imaginary = 3 +5j
name ="john snow"
list =["apple" ,"mango" ,"grapes"]
document_no = (("123456789","JUFSNS2342"))
stuent_roll_no = {23,43,34,12} # unique
student_info ={
    "first_name" :"John",
    "last_name" : "snow",
    "age" : 24,
    "skills" : ["Swordfighting" , "running" ,"killing_white_walkers"]

}
print(student_info)
print("/n/n")

# Finding euclidian distance between (2,3) and (10,8)
# what is it?
# let P be a point whose co-ordinate is(2,3) and Q be the other co-ordinate(10,8)
# distance (P,Q) can be given by d(p,q)= root ( p1 - q1 whole sq + p2 - q2 whole sq)
import math
p1 =2
p2 =3
q1 =10
q2 =8
p1_minus_q1 = p1-q1
p2_minus_q2 = p2 -q2
sq_of_p1_q1 = math.pow(p1_minus_q1,2)
sq_of_p2_q2= math.pow(p2_minus_q2,2)

euclidian_Distance = math.sqrt(sq_of_p1_q1+sq_of_p2_q2)
print(euclidian_Distance)

# better way of doing
x1 ,y1 = 2 ,3
x2 ,y2 = 10 ,8

distance = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
print(distance)