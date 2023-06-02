# Assignment 1

#%% a.
person = {"name": "John",
          "age": 50,
          "hobbies": ["football", "reading", "cycling"]}

# %% b.
person_2 = {}
person_2['name'] = "Jack"
person_2['age'] = 40
person_2['hobbies'] = ["chess", "running"]


# Assignment 2
#%%
my_family = {}
my_family['name'] = "Jones"

# %%
my_family['members'] = []

# %% create dictionaries containing information about the people
person_3 = {"name": "Mary", 
            "age": 20,
            "hobbies": ["gaming", "tennis"]}

person_4 = {"name": "Ann", 
            "age": 13,
            "hobbies": ["gaming", "hockey"]}

person_5 = {"name": "Carl", 
            "age": 12,
            "hobbies": ["reading", "programming"]}

#%%
my_family["members"] = [person, person_2, person_3, person_4, person_5]

#%%
person_6 = {"name": "Bobby",
            "age": 0,
            "hobbies": ["sleeping", "crying"]}

#%%
my_family['members'].append(person_6)
# %%
my_family['members'][3]['name'][0]
# %%
