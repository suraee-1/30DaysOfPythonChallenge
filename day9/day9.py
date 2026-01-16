# if condition is true it executes the following code
a = 3
if a >0:
    print("A is a positive number.")

# if else condition if the first condition is true executes the first condition or it executes the else block
a =-3 
if a >0:
    print("A is a positive number.")
else:
    print("A is a negative number.")

# if else if condition
a =0
if a>0 :
    print("A is a positive number. ")
elif a<0 :
    print("A is a negative number.")
else :
    print("A is a zero.")

# Short Hand
a=-3
print("A is positive ") if a>0 else print("Not Positive")

# nested if 

a =11

if a>0:
    if a %2 ==0:
        print("A is positive and a even number")
    else:
        print("A is a positive number")
elif a ==0 :
    print("A is zero")
else :
    print("A is negative")

# with and operator

a =10
if a>=10 and a<=100:
    print("A lies between 0 and 100")
else :
    print("A is not in range")


#if with or operator

user ="James"
access_level =3
if user=="admin" or access_level>=4:
    print("Access Granted")
else:
    print("Acess denied")
    