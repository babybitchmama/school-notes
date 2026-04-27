"""
Hashem A. Damrah
In Class Activity 2
"""


def problem_1():
    """
    We want the output of this function to be:
    `Hot`.
    But, if we run it, it prints:
    ```
    Not Freezing
    Hot
    ```
    This happens because we want to use elif statements, meaning if the first statement is true, the rest of the statements will not be checked. But, if we use if statements, all statements will be checked, and since the second statement is true, it will print "Not Freezing" and then check the third statement, which is also true, so it will print "Hot".
    """
    temperature = 88
    if temperature < 32:
        print("Freezing")
    if temperature >= 32:
        print("Not Freezing")
    if temperature > 80:
        print("Hot")


def problem_2():
    """
    The output of the function will be:
    ```
    Negative
    Slightly Negative
    ```
    """
    number = -5
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
        if number < -10:
            print("Very Negative")
        else:
            print("Slightly Negative")
    else:
        print("Zero")


def problem_3():
    """
    The output of the function will be:
    ```
    10
    8
    6
    ```
    We terminate the loop when x is no longer greater than 5, which happens when x is equal to 4. So, the last value of x that is printed is 6.
    """
    x = 10
    while x > 5:
        print(x)
        x = x - 2


def problem_4():
    """
    The output of the function will be:
    ```
    0 + 1 + 2 + 3 + 4 = 10
    ```
    """
    total = 0
    num = 1
    while num <= 4:
        total = total + num
        num = num + 1
    print(total)


def problem_5():
    """
    This function will run indefinitely because the value of x is always greater than or equal to 10, so the condition of the while loop will always be true, and the loop will never terminate.
    In order to correct this, we need to change the last line from `x = x + 1` to `x = x - 1`, so that the value of x will decrease with each iteration of the loop, and eventually, it will become less than 0, which will terminate the loop.
    """
    x = 10
    while x >= 0:
        print(x)
        x = x + 1


def problem_6():
    """
    The output of the function will be:
    ```
    10
    ```
    """
    def calculate(num):
        result = 0
        while num > 0:
            result = result + num
            num = num - 1
        print(result)

    calculate(4)


def problem_7():
    """
    The return type of this function is: int
    The value of this function is:
    n = -5: 0
    n = 7: 14
    n = 15: 25
    """
    def compute(n):
        if n < 0:
            return 0
        elif n < 10:
            return n * 2
        else:
            return n + 10
    print(compute(-5))
    print(compute(7))
    print(compute(15))


def problem_8():
    """
    The return type of this function is: string
    The value of this function is:
    a = 10, b = 20, c = 2: "Condition A"
    """
    def complex_eval(a, b, c):
        if (a > 0 or b / c > 5) and c != 0:
            return "Condition A"
        elif c == 0 or (b / c <= 5 and a <= 0):
            return "Condition B"
        return "Condition C"
    print(complex_eval(10, 20, 2)
