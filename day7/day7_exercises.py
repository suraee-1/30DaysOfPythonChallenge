# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


#Exercises: Level 1

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(["Infosis","Wipro","TCS"])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove("TCS")
print(it_companies)

# What is the difference between remove and discard
it_companies.discard("TCS")
#it_companies.remove("TCS") # raises key error if not present

#Exercises: Level 2

#Join A and B
C = A.union(B)
print(C)

#Find A intersection B

print(A.intersection(B))

#Is A subset of B

print (A.issubset(B))

#Are A and B disjoint sets

print(A.isdisjoint(B))

#Join A with B and B with A
C= A.union(B)
D =B.union(A)
print(C.union(D))

#What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#Delete the sets completely
del it_companies,A,B,C,D

#Exercises: Level 3

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?

ages_set =set(age)
print(ages_set)

print(f"Length of Age[list] > length of Age(set) : {len(age)>len(ages_set)}")

#Explain the difference between the following data types: string, list, tuple and set  
# String -  A string is an immutable sequence of characters used to represent text. Strings can be empty and are indexed and ordered.
# list - A list is an ordered, mutable collection that can store multiple data types and allows elements to be added, removed, or modified.
# tuple - A tuple is an ordered collection similar to a list, but it is immutable, meaning its elements cannot be changed after creation.
# set -A set is an unordered collection of distinct elements.Elements are stored using hashing, so the order is not guaranteed, but items can be added or removed efficiently.

#I am a teacher and I love to inspire and teach people.
#  How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people"
word_list = sentence.split()
print(word_list)
unique_words = set(word_list)
print(unique_words)