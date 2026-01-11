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

# deleting items using del keyword
print(fruits)
del(fruits[0])
print(fruits)
del(fruits)
print("\n\n")

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
print(fruits)
del(fruits[0])
print(fruits)
del(fruits[1])
print(fruits)
del(fruits[1:3])
print(fruits)
del(fruits)
#print(fruits)

# clear method empties the list
fruits =["apples" ,"banana"]
print(fruits)
fruits.clear()
print(fruits)
print("\n\n")
#coping a list
fruits = ["Apple","Banana" ,"Lime","Orange"]
print(fruits)
fruits_copy =fruits.copy()
print(fruits_copy)
print("\n\n\n")
# joining a list  with + => creates a new list
zero = [0]
positive_numbers = [1,2,3,4,5,6,7,8,9,10]
negative_numbers =[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
integers = negative_numbers + zero +positive_numbers
print(integers)
# using extend
negative_numbers.extend(zero)
print(negative_numbers)
negative_numbers.extend(positive_numbers)
print(negative_numbers)
# count
fruits = ['banana', 'orange', 'mango', 'lemon',"banana"]
print(fruits.count("banana"))
# finding index of an item
print(fruits.index("orange"))
print(fruits.index("banana")) # prints first occurance only
print("\n\n")
#reverse a list
print(fruits)
fruits.reverse()
print(fruits)
# sorting a list 
fruits.sort()
print(fruits)
#numbers.sort
numbers = [121323210,12,2734,2323]
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse= True)
print(numbers)