"""
Hashem A. Damrah
Project 3
Turtle Graphics Artwork - Spiral Galaxy of Geometric Shapes
"""

import turtle


def draw_spiral_square(t, side_length, color, num_iterations):
    """
    Draws a spiral made of squares that grows outward.

    Parameters:
        t (turtle.Turtle): The turtle object used for drawing.
        side_length (float): The starting length of each side of the square.
        color (str): The color of the spiral square.
        num_iterations (int): How many squares to draw in the spiral.
    """
    t.color(color)
    for i in range(num_iterations):
        for _ in range(4):
            t.forward(side_length + i * 5)
            t.left(90)
        t.left(10)


def draw_star(t, size, color, points):
    """
    Draws a star with a given number of points.

    Parameters:
        t (turtle.Turtle): The turtle object used for drawing.
        size (float): The length of each line in the star.
        color (str): The color of the star.
        points (int): The number of points on the star.
    """
    t.color(color)
    angle = 180 - (180 / points)
    for _ in range(points):
        t.forward(size)
        t.right(angle)


def setup_screen():
    """
    Sets up the turtle screen with a black background and title.

    Parameters:
        None
    """
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Spiral Galaxy of Geometric Shapes")
    return screen


def create_turtle():
    """
    Creates and returns a turtle object with speed set to maximum.

    Parameters:
        None
    """
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    return t


def main():
    """
    Main function that sets up the screen and draws the full artwork
    by calling draw_spiral_square and draw_star multiple times
    with different parameters, positions, sizes, and colors.

    Parameters:
        None
    """
    setup_screen()
    t = create_turtle()

    # --- Draw spiral squares in different positions and colors ---

    t.penup()
    t.goto(-200, 100)
    t.pendown()
    draw_spiral_square(t, 10, "cyan", 18)

    t.penup()
    t.goto(150, 100)
    t.pendown()
    draw_spiral_square(t, 10, "magenta", 18)

    t.penup()
    t.goto(-30, -150)
    t.pendown()
    draw_spiral_square(t, 10, "yellow", 18)

    t.penup()
    t.goto(-200, -250)
    t.pendown()
    draw_spiral_square(t, 5, "lime", 12)

    t.penup()
    t.goto(200, -220)
    t.pendown()
    draw_spiral_square(t, 5, "orange", 12)

    # --- Draw stars scattered across the canvas ---

    t.penup()
    t.goto(0, 50)
    t.pendown()
    draw_star(t, 120, "white", 5)

    t.penup()
    t.goto(-280, -50)
    t.pendown()
    draw_star(t, 60, "red", 6)

    t.penup()
    t.goto(280, 30)
    t.pendown()
    draw_star(t, 60, "deepskyblue", 7)

    t.penup()
    t.goto(0, 220)
    t.pendown()
    draw_star(t, 50, "gold", 8)

    t.penup()
    t.goto(-100, -280)
    t.pendown()
    draw_star(t, 45, "violet", 5)

    t.penup()
    t.goto(130, -270)
    t.pendown()
    draw_star(t, 45, "tomato", 6)

    turtle.done()


main()
