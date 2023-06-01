#%%
full_name = "Arie Twigt .Sr"
# %%
full_name_list =  full_name.split(" ")
# %%
first_name = full_name_list[0]

#%%
first_letter = first_name[0]

# %%
last_name = full_name_list[1:]
# %%
last_name_str =  " ".join(last_name)
# %%
f"{first_letter}. {last_name_str}"
# %%
