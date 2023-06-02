#%%
numbers_list = [10, 20, 30, 40]

for i in numbers_list:
    print(i * 100)


# %%
names_list = ['Arie', 'Dirk', 'Jaap']
names_list_upper = []

for i in names_list:
    names_list_upper.append(i.upper())

# %%
for idx, name in enumerate(names_list):
    print(f"De naam {name} staat op plek {idx}")



# %%
names_list = ['Dirk', 'Arianne', 'Stephany', 'Jaap']

long_names_list = []
short_names_list = []

for name in names_list:
    if len(name) > 4:
        long_names_list.append(name)
    elif len(name) <= 4:
        short_names_list.append(name)


#%%
long_names_list = [name for name in names_list if len(name) > 4]


# %%
