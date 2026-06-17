def find_timestamp_of_highest_temp(readings, high):
    """
    Finds the timestamp of the highest temperature

    Args:
        readings: list of tuples
        high: highest temperature

    Returns:
        str: timestamp of the highest temperature
    """
    for time, temp in readings:
        if temp == high:
            return time


def find_stats(readings):
    """
    Finds temperature statistics

    Args:
        readings: list of (time, temperature) tuples

    Returns:
        tuple: (high, high_time, low, avg)
    """
    high = readings[0][1]
    low = readings[0][1]
    total = 0

    for time, temp in readings:
        if temp > high:
            high = temp
        if temp < low:
            low = temp
        total += temp

    avg = total / len(readings)
    high_time = find_timestamp_of_highest_temp(readings, high)

    return high, high_time, low, avg


def display_report(readings, high, high_time, low, avg):
    """
    Displays temperature summary report
    """
    print("\nSummary:")
    print(f"  Highest:  {high:.1f}° (at {high_time})")
    print(f"  Lowest:   {low:.1f}°")
    print(f"  Average:  {avg:.1f}°")


def read_temperature_file(filename):
    """
    Reads temperature data from a file.

    Args:
        filename: name of the file

    Returns:
        list of (time, temperature) tuples
    """
    readings = []

    file = open(filename, "r")

    for line in file:
        line = line.strip()
        time, temp = line.split(",")

        readings.append((time, float(temp)))

    file.close()

    return readings


def main():
    readings = read_temperature_file("temperatures.txt")

    high, high_time, low, avg = find_stats(readings)

    display_report(readings, high, high_time, low, avg)


main()
