# tuple are immutable 
empty_tuple =()
print(empty_tuple)

# creating with the tuple constructor
new_tuple = tuple()
print(new_tuple)

# tuple with intial values
fruits =("Apple","Banana","Lemon","Orange")

# printing the length of tuple

print(len(fruits))
print(fruits[0])# first item
print(fruits[1])# second item
# negative indexing starts from -1
print(fruits[-1])# last item

#slicing a tuple

print(fruits[0:])# all elements
print(fruits[1:3])# item 1 and item 2 at index
print(fruits[-1:-2])# empty

# converting touple to list
list_fruits = list(fruits)
print(list_fruits)

# checking an item in touple

print(f'"Apples" in {fruits} : {"Apple" in fruits}' )

# joining touple 
touple_1 = ("item1","item2")
touple_2 = ("item3","item4")
touple3 = touple_1 +touple_2
print(touple3)

# deleting a touple
del touple_1  # del is not a function
print(touple_1)