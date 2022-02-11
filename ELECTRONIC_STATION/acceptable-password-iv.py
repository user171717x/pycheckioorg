import string


def is_acceptable_password(password: str) -> bool:
    return (len(password) > 6) and (True if len(password) > 9 else
                                    (bool(set(password).intersection(set('0123456789'))) and
                                    bool(set(password).intersection(set(string.ascii_letters)))))


print(is_acceptable_password('short'))
print(is_acceptable_password('short54'))
print(is_acceptable_password('muchlonger'))
print(is_acceptable_password('ashort'))
print(is_acceptable_password('muchlonger5'))
print(is_acceptable_password('sh5'))
print(is_acceptable_password('1234567'))
print(is_acceptable_password('12345678910'))

"""
Best "Clear" Solution

def is_acceptable_password(password: str) -> bool:
    return (len(password)>6 and not password.isdigit() and not password.isalpha()) or len(password)>9

"""


"""
Best "Speedy" Solution

def is_acceptable_password(password: str) -> bool:
    return len(password) > 9 or (    len(password) > 6
                                 and any(ch.isdigit() for ch in password)
                                 and not password.isdigit())
"""