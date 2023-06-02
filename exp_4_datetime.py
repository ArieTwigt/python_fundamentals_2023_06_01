#%%
from datetime import date, datetime, timedelta

#%% get the date of today
today_date = date.today()
# %%
time_now = datetime.now()
# %%
today_date.month

# %% maak een date aan
birthday_date = date(2024, 4, 1)

# %% verschil tussen 2 dates
birthday_date - today_date

# %% dagen optellen bij een date
today_date + timedelta(days=1000)

# %% Get the current month (https://strftime.org/)
today_date.strftime("%B")
# %%
today_date.strftime("Today is a lovely %A")
# %%

# %%
