# Create an empty list
info =list()
print(info)

#Declare a list with more than 5 items
fruits = ["Apple","Mango","Banana","Orange","Lime"]
# find len of ur list
print(len(fruits))

#Get the first item, the middle item and the last item of the list
print(fruits[0])
print(fruits[len(fruits)//2])
print(fruits[-1])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["John Stark",34,170,True]



#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

#Print the list using print()
print(companies)

#Print the number of companies in the list
print("No of campanies : ",len(companies))

#Print the first, middle and last company
print("First : ",companies[0])
print("Middle : ",companies[len(companies)//2])
print("Last : ",companies[-1])

#Print the list after modifying one of the companies
companies[0] ="Meta"
print(companies)

#Add an IT company to it_companies
companies.append("Capgemini")
print(companies)

#Insert an IT company in the middle of the companies list
mid = len(companies)//2
companies.insert(mid,"INFOSIS")
print(companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
companies[0]=companies[0].upper()
print(companies)
#Join the it_companies with a string '#;  '
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
result = '#; '.join(it_companies)
print(result)

#Check if a certain company exists in the it_companies list.
print("Apple" in companies)

#Sort the list using sort() method
companies.sort()
print(companies)

# Reverse the list in descending order using reverse() method
companies.sort(reverse=True)
print(companies)

#Slice out the first 3 companies from the list

print(companies[0:3])

#Slice out the middle IT company or companies from the list
print(companies[4:5])

#Remove the first IT company from the list
companies.pop(0)
print(companies)
print("\n\n")
#Remove the middle IT company or companies from the list
print(companies)
companies.pop(len(companies)//2)
print(companies)
print("\n\n")
#Remove the last IT company from the list
print(companies)
companies.pop(6)
print(companies)

#Remove all IT companies from the list
companies.clear()
print(companies)

#Destroy the IT companies list
del(fruits)

#join the following list
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print(front_end + back_end)
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack = front_end +back_end
full_stack.append("SQL")
print(full_stack)
print("\n\n")

# Exercise level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
print(ages)
ages.sort()
max = ages[-1]
min = ages[0]
print(min,max)
#Add the min age and the max age again to the list
ages.append(min)
ages.append(max)
print(ages)

#Find the median age (one middle item or two middle items divided by two)
ages_length = len(ages)
print(ages_length)
ages.sort()
print(ages)
median = (ages[ages_length//2] + ages[ages_length//2])/2
print(median)

#Find the average age (sum of all items divided by their number )
total = 0
for i in ages:
    total+=i

print(total/ages_length)

#Find the range of the ages (max minus min)
ages_range = max-min
print(ages_range)

#Find the middle country(ies) in the countries list
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
print(countries[len(countries)//2])

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
no_of_countries = len(countries)
print(no_of_countries)
print(countries.index("Lesotho"))
contries_first_half = countries[0:98]
countries_second_half =countries[98:195]
print(contries_first_half)
print(countries_second_half)

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
new_countries = ["China","Russia","USA","Finland","Sweden","Norway","Denmark"]
china,russia,usa, *scandic_countries = new_countries
print(scandic_countries)
