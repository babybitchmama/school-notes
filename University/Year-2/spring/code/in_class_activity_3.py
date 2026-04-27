def is_divisible_by_both(a, b, divisor):
    """
    Check if both a and b is divisible by divisor
    return True, if they are, False otherwise.

    What is the bug in the code below:
        The bug in the code is that it checks if either a or b is divisible by the divisor, instead of checking if both a and b are divisible by the divisor. The correct code should use the 'and' operator instead of the 'or' operator.
    """

    return a % divisor == 0 or b % divisor == 0


def print_even_numbers1(n):
    """
    Print all even numbers from 1 to `n`, inclusive.

    What is the bug in the code below:
        The bug in the code is that it isn't inclusive of n. The loop should run until n + 1 to include n in the output if n is even, so we would use range(i, n + 1) instead of range(i, n).
    """

    for i in range(1, n):
        if i % 2 == 0:
            print(i)


def print_even_numbers2(n):
    """
    Print all the even numbers from 1 to n (inclusive).

    What is the bug in the code below:
        The bug is that the condition in the loop only prints odd numbers, since 3 % 2 == 1, 5 % 2 == 1, etc. The condition should be i % 2 == 0 to print even numbers.
    """

    i = 1
    while i <= n:
        if i % 2 == 0:
            print(i)
        i += 1


def count_down(n):
    """
    Print all numbers from `n` down to 1, inclusive.

    What is the bug in the code below:
        The bug in the code is that it increments n instead of decrementing it. To count down from n to 1, we should use n -= 1 instead of n += 1.
    """

    while n > 0:
        print(n)
        n += 1


def count_divisors(n):
    """
    Count how many numbers between 1 and `n` divide `n` evenly.
    Return the count.

    What is the bug in the code below:
        The bug in the code is that it starts the loop from 0, which will cause a division by zero error when n % i is evaluated. The loop should start from 1 to avoid this error, so we should use range(1, n + 1) instead of range(n + 1).
    """

    count = 0
    for i in range(n+1):
        if n % i == 0:
            count += 1
    return count


def find_largest_digit(num):
    """
    Find the largest digit in the number `num`.
    Return the largest digit.

    What is the bug in the code below:
        The bug in the code is that it initializes largest to 0 and then checks if the current digit is less than largest, which will never update largest since all digits are greater than or equal to 0. The condition should be if digit > largest to find the largest digit correctly.
    """

    largest = 0
    while num > 0:
        digit = num % 10
        if digit < largest:
            largest = digit
        num //= 10
    return largest


def is_prime(n):
    """
    Check if a number `n` is prime using a while loop.
    Return True if it is a prime, False otherwise.

    What is the bug in the code below:
        The logic is flipped, the code returns True if n is divisible by any number from 2 to n, which means n is not prime. The correct logic should return False if n is divisible by any number from 2 to n, and return True if it is not divisible by any of those numbers.
    """

    if n <= 1:
        return False

    i = 2
    while i <= n:
        if n % i == 0:
            return True
        i += 1

    return False

print(is_prime(12))
