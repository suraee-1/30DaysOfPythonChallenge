from my_module import generate_full_name
print(generate_full_name("John","Stark")) # import module.fun works like objects

# from my_module import generate_full_name, two_sum
from my_module import two_sum # for specific functions in a module
print(two_sum(2,4))

# importing functions and renaming 
from my_module import two_sum as sum
print(sum(3,4))

# import build in module of py

import os
# creating a directory
os.mkdir("FOLDER 1") # it will create a directory in the pwd  # if folder exists it will cause errors

#changing the current directory
#os.chdir("/Documents/MY Projects/30DaysOfPython/day12")

# getting current working directory

print(os.getcwd()) # pwd 

# removing the directory
os.rmdir("FOLDER 1")

# sys module