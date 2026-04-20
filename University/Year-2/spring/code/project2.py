"""
Hashem A. Damrah
CS122 - project 2
"""


# problem 1
def find_min_of_three(a, b, c):
    """
    Find the minimum given three numbers.
    We do this by checking each possible case, if a < b and a < c => a is min. We do the same thing with the other two given numbers.
    """
    if a <= b and a <= c:
        return a
    if b <= a and b <= c:
        return b
    if c <= a and c <= b:
        return c


# problem 2
def print_string_list(string_list):
    """
    Prints each character from a given list on a new line.
    We do this by using a while loop with the condition that the current item number is less then the length of the list.
    """
    count = 0
    while count < len(string_list):
        print(str(count) + ". " + str(string_list[count]))
        count += 1


# problem 3
def sum_of_list(int_list):
    """
    Returns the sum of a given list of integers.
    We do this by using a for loop over the given list and we sum them up and return the resulting value
    """
    list_sum = 0
    for integer in int_list:
        list_sum += integer
    return list_sum


def main():
    print(find_min_of_three(1, 2, 3))
    print(find_min_of_three(1, -2, 3))
    print(find_min_of_three(-1, -2, -3))
    print(find_min_of_three(-1, -1, -1))
    x = 2
    y = 3
    z = 4
    print(find_min_of_three(x, y, z))

    print_string_list(['d', 'e', 'f'])
    print_string_list(['ab', 'c'])
    print_string_list(['1', '2', '3'])
    print_string_list(['hello', 'hi', 'hey'])
    x = ['a', 'b', 'c']
    print_string_list(x)
    print_string_list([])

    print(sum_of_list([1, 2, 3]))
    print(sum_of_list([-1, -2, -3]))
    print(sum_of_list([]))
    print(sum_of_list([-1, -2, 3]))
    x = [10, 3, 4]
    print(sum_of_list(x))


if __name__ == "__main__":
    main()
