def calculate_percentages(frequencies):
    """
    Calculate percentages for each letter.
    """
    percentages = {}

    # Step 1: Calculate total number of letters
    total_letters = sum(frequencies.values())

    # Step 2: Calculate percentage for each letter
    for letter, count in frequencies.items():
        percentages[letter] = (count / total_letters) * 100

    # Step 3: Return percentages
    return percentages


def calculate_percentages(frequencies):
    """
    Calculate percentages for each letter.
    """
    percentages = {}

    # Step 1: Calculate total number of letters
    total_letters = sum(frequencies.values())

    # Step 2: Calculate percentage for each letter
    for letter, count in frequencies.items():
        percentages[letter] = (count / total_letters) * 100

    # Step 3: Return percentages
    return percentages
