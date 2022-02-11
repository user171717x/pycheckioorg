import string


def is_all_upper(text: str) -> bool:
    is_empty = bool(len(text))
    more_one_symbol = bool(set(text).intersection(set(string.ascii_letters)))
    all_upper = True
    for symbol in text:
        if symbol.islower():
            all_upper = False
            break
    return is_empty and more_one_symbol and all_upper


print(is_all_upper('ALL UPPER'))
print(is_all_upper('all lower'))
print(is_all_upper('mixed UPPER and lower'))
print(is_all_upper(''))
print(is_all_upper("     "))


"""
Best "Clear" Solution

def is_all_upper(text: str) -> bool:
    # your code here
    return text.isupper()
"""

"""
Best "Creative" Solution

is_all_upper = str.isupper
"""

"""
Best "Speedy" Solution

def is_all_upper(text: str) -> bool:
    return text.isupper()
"""