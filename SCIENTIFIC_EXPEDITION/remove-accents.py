import unicodedata


def checkio(in_string):
    """remove accents"""
    return ''.join(c for c in unicodedata.normalize('NFD', in_string)
                   if unicodedata.category(c) != 'Mn')


print(checkio(u"préfèrent"))
print(checkio(u"loài trăn lớn"))
print(checkio("loài trăn lớn"))
print(checkio("àèìǹòùẁỳÀÈÌǸÒÙẀỲ"))
print(checkio("ằẰ"))

"""
https://www.compart.com/en/unicode/category/Mn
https://docs-python.ru/standart-library/modul-unicodedata-python/
"""

"""
... ???
"""

"""
Best "Clear" Solution

from unicodedata import normalize, category


def checkio(in_string):
    # normalize splits accented letters in two: letter + accent
    # category(c) 'Mn' contains every accent
    # http://www.fileformat.info/info/unicode/category/Mn/list.htm
    return ''.join(c for c in normalize('NFD', in_string) if category(c) != 'Mn')
"""


"""
Best "Speedy" Solution

from unicodedata import category, normalize


def checkio(in_string: str) -> str:
    return ''.join(ch for ch in normalize('NFKD', in_string)
                      if category(ch) != 'Mn')
"""