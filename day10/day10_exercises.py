#Iterate 0 to 10 using for loop, do the same using while loop.

for number in range(0,11):
    print(number)
print("\n\n")
number =0
while number<11:
    print(number)
    number+=1

print("\n\n")
#Iterate 10 to 0 using for loop, do the same using while loop.

for number in range(10,-1,-1):
    print(number)

print("\n")
number =10
while(number>=0):
    print(number)
    number-=1
print("end")

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:

for i in range(1,8,1):
    print("*"*i)

#Use nested loops to create the following: 8x8 grid with #


for _ in range(1,9):
    for _ in range(1,9):
        print("#", end =" ")
    print("")

# Print the following pattern:
"""0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100"""

for j in range(0,11):
        print(f"{j} X {j} = {j*j}")

#terate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

tech = ["Python","Numpy","Django","Flask"]
for items in tech:
     print(items+" ",end="")

print("")

#Use for loop to iterate from 0 to 100 and print only even numbers

for num in range(0,101):
     if num == 0:
          continue
     elif num % 2 ==0 :
          print(num)

for num in range(2,101,2):
     print(num)
print("\n\n")

#Use for loop to iterate from 0 to 100 and print only odd numbers

for num in range(0,101):
     if num % 2 ==0 :
          continue
     else :
          print(num)

#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for num in range(0,101):
     sum+=num
print(sum)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even =0
sum_odd = 0

for i in range(0,101):
     if i %2 ==0:
          sum_even+=i
     else:
          sum_odd +=i
    
print(f"The sum of odd number in range 0 to 100 is {sum_odd} and sum of all even numbers in range 0 to 100 is {sum_even}")

# level 3

#Go to the data folder and use the countries.py file.
#  Loop through the countries and extract all the countries containing the word land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
for country in countries :
     if country.endswith("land"):
          print(country)

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ["banana","orange","mango","lemon"]
i = len(fruits) -1

while True:
     print(fruits[i])
     i-=1
     if i==-1:
          break
     
fruits = ["banana","orange","mango","lemon"]
i = len(fruits) -1
reversed_fruits=list()
while True:
     reversed_fruits.append(fruits[i])
     i-=1
     if i==-1:
          break
print(reversed_fruits)


'''Go to the data folder and use the countries_data.py file.

    What are the total number of languages in the data
    Find the ten most spoken languages from the data
    Find the 10 most populated countries in the world
'''

from data.countries_data import countries_list

lang = list()

for country in countries_list:
     lang.extend(country["languages"])
     
unique_lang =set(lang)
print(unique_lang)
print(f"Total no of languages in the data is : {len(unique_lang)}")

# the ten most spoken languages
from collections import Counter
count = Counter(lang)
print(count)

top_10 = count.most_common(10)