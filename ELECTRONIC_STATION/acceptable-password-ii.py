
def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and bool(set(password).intersection(set('0123456789')))


print(is_acceptable_password('short'))
print(is_acceptable_password('muchlonger'))
print(is_acceptable_password('ashort'))
print(is_acceptable_password('muchlonger5'))
print(is_acceptable_password('sh5'))

"""
Best "Clear" Solution

def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and any(map(str.isdigit, password))
"""


"""
Best "Speedy" Solution

def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and any(ch.isdigit() for ch in password)
"""