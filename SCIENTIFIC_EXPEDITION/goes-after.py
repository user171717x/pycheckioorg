def goes_after(word: str, first: str, second: str) -> bool:
    return (word.index(second) if word.count(second) else -100) \
           - (word.index(first) if word.count(first) else -100) == 1


print(goes_after('world', 'w', 'o'))
# print(goes_after('world', 'w', 'r'))
# print(goes_after('world', 'l', 'o'))
# print(goes_after('panorama', 'a', 'n'))
# print(goes_after('list', 'l', 'o'))
# print(goes_after('', 'l', 'o'))
# print(goes_after('list', 'l', 'l'))
# print(goes_after('world', 'd', 'w'))
# print(goes_after("almaz","m","a"))


"""
Best "Clear" Solution

def goes_after(word: str, first: str, second: str) -> bool:
    try:
        return word.index(second)-word.index(first) == 1
    except ValueError:
        return False

"""


"""
Best "Speedy" Solution

def goes_after(word: str, first: str, second: str) -> bool:
    i = word.find(first)
    return i >= 0 and word.find(second) == i+1
"""