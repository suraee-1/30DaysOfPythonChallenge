"""Lists

There are four collection data types in Python :

    List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
    Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
    Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
    Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items."""

#creating list with a build in function
lst =list()
print(lst)

# using square brackets []
fruits =['banana', 'orange', 'mango', 'lemon']
print(fruits)

# printing length of list
print(len(fruits))# index starts from 0 
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
#print(fruits[4]) # index out of range

# lists can have different data type
student_info= [{"first_name" :"John","ast_name ":"Snow"},250,True]
print(student_info)

# finding last index of a list
last = len(student_info) -1
print(last)

# negative indexing accessing elements from the end
print(fruits[1])
print(fruits[-3])

#Unpacking a list means assigning the elements of a list to individual variables in a single step.
numbers = [10,20,30,54,343]
a , b , c ,*rest = numbers
print(a)
print(rest) # it will convert to a new list

#Slicing a list [Start: end] # start is inclusive end is exlucive
fruits =['banana', 'orange', 'mango', 'lemon']
print(fruits[0:4])# full list
print(fruits[1:4])
print(fruits[0:])# to end
print(fruits[:1])# from beginning

# slicing with negative indexing
print(fruits[-4:]) # full list
print(fruits[:-4]) # empty list = from beginning [0] to end [-4] or [0]

# to reverse
print(fruits[::-1])

# changing values of a list
fruits[0] = "avacardo"
print(fruits)

# checking if item present in list
does_exits = "lime"
print(does_exits in fruits)
does_exits = "lemon"
print(does_exits in fruits)

# add more items in list
fruits.append("Apples") # adds to the end
print(fruits)

# add items in a list at a specified index
fruits.insert(0,"Apple")
print(fruits)

#remove an item from a list
fruits.remove("Apple")
print(fruits)

# remove a item
lst = ["item1","item2"]
lst.remove("item1")
print(lst)

# remove items using pop
print(fruits)
fruits.pop() # if no index is specified last item is removed
print(fruits)
fruits.pop(0)
print(fruits)