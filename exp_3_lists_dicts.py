#%%
person_1 = {"name": "John",
          "age": 50,
          "hobbies": ["football", "tennis", "chess"],
          "spouse": {"name": "Mary",
                     "age": 45, 
                     "hobbies": ["hockey", "reading", "boxing"]}}

person_2 = {"name": "Jack", 
            "city": "Amsterdam"}

persons_list = [person_1, person_2]

# %%
names_list = ["Arie", "John", "Arie"]
ages_list = [20, 30, 40, 50]

persons_dict = dict(zip(names_list, ages_list))
# %%
person = {"name": "Arie", "age": [50, 39] }

#%%
person["name"]
# %%
person["name"] = "Jim"
# %%
