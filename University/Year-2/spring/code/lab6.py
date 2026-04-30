import doctest


def is_valid_phone(number):
    if len(number) != 10:
        return False
    return number.isdigit()


def is_valid_phone_with_area(number):
    if not is_valid_phone(number):
        return False
    return number[0:3] in ['503', '541', '971']


def is_valid_international_phone(number):
    """
    Validate international phone number

    >>> is_valid_international_phone('+15031234567')
    True
    >>> is_valid_international_phone('5031234567')  # Missing +1
    False
    >>> is_valid_international_phone('+1503123')    # Too short
    False
    >>> is_valid_international_phone('+19711234567')  # Valid 971 area code
    True
    >>> is_valid_international_phone('+12121234567')  # Invalid area code
    False
    """
    if not number.startswith('+1'):
        return False

    rest = number[2:]

    return is_valid_phone_with_area(rest)


doctest.testmod(verbose=True)
