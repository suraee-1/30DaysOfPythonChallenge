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
