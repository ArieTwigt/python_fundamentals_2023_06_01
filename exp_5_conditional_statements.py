#%%
guests_list = ["Dirk", "Bob", "James"]

#%%
if "Arie" in guests_list:
    print("You are in the list")

# %%
min_age = 18
my_age = 18

if my_age > min_age:
    print("Je bent ouder")
    print("Een andere regel")
elif my_age == min_age:
    print("Je bent even oud")
else:
    print("Je bent jonger")






print("De rest van de code")


# %%
my_name = "Arie"

if "e" in my_name:
    print("Your name contains an 'e'")

#%%
numbers_list = [1,2,3,4]
# %%


number = 7
if number in numbers_list:
    print(f"{number} is in the list")
else:
    print(f"{number} is not in the list")
    numbers_list.append(number)
    print(f"Added {number} to the list")

print(numbers_list)

# %%
my_dict = {"key_1": 1,
           "key_2": 2}

#%%
new_key = "key_10"

if new_key in my_dict.keys():
    print(f"{new_key} already in dict")
else:
    print(f"{new_key} not in dictionary")
    my_dict[new_key] = None

# %%
import os

files_folders = os.listdir()

folder_name = input("Add new folder")

if folder_name not in files_folders:
    print(f"Creating {folder_name}")
    os.mkdir(folder_name)
else:
    print(f"Folder {folder_name} already exists")









# %%
donation_amount = 1
donation_limit = 100

while donation_amount > 0:
    print(f"Donation amount: {donation_amount}")
    donation_amount += 1
# %%
