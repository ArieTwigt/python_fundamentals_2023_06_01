#%% Assignment 1a

names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']

vowels = ['a', 'e', 'o', 'u', 'i']

for name in names_list:
    for letter in name:
        if letter in vowels:
            name = name.replace(letter, "")
 


#%%
#%% Assignment 1b
names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']

new_names = []

vowels = ['a', 'e', 'o', 'u', 'i']

for name in names_list:
    new_name = ""
    for letter in name:
        if letter not in vowels:
            new_name+=letter
    
    new_names.append(new_name)

print(new_names)


# %%
naam += "T"
print(naam)
# %%
