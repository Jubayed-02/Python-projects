# password generator
import string
import secrets


# def contains_upper(password: str) -> bool:
#     if string.ascii_uppercase in password:
#         return True

#     return False


# def contains_symbol(password: str) -> bool:
#     if string.punctuation in password:
#         return True

#     return False


def password_generator(length: int, symbol: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbol:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase

    combination_length: int = len(combination)
    new_pass: str = ""

    for _ in range(length):
        new_pass += combination[secrets.randbelow(combination_length)]
    

    return new_pass

pass_length = int(input("Enter the length of the password >> "))
print(password_generator(pass_length, True, True))
 