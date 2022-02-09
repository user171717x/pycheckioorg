def checkio(values: list) -> list:
    return sorted(values, key=lambda x: int((x ** 2) ** 0.5))

print(checkio([-20, -5, 10, 15]))

"""
Best "Clear" Solution

def checkio(numbers_array):
    return tuple(sorted(numbers_array, key=abs))
"""


"""
Best "Speedy" Solution

def checkio(numbers_array):
    b=sorted(numbers_array, key=lambda x:(abs(x)))
    return b
"""