 # Exercise level 1
#Create an empty tuple
empty_touple =()
print(empty_touple)

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers =("Robb","James","John")
sisters = ("Angel","Darcy","Smith")

#Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

#How many siblings do you have?
print(f"No of siblings : {len(siblings)}")

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father_mother =("Jamson","Grace")
family_members =father_mother+siblings
print(family_members)

# Exercise level 2

#Unpack siblings and parents from family_members
father,mother ,*siblings =family_members
print(f"Father : {father}, Mother : {mother}, Siblings : {siblings}")

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Apple","Banana","Lemon","Lime","Orange")
vegetables =("Tomatoes","Potato")
animal_product =("Ghee","Cheese")
food_stuff_tp = fruits +vegetables +animal_product
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_list = list(food_stuff_tp)
print(food_stuff_list)

#Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_list[0:3])
print(food_stuff_list[-1:-4:-1])
print(food_stuff_list[-3:])

#Delete the food_stuff_tp tuple completely
del food_stuff_tp
#print(food_stuff_tp)

'''    Check if an item exists in tuple:

    Check if 'Estonia' is a nordic country

    Check if 'Iceland' is a nordic country

    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')'''

nordic_countries =("Denmark","Finland","Iceland","Norway","Sweden")
print(nordic_countries)
print(f"Is 'Estonia' a nordic country : {'Estonia' in nordic_countries}")
print(f"Is 'Iceland' a nordic country : {'Iceland' in nordic_countries}")
