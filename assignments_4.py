#%% Assignment 1
from datetime import date

next_birthday = date(2024, 4, 1)

# %%
today_date = date.today()
days_to_next_birthday = (next_birthday - today_date).days

# %% Assignment 2
import math

diameter = 10
radius = diameter / 2
size = math.pow(radius, 2) * math.pi
print(size)

# %% Assignments 3
import os

files_in_dir = os.listdir()
print(files_in_dir)

# %% Assignment 4
os.mkdir("our_functions")

# %%
