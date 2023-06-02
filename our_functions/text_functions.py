def remove_vowels(name:str) -> str: 
    """
    Function that removes vowels from a given name

    (a, e, o, u , i)

    Params:
    * name (str)

    Returns:
    * A string with the vowels removed
    """

    vowels = ['a', 'e', 'o', 'u', 'i']

    new_name = ""
    
    for letter in name.lower():
        if letter not in vowels:
            new_name += letter

    return new_name


def capitalize_names(names_list):

    new_names_list = []

    for name in names_list:
        name_capitalized = name.capitalize()
        new_names_list.append(name_capitalized)

    return new_names_list