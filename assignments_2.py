# Assignments
# Assignment 1 - Append .Jr. to the current full_name variable which will result in Erling Haaland Jr.
#%%
first_name = "Erling"
last_name  = "Haaland"

full_name  = first_name + last_name
print(full_name)

#%% a. (using the '+' operator)
first_name + " " + last_name + " .Jr"

# %% b. (using an f-string)
f"{first_name} {last_name} .Jr"

# Assignment 2 - replace the first name of Erling Haaland (Erling) to only the abbreviation of his first hame. This should result in: E. Haaland Jr.
# %%
first_letter = first_name[0]
f"{first_letter}. {last_name} .Jr"

# Assignment 3 - Create a variable called nationality with the value "Norway". Use this variable to create the string (sentence) "E. Haaland .Jr - Nationality: Norway". Print out the sentence.
# %%
name_abbrv = f"{first_letter}. {last_name} .Jr"
nationality = "Norway"
sentence = f"{name_abbrv} - Nationality: {nationality}"
sentence
# %%
