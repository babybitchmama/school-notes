import turtle


def setup_screen():
    """Initialize and configure the screen"""
    screen = turtle.Screen()
    screen.title("Number System Converter")
    screen.bgcolor("black")
    screen.setup(800, 600)
    return screen


def create_turtle():
    """Create and configure the turtle for writing"""
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed(0)
    t.color("white")
    return t


def get_number(screen):
    """Get decimal number input from user"""
    while True:
        num = screen.numinput("Number Input",
                              "Enter a decimal number (0 or positive):",
                              default=0,
                              minval=0)
        if num is not None:
            return int(num)


def get_base(screen):
    """Get the target base from the user (2-8)"""
    while True:
        base = screen.numinput("Base Input",
                               "Enter the target base (2-8):",
                               default=2,
                               minval=2,
                               maxval=8)
        if base is not None:
            return int(base)


def decimal_to_base(decimal, base):
    """
    Convert a decimal (base-10) number to the given base.

    Parameters:
        decimal (int): A non-negative integer in base 10 to be converted.
        base (int): The target base to convert to (between 2 and 8).

    Returns:
        str: A string representing the converted number in the target base.
             Returns '0' if the decimal input is 0.

    >>> decimal_to_base(372, 8)
    '564'
    >>> decimal_to_base(10, 2)
    '1010'
    >>> decimal_to_base(0, 5)
    '0'
    """
    if decimal == 0:
        return "0"

    result = ""
    num = decimal

    while num > 0:
        r = num % base
        result = str(r) + result
        num = num // base

    return result


def write_line(t, x, y, text, font_size=20, font_style="normal"):
    """
    Write a single line of text at the given position.

    Parameters:
        t (turtle.Turtle): The turtle object used for writing.
        x (int): The x-coordinate for the text position.
        y (int): The y-coordinate for the text position.
        text (str): The text to display.
        font_size (int): The size of the font. Default is 20.
        font_style (str): The style of the font ('normal', 'bold', 'italic'). Default is 'normal'.
    """
    t.goto(x, y)
    t.write(text, align="center", font=("Courier", font_size, font_style))


def display_results(t, decimal, base, converted):
    """
    Display the conversion results on the turtle screen in a formatted layout.

    Parameters:
        t (turtle.Turtle): The turtle object used for writing.
        decimal (int): The original decimal number entered by the user.
        base (int): The target base the number was converted to.
        converted (str): The converted number as a string in the target base.
    """
    t.color("cyan")
    write_line(t, 0, 220, "Number System Converter", font_size=28, font_style="bold")

    t.color("white")
    write_line(t, 0, 175, "-" * 42, font_size=16)

    t.color("yellow")
    write_line(t, 0, 120, "Decimal (Base 10) Input:", font_size=18, font_style="bold")
    t.color("white")
    write_line(t, 0, 75, str(decimal), font_size=24, font_style="bold")

    t.color("lime")
    write_line(t, 0, 20, "converts to", font_size=16, font_style="italic")

    t.color("yellow")
    write_line(t, 0, -40, "Base " + str(base) + " Result:", font_size=18, font_style="bold")
    t.color("white")
    write_line(t, 0, -90, converted, font_size=36, font_style="bold")

    t.color("white")
    write_line(t, 0, -150, "-" * 42, font_size=16)

    t.color("gray")
    write_line(t, 0, -195, str(decimal) + " (base 10)  =  " + converted + " (base " + str(base) + ")", font_size=15)


def main():
    screen = setup_screen()
    t = create_turtle()

    decimal = get_number(screen)
    target_base = get_base(screen)

    converted = decimal_to_base(decimal, target_base)
    display_results(t, decimal, target_base, converted)

    screen.mainloop()


main()
