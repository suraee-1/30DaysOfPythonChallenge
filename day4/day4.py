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

# unpacking character
language = "Python"
a,b,c,d,e,f =language # if variables > len(str) -> Value Error
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print("\n\n")
# Accessing character of a string by Index from left side
print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])
print("\n\n")

#Accssing characters of a string by Right side
print(language[-1])
print(language[-2])
print(language[-3])
print(language[-4])
print(language[-5])
print(language[-6])
#print(language[-7]) # index error
print("\n\n")

#slicing a string in python

language = "Python"
first_three_characters = language[0:3] # includes first character but excludes last cahracter
print(first_three_characters)
last_three_characters = language[3:6]
print(last_three_characters)
last_four_characters = language[-4::] # start at minus 4 go till end 
print(last_four_characters)

#reverse a string
greeting = "Hello world"
print(greeting[::-1])

#skipping characters while slicing

language ="Javascript" #Jvsrp
print(language[0:11:2])

#capitalize function

name ="harley winston"
print(name.capitalize()) # capitalizes first word of the string

# counts the  occurance of a sub string 
sentence = "I m loving coding in Python for thirty days"
print(sentence.count("o",0,4))
print(sentence.count("th",0,))

# checking if a string ends with something
print("Ending with on :",sentence.endswith("on"))
print("Ending with ys : ",sentence.endswith("ys"))

#increase tab sizes
sentence = "I m \tloving coding with python"
print(sentence)
print(sentence.expandtabs(15)) # increase tab spacing

#finding something in a  string 
print(sentence.find("python")) # returns -1 if not found
print(len(sentence))

# finding the last occurance of a word in python # rfind
print(sentence.rfind("i"))

# fomating a string

first_name ="James"
last_name ="Wilson"
age = 30
job ="entreprenuer"
print("My name is {} {}.I am {} and I work as a {}".format(first_name,last_name,age,job))

#.index method returns the lowest index of a string
items = " tv , fridge , iron , oven"
print(items.index(','))

# .rindex method returns the highes index when an item in found
print(items.rindex(","))

# checks for alpha and num
print(("IsaphaNumeric12").isalnum())
print("Is not a alpha numeric" ,"not".isalnum())
# checks for num
words = "1234"
print(words.isnumeric())
# checks for alphabets
words ="adsad"
print(words.isalpha())

#isdecimal - checks if a string contains only decimal i.e. 0 to 9
numbers ="1223 4"
print(numbers.isdecimal())

#isdigit - checks if a string is a digit
age ="_290"
print(age.isdigit())

#isIdentifier -checks if a string is a identifier
print(age.isidentifier())

#islower 
words ="apple"
print(words.islower())

#isUpper
words = "APPLE"
print(words.isupper())

