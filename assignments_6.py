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


###### Assignment 2 - Create a loop that prints the name of the day for the following 10 days
#%%
from datetime import date, timedelta

today_date = date.today()

num_days = 10

days_names_list = []

for num_day in range(1, num_days + 1):
    new_date = today_date + timedelta(days=num_day)
    day_name = new_date.strftime("%A")

    if day_name not in ['Saturday', 'Sunday']:
        days_names_list.append(day_name)

# %%
today_date = date.today()

days_count = 0

days_names_list = []


while days_count < 10:
        today_date = today_date + timedelta(days=1)
        day_name = today_date.strftime("%A")

        if day_name not in ['Saturday', 'Sunday']:
            days_names_list.append(day_name)
            days_count += 1
# %%
