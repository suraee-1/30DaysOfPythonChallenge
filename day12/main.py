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

import sys

print("Welcome {}.Enjoy {} the challenge!".format(sys.argv[1],sys.argv[2]))

# to exit sys
#sys.exit()

# to know path
sys.path
# to know the version of python
sys.version
#to know the largest integer
print(sys.maxsize)

# Satistics Module
from statistics import *
ages = [20,22,20, 20, 42, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

# from the math module

import math #as obj
print(math.pi)
print(math.pow(2,3))
print(math.floor(9.81))
print(math.ceil(10.23))# rounding to highest
print(math.log10(100)) # log with base 10
#help(math) # checks all the functions the module has
print(dir(math)) # returns all the functions in a list
print(help(os.mkdir))

# changign name of a function while importing

from math import pi as pie
print(pie)

# string module
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

#random module
from random import random, randint
print(random()) # returns value from 0 to 0.99
print(randint(5,20)) # both 5 and 20 are inclusive


