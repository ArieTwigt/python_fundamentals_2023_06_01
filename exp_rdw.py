#%%
import requests
import pandas

#%%
merk = input("Voer een merk in:\n")
merk_upper = merk.upper()
response = requests.get(f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={merk_upper}")

# %%
data = response.json()
# %%
data_df = pandas.DataFrame(data)
# %%
data_df.to_csv(f"export_{merk}.csv", sep=";", index=False)
# %%
