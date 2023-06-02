#%% Assignment 1 Create a conditional statement that indicates if your name starts with an "A or not
my_name = input("What is your name?\n")

first_letter = my_name[0].lower()

if first_letter == "a":
    print("Your name starts with an a")

#%% Assignment 2
vowels = ['a', 'e', 'o', 'u', 'i', 'y']

my_name = input("What is your name?")

first_letter = my_name[0].lower()

if first_letter in vowels:
    print("Your name begins with a vowel")
    my_name = my_name.replace(my_name[0], "B")
    print(my_name)
else:
    print("Your name does not begin with a vowel")
    my_name = my_name.replace(my_name[0], "A")
    print(my_name)


# %% b.
import string
import random


letters = string.ascii_letters
vowels = ['a', 'e', 'o', 'u', 'i']
non_vowels = [letter for letter in letters if letter not in vowels]

my_name = input("What is your name?")

first_letter = my_name[0].lower()

if first_letter in vowels:
    print("Your name begins with a vowel")
    random_letter = random.choice(non_vowels)
    my_name = my_name.replace(my_name[0], random_letter.upper())
    print(my_name)
else:
    print("Your name does not begin with a vowel")
    random_letter = random.choice(vowels)
    my_name = my_name.replace(my_name[0], random_letter.upper())
    print(my_name)

#%% Assignment 4a
my_age =  int(input("What is your age?"))  

if my_age > 18 and my_age < 68:
    print("You are between 18 and 68")
else:
    print("You are not")


# %% Assignment 4b
my_age =  int(input("What is your age?"))  

if 18 < my_age <  68:
    print("You are between 18 and 68")

