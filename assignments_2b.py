# %% Assignment 1
first_name = "Erling"
last_name  = "Haaland"

full_name  = first_name + last_name
print(full_name)
# %% a.
first_name + " " + last_name + " .Jr"

# %% b.
full_name_new = f"{first_name} {last_name} .Jr"

# %% Assignment 2
full_name_new.replace("Erling", "E.")

# %%
full_name_new = "Arie Twigt"
first_letter = full_name_new[0]
full_name_new.replace(first_name, first_letter)
# %% c.
full_name_list = full_name_new.split(" ")
first_name = full_name_list[0]
last_name = full_name_list[1:]
last_name_str = " ".join(last_name)

full_name_2 = f"{first_name} {last_name_str}"
full_name_2

# %%
