#loops 

# while loops

count =0 

while count<5:
    print(count)
    count+=1
else :
    print(count)

# break and continue
count =0
while count <5:
    print(count)
    count+=1
    if count == 3:
        break
print("\n\n")
count =0

while count <5:
    if count ==3 :
        count+=1
        continue # skips the iteration
    else :
        print(count)
        count+=1
print("\n\n\n")
# for loop

numbers = [0,1,2,3,4,5]
for number in numbers:  # number is temporary name to refer to the list's items, valid only inside this loop
    print(number) #  the numbers will be printed line by line, from 0 to 5
print("\n\n")
language = "Python"
for letter in language :
    print(letter)
print("\n\n")
for i in range(len(language)):
    print(language[i])
print("\n\n")
numbers =(1,2,3,4,5)
for number in numbers:
    print(number)

# in dic
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key,"-",value)

# set
it_compaines ={"Facebook","Oracle","Apple","Meta"}
for companies in it_compaines:
    print(companies)
print("\n\n")
# break and continue part 2
numbers =(1,2,3,4,5)
for number in numbers:
    print(number)
    number+=1
    if number ==3:
        break

print("\n\n\n")
for number in numbers:
    print(number)
    number+=1
    if number ==3:
        continue
    print("The next number should be ",number+1) if number !=5 else print("loop ends")
print("outside the loop")