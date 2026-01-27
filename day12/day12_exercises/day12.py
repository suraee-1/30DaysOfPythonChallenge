#Write a function which generates a six digit/character random_user_id. 
import random 
import string

def generate_six_digit_char():
    random_string= ""
    characters = string.ascii_letters+string.digits
    for i in range(0,6):
        random_string+=characters[int(random.random()*len(characters))]
    return random_string
print(generate_six_digit_char())

# Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def user_id_gen_by_user():
    num_of_char = int(input("Enter no characters to be generated : "))
    num_of_ids = int(input("Enter the no no ids to be generated : "))
    characters = string.ascii_letters+string.digits
    user_id=set()
    random_string= ""
    for _ in range(num_of_ids):
        for _ in range(num_of_char):
            random_string+=random.choice(characters)

        user_id.add(random_string)
        random_string=""
    return user_id



print(user_id_gen_by_user())

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    colour = list()
    for _ in range(3):
        colour.append(int(random.random()*256))
    return colour
print(rgb_color_gen())