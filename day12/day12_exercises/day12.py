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

# hexa decimal color generator
"""Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples)."""

def hex_colour_generator(num):
    hex_char = "abcdef"
    list_of_colours =[]
    for _ in range(num):
        colour = "#"+"".join(random.choice(string.hexdigits[:16])  for _ in range(6))
        list_of_colours.append(colour)
    return list_of_colours
print(hex_colour_generator(6))
    

"""Write a function list_of_rgb_colors which returns any number of RGB colors in an array."""

def list_of_rgb_colours(num):
    colours =[]
    for _ in range(num):
        colours.append(rgb_color_gen())
    return colours

print(list_of_rgb_colours(6))

#Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_colours(type_of_code,num_of_colours):
    type_of_code=type_of_code.lower()
    colours=[]
    if type_of_code == "rgb" :
        for _ in range (num_of_colours):
            colours.append(rgb_color_gen())
    elif type_of_code =="hex":
        colours.extend(hex_colour_generator(num_of_colours))
    else :
        return "Invalid Type"
    return colours

print(generate_colours("rgb",2))
print(generate_colours("hex",2))

# level 3
#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
lst=[0,1,2,3,4,5,6,7]
def shuffle_list(lst):
    shuffle =[]
    while not(len(lst))==len(shuffle):
        x = random.choice(lst)
        if x not in shuffle:
            shuffle.append(x)
    return shuffle
print(shuffle_list(lst))

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def list_of_seven_random():
    random_seven =[]
    while not len(random_seven)==7 :
         x = random.randint(0,9)
         if x not in random_seven:
             random_seven.append(x)
    return random_seven

print(list_of_seven_random())