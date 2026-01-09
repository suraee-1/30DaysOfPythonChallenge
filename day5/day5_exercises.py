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