"""Exercises: Level 1

    Get user input using input(“Enter your age: ”). If user is 18 or older,
     give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
     Output:Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive."""

age = int(input("Enter your age : "))
if age >=18 :
    print("You are old enough to drive")
elif (18 - age)==1:
    print("Wait for 1 more year.")
else :
    print(f"Wait for {18-age} more years . ")

"""Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
 You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me."""

user_age = int(input("Enter your age : "))
admin_age =24
if user_age > admin_age :
   if user_age - admin_age ==1 :
        print("You are 1 yr oder than me")
   else :
        print(f"You are {user_age-admin_age} years older than me.")
else :
    if admin_age - user_age ==1 :
       print("I am 1 year older than you.") 
    else:
       print(f"I am {admin_age - user_age} years older than you.")

'''Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:'''

num1 =int(input("Enter a number : "))
num2 = int(input("Emter other number : "))

if num1 > num2 :
    print(f"{num1} is greater than {num2}")
else :
    print(f"{num1} is smaller than {num2}")

# level 2
'''
    Write a code which gives grade to students according to theirs scores:

```sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
```
'''
marks = int(input("Enter your marks : "))

if (marks>=90 and marks<=100):
    print("A")
elif (marks>=80 and marks<=89):
    print("B")
elif (marks>=70 and marks <=79):
    print("C")
elif (marks >=60 and marks<=69):
    print("D")
else :
    print("F")

"""Get the month from user input then check if the season is Autumn,
 Winter, Spring or Summer. If the user input is: September,
   October or November, the season is Autumn. December, January or February, 
   the season is Winter. March, April or May, the season is Spring June, July or August,
     the season is Summer"""
month = input("Enter a month :").lower()
autumn = ["september","october","november"]
winter = ["december","january","february"]
spring = ["march","april","may"]
summer = ["june","july","august"]

if month in autumn :
    print("Autumn")
elif month in winter :
    print("Winter")
elif month in spring :
    print("Spring")
elif month in summer :
    print("Summer")
else :
    print("Invalid Input!")

"""    The following list contains some fruits:

```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
"""
fruits = ["banana","orange","mango","lemon"]
fruit = input("Enter a fruit : ").lower()
if fruit in fruits :
    print("The fruit already exists.")
else :
    fruits.append(fruit)
    print(fruits)

# level 3
"""
    Here we have a person dictionary. Feel free to modify it!
"""
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if "skills" in person:
    print(person["skills"][2])

#Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill and print out the result.
if "skills" in person :
    if "Python" in person['skills']:
        print("Yes python exists.")
    else: 
        print("Python does not exits.")

# * If a person skills has only JavaScript and React, print('He is a front end developer'),
#  if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!
if "skills" in person :
    if "Node" and "React" and "MongoDB"in person['skills']:
        print("He is a fullstack developer")
    elif "React" and "Node" and "MongoDB" in person["skills"]:
        print("He is a backend developer.")
    elif "JavaScript" and "React" in person["skills"]:
        print("He is a front end developer")

# If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetif person['is_married'] and person['country'] == "Finland":
if person['is_married'] and person['country'] == "Finland":
    print("Asabeneh Yetayeh lives in Finland. He is married.")
