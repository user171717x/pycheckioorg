import string


def is_acceptable_password(password: str) -> bool:
    return ((password.lower().count('password') == 0) and
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

"""
Best "Clear" Solution

def is_acceptable_password(password: str) -> bool:
    # C1 : the length should be bigger than 6;
    # C2 : should contain at least one digit, but cannot consist of just digits.
    # C3 : having numbers or containing just numbers does not apply to the password longer than 9.
    # C4 : a string should not contain the word "password" in any case.
    c1 = len(password) > 6
    c2 = any(map(str.isdigit, password)) and not password.isdigit()
    c3 = len(password) > 9
    c4 = 'password' not in password.lower()
    return c1 and (c2 or c3) and c4
"""


"""
Best "Speedy" Solution

def is_acceptable_password(password: str) -> bool:
    # your code here
    if len(password) > 6:
        for x in password:
            if x.isdigit():
                return True
        return False
    else:
        return False
"""