"""
    Create an empty dictionary called dog
    Add name, color, breed, legs, age to the dog dictionary
    Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
    Get the length of the student dictionary
    Get the value of skills and check the data type, it should be a list
    Modify the skills values by adding one or two skills
    Get the dictionary keys as a list
    Get the dictionary values as a list
    Change the dictionary to a list of tuples using items() method
    Delete one of the items in the dictionary
    Delete one of the dictionaries
"""

dog ={}
dog["name"] = "Shiro"
dog["color"] = "black"
dog["breed"] ="street"
dog["legs"] = 4
dog["age"] = 4

student ={"first_name":"John",
          "last_name" : "Smith",
          "gender":"male",
          "marital_status":True,
          "skills":["html","css","python","java"],
          "country" : "India",
          "city" : "Siliguri",
          "address" : "Salt Lake"
          }
print(len(student))

print(student["skills"])
print(type(student["skills"]))

student["skills"].append("git")
student["skills"].append("docker")
print(student["skills"])

keys = student.keys()
print(keys)

values = student.values()
print(type(values))# specific type 

student_list = student.items()
print(student_list)
student_tpl = tuple(student_list)
print(type(student_tpl))

student.pop("first_name")
print(student)

del student
#print(student)