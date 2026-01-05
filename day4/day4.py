# Strings - any text is of sting data type including symbols
letter = "p" # string can be a letter of a character
print(len(letter)) # prints  the length of letter

sentences ="Strings can be used with single or double quotes"
print(sentences)

# multiline strings can(''' ''') be made (""" """) with triple single or double quotes

multiline_comment ="""
    This 
    is 
    a 
    multiple 
    line 
    comment.
"""
print(multiline_comment)

# string concatenation - combining two or more string into a new string
first_name = "John"
last_name = "Snoww" 
space =" "
full_name = first_name + space + last_name
print(full_name)
print("Length of first name :",len(first_name))
print("length of last name :",len(last_name))
print("If last name > first name : ",last_name>first_name)
print("Length of full name : ",len(full_name))

# Escape sequence in string
# \n - new line 
# \t - new tab () 4 spaces
# // back slash
# \': single quote
# \": Double quote


print("I m enjoying this python challenges . \nAren't I ?")
print("\n\n")
print("Days \tTopic \tExercises")
print("Day1\t5\t5")
print("Day2\t6\t20")
print("Day3\t5\t23")
print("Day4\t1\t35")
print("This is \\ symbol to type \\")

# old way of formatting like c %s for strings %d for int %f for float %.number of digits for precision and %a for ascii
print("I am %s %s ."%(first_name,last_name))

radius =3.1415
age =25
print("The radius of the circle is %.3f and the age variable is %a age"%(radius,age))

#new style of formatting using .format

print("The radius of the circle is {}, and age of a person is {}".format(radius,age))

# Exercises 

#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

a ="Thirty"
b ="Days"
c ="Of"
d ="Python"
space=" "
sentence = a+space+b+space+c+space+d
print(sentence)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_coding= "Coding"
string_for ="For"
string_all ="All"

sentence3 = string_coding+ space +string_for + space + string_all
print(sentence3)

#Declare a variable named company and assign it to an initial value "Coding For All".
print("\n\n")
company = "Coding For All! enjoy"
#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print("\n\n")
length_of_string_company = len(company)
print(length_of_string_company)

#Change all the characters to uppercase letters using upper() method.

print(company.upper())

#change all the characters to lowercase letter using lower() method.

print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())
 
#Cut(slice) out the first word of Coding For All string.
