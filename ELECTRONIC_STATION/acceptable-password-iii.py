
def is_acceptable_password(password: str) -> bool:
    return (len(password) > 6 and
            bool(set(password).intersection(set('0123456789'))) and
            bool(set(password).difference(set('0123456789'))))


print(is_acceptable_password('short'))
print(is_acceptable_password('muchlonger'))
print(is_acceptable_password('ashort'))
print(is_acceptable_password('muchlonger5'))
print(is_acceptable_password('sh5'))
print(is_acceptable_password('1234567'))

"""
Best "Clear" Solution

is_acceptable_password = lambda p: 0 < sum(c.isdigit() for c in p) < len(p) > 6

"""


"""
Best "Speedy" Solution

def is_acceptable_password(password: str) -> bool:
    return (    len(password) > 6
            and any(ch.isdigit() for ch in password)
            and not password.isdigit())
"""