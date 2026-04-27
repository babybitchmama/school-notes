"""
Hashem A. Damrah
Lab 3: Drawing Polygons with Turtle Graphics
"""

import turtle as t


def draw_polygon(n):
    """
    Draws a regular polygon with n sides using turtle graphics.

    We calculate the angle to turn after drawing each side as 360 degrees divided by n (the number of sides). The length of each side is set to a fixed value (100 in this case).
    """
    angle = 360 / n
    side_length = 100

    for _ in range(n):
        t.forward(side_length)
        t.right(angle)


draw_polygon(4)  # square
draw_polygon(3)  # triangle
draw_polygon(8)  # octagon

t.done()
