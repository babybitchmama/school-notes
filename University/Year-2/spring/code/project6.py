'''
Project 6: Password Checker
Hashem A. Damrah
'''


import doctest

def password_check(password_str):
    """
    Checks if a password aligns with security requirements.

    >>> password_check('A99#')
    False
    >>> password_check('')
    False
    >>> password_check('Qwrty9')
    False
    >>> password_check('%CS122')
    False
    >>> password_check('#UODucks')
    False
    >>> password_check('#mypsw1')
    False
    >>> password_check('#qwrty')
    False
    >>> password_check('123456')
    False
    >>> password_check('#Qw99rty')
    True
    >>> password_check('OK99!!')
    True
    >>> password_check('#U02024')
    True
    """
    if len(password_str) < 6:
        return False

    has_upper = False
    has_digit = False
    has_special = False
    special_chars = "!@#$&*"

    for char in password_str:
        if char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    return has_upper and has_digit and has_special

def prompt_password():
    while True:
        password = input("Enter a password: ")
        if password_check(password):
            print("Password accepted.")
            break
        else:
            print("Invalid password. Passwords must be at least six characters long, include an uppercase character, a number, and a special character (!, @, #, $, &, *).")

def main():
    doctest.testmod(verbose=True)

if __name__ == "__main__":
    main()
