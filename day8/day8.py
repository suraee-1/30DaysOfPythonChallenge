# creating an empty dictionary
empty_dict ={}
print(empty_dict)

dict1 ={"key1":"val1","key2":"Val2","key3":"Val3"}
print(dict1)

# length of dictionary 
print(len(dict1))

#Accessing dictionary items
print(dict1["key1"])
#print(dict1["key5"]) # key error

# Best way to access val 
print(dict1.get("key3"))
print(dict1.get("key5"))

#Adding items to dict
dict1 ["key4"] ="Val4"
print(dict1)
dict1 ["key5"] = [1,2,3,4]
print(dict1)
dict1["key5"].append(5)
print(dict1)

# modifing elements in a dictionary
dict1["key1"] = "value-one"
print(dict1)

#checking keys in a dict
print("key1" in dict1)
print("key6" in dict1)

# removing key and value pair 
dict1.pop("key1")
print(dict1)
dict1.popitem()# removes last item
del dict1["key3"]
print(dict1)

#converting dict to a list using items()
print(dict1.items())

#clearing a dict
dict1.clear()
print(dict1)

# del a dict
del dict1


# copy a dict
person ={"Name" : "John" , "Age" : 2434 ,"Married ":True}
print(person)
person2 = person.copy()
print(person2)

# getting dict keys as list
keys = person.keys()
print(keys)

# getting dict values as list

values = person.values()
print(values)