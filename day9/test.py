
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if "skills" in person:
    print(person["skills"][2])

#Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill and print out the result.

if "skills" in person :
    if "Python" in person['skills']:
        print("Yes python exists.")
    else: 
        print("Python does not exits.")

# * If a person skills has only JavaScript and React, print('He is a front end developer'),
#  if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!

if "skills" in person :
    if "Node" and "React" and "MongoDB"in person['skills']:
        print("He is a fullstack developer")
    elif "React" and "Node" and "MongoDB" in person["skills"]:
        print("He is a backend developer.")
    elif "JavaScript" and "React" in person["skills"]:
        print("He is a front end developer")

if person['is_married'] and person['country'] == "Finland":
    print("Asabeneh Yetayeh lives in Finland. He is married.")