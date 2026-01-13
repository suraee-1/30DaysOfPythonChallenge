#Sets

#creating an empty set
st ={}
print(st)
# creating a set with items
fruits={"apple","banana","mango","lemon"}
print(fruits)
# getting the length of a set
print(len(fruits))

# checking an item in set
print(f"Lime in set : {"lime" in fruits}")

print(f"Lemon in set : {"lemon" in fruits}")# case sensitive

# adding an item in set
fruits.add("oranges")
print(fruits)

# adding multiple elements
vegetables = ("carrot","onion","cucumber")
fruits.update(vegetables)
print(fruits)

# del values in set
fruits.remove("onion")
print(fruits)

# pop method removes a random element 
fruits.pop()
print(fruits)

# clear the set
fruits.clear()
print(fruits)

# del a set
del fruits
# print(fruits) # name error

#converting a list to a set
fruits = ["Apple","Avacardos","Blue"]
fruits_set = set(fruits)
print(fruits,"\n",fruits_set)

# joining a set
odd_num ={1,3,5,7}
even_num ={0,2,4,6,8}
whole_num = odd_num.union(even_num)
print(whole_num)

# intesection in a set
print(odd_num.intersection(even_num))

#supset and superset
st1 ={"item1","item2","item3","item4"}
st2 = {"item3","item4"}
print(st1.issuperset(st2))
print(st2.issubset(st1))
print(st1.issubset(st2))

#difference of two sets
print(st1.difference(st2))
print(st2.difference(st1))

# symmetric difference 
print(st1.symmetric_difference(st2))
print(st1.isdisjoint(st2))