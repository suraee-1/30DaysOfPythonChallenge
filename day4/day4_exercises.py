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
