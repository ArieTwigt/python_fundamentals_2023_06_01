# Assignment 1

#%%
def contents_box(length: float, width: float, height: float) -> float:
    '''
    Function that returns the contents of a box:

    Params:
    * length
    * width
    * height

    Returns:
    * contents 
    '''
    content = length * width * height
    return content

#%%
contents_box(10, 3, 3)

# %% Assignment 2

def capitalize_names(names_list):

    new_names_list = []

    for name in names_list:
        name_capitalized = name.capitalize()
        new_names_list.append(name_capitalized)

    return new_names_list

#%%
my_list = ['jim', 'john', 'marc', 'danny', 'peter']

capitalize_names(my_list)
# %%
