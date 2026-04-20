"""
Project 1
Author: Hashem A. Damrah
"""


def problem_1(percentage):
    """
    The original given code doesn't work (or it works, but it spits out multiple values), because we are using regular if statements, i.e., something like:
    ```
    if percentage >= 92:
        print("A")
    if percentage >= 82:
        print("B")
    if percentage >= 68:
        print("C")
    if percentage >= 62:
        print("D")
    else:
        print("F")
    ```
    Then, if percentage = 92.5, then we'll get the output of
    ```
    A
    B
    C
    D
    ```
    To fix this, we can use if-elif-else statements, which will only execute one of the branches. Meaning, if the first statement is true, then the rest of the statements will be skipped. So, we can write it as
    """
    if percentage >= 92:
        return "A"
    elif percentage >= 82:
        return "B"
    elif percentage >= 68:
        return "C"
    elif percentage >= 62:
        return "D"
    else:
        return "F"


def problem_2(celsius):
    """
    We just use a simple equation to convert Celsius to Fahrenheit, which is F = (C * 9/5) + 32. So, we can write it as
    """
    fahrenheit = (celsius * 9/5) + 32  # You don't need to assign it to a variable, you can just return the value directly, but I assigned it to a variable for clarity.
    return fahrenheit


def problem_3(number):
    """
    This is a simple FizzBuzz problem, where we need to print "Fizz" if the number is divisible by 3, "Buzz" if the number is divisible by 5, and "FizzBuzz" if the number is divisible by both 3 and 5. We can use if-elif-else statements to achieve this. So, we can write it as
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


def main():
    percentage = 92.5
    grade = problem_1(percentage)
    print(f"The grade for {percentage}% is: {grade}")

    celsius = 20
    fahrenheit = problem_2(celsius)
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

    number = 45
    result = problem_3(number)
    print(f"The result for the number {number} is: {result}")


if __name__ == "__main__":
    main()
