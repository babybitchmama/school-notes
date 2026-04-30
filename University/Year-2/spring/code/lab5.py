def decimal_to_base_4(num):
    """
    Convert a decimal number to its base 4 representation.

    Parameters:
        - num (int): The decimal number to convert.
    Returns:
        - str: The base 4 representation of the input number.
    """
    result = ""

    while num > 0:
        q = num // 4
        r = num % 4
        result = str(r) + result
        num = q

    return result


result1 = decimal_to_base_4(372)
result2 = decimal_to_base_4(161)
result3 = decimal_to_base_4(52)

print(result1 == '11310')
print(result2 == '2201')
print(result3 == '310')
