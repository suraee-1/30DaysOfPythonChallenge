import math
# boolean values : Either True or False
print(True)
print(False)

# arithmetic operators in python 
print("Addition ",3+2)
print("Substraction :",3-2)
print("Multilication : ",3*2)
print("Division : ",3/2)
print("Modulus : ",3%2)
print("Exponent : ",3 ** 2)

# calculating area of circle

radius = 30
area_of_circle = math.pi * radius ** 2
print("Area of circle : ",area_of_circle)

# calculating area of rectangle
print("\n\n")
length :float = 20
breath : float= 10

area_of_rectangle = length * breath
print("Area of rectangle : ",area_of_rectangle)

# caclulate the weight of an object
print("\n\n")
mass = 10
gravity :float = 9.8
weight = mass * gravity
print("Weight : ",weight,"N")

# calculate density of a liquid

print("\n\n")
mass = 12 # in kg
volume :float =0.012 # in cubic m
density = mass/volume # 1000kg/m^3

print("Density : ",density)
print("\n\n")
#comparision operators

print(3>2)
print(10>12)
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print("\n\n")
# comparision operator

print(4>2)
print(4<2)
print(2<=2)
print(3!=2)
print(3 ==4)

print(len("star") == len("bata"))
print(len("Aeiou")!=len("consonant"))
print(len("python") >len("django"))
print("\n\n")

# using the is keyword

print("1 is 1",1 is 1)
print("1 is not 2" , 1 is not 2)
print("S in String", "S" in "String") # caps sensitive
print("Coding in Coding for all : " ,"Coding" in "Coding for all")
print("\n\n")

 # logical operators 

print(3>2 and 3>1)
print(3>7 or 3<4)
print(3>1 or 3>2)
print( True and True)
print(True or False)
print (True and not False)
print(not 3>2)
print(not not 3<4)
print(not not True)
print(not not False) 
print("\n\n")

# Exercises
#Declare your age as integer variable
age = 24
#Declare your height as a float variable
height = 160.2  # cm
#Declare a variable that store a complex number
num = 3+4j
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#base = float(input("Enter the base of triangle : "))
#height = float(input("Enter the height of the traingle : "))

#area_triangle = 0.5 * base * height
#print("Area of triangle : ",area_triangle)

# Perimeter of a triangle
'''
side_a =float(input("Enter side A : "))
side_b =float(input("Enter side B : "))
side_c =float(input("Enter side C : "))
perimetre = side_a + side_b + side_c
print("The perimeter of the triangle is ",perimetre)
'''

# Area of rectangle 

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
'''
length = float(input("Enter the length of the rectangle :"))
width = float(input("Enter the width of the rectangle : "))
area = length * width
print("Area of rectangle : ",area)
'''
 
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

#radius = float(input("Enter the radius of the circle : "))
#area_of_circle = math.pi* math.pow(radius,2)
#print(area_of_circle)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2

equation = "y = 2x -2"

slope = 2 # y = mx +c
# for x intercept y =0 
x = 2/2
y = 2*0 -2 # x =0
print( "slope : ",slope,"X :",x,"Y :",y)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

point_a = {"x1" : 2,"y1" :2}
point_b = {"x2" :6, "y2" :6}
slope = (point_b["y2"] - point_a["y1"]) /  (point_b["x2"] - point_a["x1"])
print("Slope (m): ",slope)
equilidan_distance = ((point_b["x2"]-point_a["x1"])**2 +(point_b["y2"]-point_a["y1"])**2) ** 0.5
print("Equilidian distance : ", equilidan_distance)

# comparing slopess
print("y>slope :", y>slope)
print("y<slope :",y<slope)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0
x = -3
y =x ** 2+(6*x)+9
print(y)
 
 #Find the length of 'python' and 'dragon' and make a falsy comparison statement.
length_of_python = len("python")
length_of_dragon =len("dragon")
print("Length of python not equal to length of dragon : ",length_of_python != length_of_dragon)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'

print("If on is present  both in 'python' and 'dragon' : ","on" in "python" and "on" in "dragon")

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print("I hope this course is not full of jargon :" , "jargon" in "I hope this course is not full of jargon" )

#There is no 'on' in both dragon and python

print("There is no 'on' in both dragon and python : ",not "on" in "dragon" and not "on" in "python")
print("\n\n")
#Find the length of the text python and convert the value to float and convert it to string


text ="Yfjasfjaj"
length_of_text = len(text)
text_in_float = float(length_of_text)
length_of_text_to_original_type= str(text_in_float)
print("Text : ",type(text))
print("length of text" ,type(length_of_text))
print("text in float",type(text_in_float))
print("length of text to original type :",type(length_of_text_to_original_type))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

num = 10
print("No is even if num %2 == 0" ,num%2==0)

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

div = 7//3
print(div)
num = 2.7
num_int = int(num)
print("the floor division of 7 by 3 is equal to the int converted value of 2.7",div == num_int)

#Check if type of '10' is equal to type of 10

print("Type of '10' is equal to type of 10 : ",type("10") == type(10))

#Check if int('9.8') is equal to 10

print("is int('9.8') is equal to 10", 9.8 ==10)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate weekly pay of the person?

hours = int(input("Enter hours : "))
rate = float(input("Rate per hour : "))
weekly_pay = hours * rate * 7
print("Weekly pay" ,weekly_pay)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

no_of_years = int(input("Enter no of years : "))
no_of_seconds = 60*60*24*365 *no_of_years
print("You have lived for ",no_of_seconds)

# print the following pattern
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''

print('''
      1 1 1 1 1
      2 1 2 4 8
      3 1 3 9 27
      4 1 4 16 64
      5 1 5 25 125
''')