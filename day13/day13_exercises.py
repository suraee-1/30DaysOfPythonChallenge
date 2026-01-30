# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numbers_with_negative= [i for i in numbers if i <=0]
print(numbers_with_negative)

#Flatten the following list of lists of lists to a one dimensional list :
"""output
[1, 2, 3, 4, 5, 6, 7, 8, 9]"""
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

one_d_list = [numbers for row in list_of_lists for numbers in row]

print(one_d_list)

# Using list comprehension create the following list of tuples:

'''
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
'''

tpls = [(i,1,i,i**2,i**3,i**3 *i,i**3*i*i )for i in range(0,11)]
print(tpls)
print("\n")

new_tpls = [(i,1,i,i**2,i**3,i**4,i**5) for i in range(0,11)]
print(new_tpls)

"""countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]"""

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = []
for item in countries:
   country , capital = item[0]

   result.append([
      country.upper(),
      country[:3].upper(),
      capital.upper()
   ])

print(result)
new_list =[]
for [[country,capital]] in countries:
   new_list.append([
      country.upper(),
      country[:3].upper(),
      capital.upper()
   ])
print(new_list)

# list comprehension
countries_with_capital = [[country.upper(),country[:3].upper(),capital.upper()] for [[country,capital]] in countries]

# input data = [[(1, 2)], [(3, 4)], [(5, 6)]]
# output = [[1, 2, 3], [3, 4, 7], [5, 6, 11]]

numbers = [[(1,2)],[(3,4)],[(5,6)]]
numbers_list=[]

for item in numbers:
    a,b=item[0]
    numbers_list.append([
       a,
       b,
       a+b
    ])
print(numbers_list)

new_num_list=[]
for [[x,y]] in numbers:
   new_num_list.append([
      x,y,x+y
   ])
print(new_num_list)

# cities = [[('Paris','France')], [('Rome','Italy')], [('Berlin','Germany')]]
# output :[['PARIS','FR','FRANCE'],
 #['ROME','IT','ITALY'],
 #['BERLIN','GE','GERMANY']]

cities = [[("Paris","France")],[("Rome","Italy")],[("Berlin","Germany")]]
cities_cap=[]
for [[cap,coun]] in cities:
    cities_cap.append([
       cap.upper(),
       coun[:2].upper(),
       coun.upper(),
       
       
    ])
print(cities_cap)



"""Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
"""
# list comprehension
comprehension_dict = [{"country": country.upper(),"city" : city.upper()} for [[country,city]] in countries]

# 
countries = [[('Finland','Helsinki')],
             [("Sweden", 'Stockholm')],
             [('Norway','Oslo')]]


def country_capital(lst):
   result = []
   
   for [[country,city]] in lst:
      country_dict={}
      country_dict["country"] = country.upper()
      country_dict["city"] = city.upper()
      result.append(country_dict)
    
   return result
print(country_capital(countries))

"""
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

"""
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

def firstname_and_last_names(lst):
   result = []
   for items in lst:
      full_name = " ".join(items[0])
      result.append(full_name)
   return result
print(firstname_and_last_names(names))


# lets come back to list comprehensions
fullname = [" ".join([firstname,lastname]) for [[firstname,lastname]] in names ]
print(fullname)
print(countries_with_capital)

# Write a lambda function which can solve a slope or y-intercept of linear functions.

y_intercept = lambda x,y,m : y-m*x
print(y_intercept(2,13,3))

print(comprehension_dict)