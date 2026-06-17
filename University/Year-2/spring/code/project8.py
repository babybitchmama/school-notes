'''
means and medians
'''

import turtle
import statistics
import doctest


def read_numbers(filename):
    """
    Reads numbers from a file and returns a list of lists.
    Each line in the file is converted to a list of integers.
    """
    file = open(filename, 'r')
    data = []
    for line in file:
        # Convert each line into a list of integers
        numbers = convert_to_int(line.split())
        data.append(numbers)
    return data


def convert_to_int(li):
    """
    Converts a list of strings to a list of integers.
    """
    int_list = []
    for st in li:
        int_list.append(int(st))
    return int_list


def calculate_mean_median(data):
    """
    Calculates the mean and median for each line of data.
    Returns a list of tuples with (mean, median).

    >>> calculate_mean_median([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [(2, 2), (5, 5), (8, 8)]

    >>> calculate_mean_median([[1, 2], [3, 4], [5, 6]])
    [(1.5, 1.5), (3.5, 3.5), (5.5, 5.5)]

    >>> calculate_mean_median([[1], [2], [3]])
    [(1, 1), (2, 2), (3, 3)]

    >>> calculate_mean_median([[2, 2, 2], [4, 4, 4], [6, 6, 6]])
    [(2, 2), (4, 4), (6, 6)]

    >>> calculate_mean_median([[5, 2, 8], [1, 3, 7], [4, 6, 10]])
    [(5, 5), (3.6666666666666665, 3), (6.666666666666667, 6)]
    """
    results = []

    for line in data:
        mean = statistics.mean(line)
        median = statistics.median(line)
        results.append((mean, median))

    return results


def display_mean_median(t, data):
    """ display means and medians in two columns"""

    t.penup()
    t.goto(-350, 250)
    t.color("black")

    font_size = 24

    # column headers
    t.write("Mean", font=("Arial", font_size, "bold"))
    t.goto(-100, 250)
    t.write("Median", font=("Arial", font_size, "bold"))

    y = 200

    for mean, median in data:
        t.goto(-350, y)
        t.write(f"{mean:.2f}", font=("Arial", font_size, "normal"))

        t.goto(-100, y)
        t.write(f"{median:.2f}", font=("Arial", font_size, "normal"))

        y -= 35


def setup_screen_turtle():
    """ Set up turtle graphics """
    screen = turtle.Screen()
    screen.title("Mean and Median Line Graph")
    screen.bgcolor("white")
    screen.setup(width=900, height=600)

    t = turtle.Turtle()
    t.hideturtle()
    return t


def main():
    filename = "data.txt"
    data = read_numbers(filename)

    if not data:
        print("No valid data found in the file.")
        return

    t = setup_screen_turtle();

    results = calculate_mean_median(data)

    display_mean_median(t, results)

    turtle.done()


main()
#doctest.testmod(verbose=True)
