import string


def is_acceptable_password(password: str) -> bool:
    return ((len(set(password)) > 2) and
            (password.lower().count('password') == 0) and
            (len(password) > 6) and
            (True if len(password) > 9 else (bool(set(password).intersection(set('0123456789'))) and
                                             bool(set(password).intersection(set(string.ascii_letters))))))


print(is_acceptable_password('short'))
print(is_acceptable_password('short54'))
print(is_acceptable_password('muchlonger'))
print(is_acceptable_password('ashort'))
print(is_acceptable_password('muchlonger5'))
print(is_acceptable_password('sh5'))
print(is_acceptable_password('1234567'))
print(is_acceptable_password('12345678910'))
print(is_acceptable_password('password12345'))
print(is_acceptable_password('PASSWORD12345'))
print(is_acceptable_password('pass1234word'))
print(is_acceptable_password('aaaaaa1'))
print(is_acceptable_password('aaaaaabbbbb'))

"""
Best "Clear" Solution


def is_acceptable_password(password: str) -> bool:
    # c1 : length should be bigger than 6
    # c2 : contains at least one digit but it can't be all digits
    # c3 : having numbers is not required for password longer than 10
    # c4 : string should not contain word "password" in any case
    # c5 : consist of 3 different letters
    c1 = len(password) >= 6
    c2 = any(map(str.isdigit, password)) and not password.isdigit()
    c3 = len(password) >= 10
    c4 = 'password' not in password.lower()
    c5 = len(set(password)) >= 3
    return c1 and (c2 or c3) and c4 and c5
"""

"""
Best "Speedy" Solution

def is_acceptable_password(password: str) -> bool:
    return (    'password' not in password.casefold()
            and len(set(password)) > 2
            and (len(password) > 9 or (    len(password) > 6
                                       and any(ch.isdigit() for ch in password)
                                       and not password.isdigit())))
"""