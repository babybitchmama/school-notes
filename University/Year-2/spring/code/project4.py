"""
Hashem A. Damrah
Project 4
"""


def river_crossing_simulation():
    """
    This function simulates the river crossing riddle. It uses a list of booleans to represent the position of the characters, where False represents the left bank and True represents the right bank. The order of the characters in the list is [farmer, wolf, goat, cabbage]. The function displays the game state, gets user input, and changes the state based on the input until it reaches an end state (either winning or losing).
    """

    characters = [False, False, False, False]

    display_description()

    while has_reach_end_state(characters) < 1:
        show_game_state(characters)
        choice = get_input()
        change_state(characters, choice)
    show_game_state(characters)


def get_input():
    """
    This function gets input from the user to move the characters. It prompts the user to enter 'h', 'w', 'g', or 'c' to move the farmer, wolf, goat, or cabbage respectively. It also includes error handling to ensure that the input is valid.
    """

    char = input("Please enter h, w, g or c to move the characters: ")
    while char.lower() not in ["h", "w", "g", "c"]:
        print("Your input is not valid.")
        char = input("Please reenter h, w, g or c to move the characters: ")
    return char


def display_description():
    """
    This function displays the rules of the game to the user. It explains the objective of the game, the constraints on moving the characters, and the consequences of leaving certain characters alone together.
    """

    s = "-------------------------------------------------------------------------------\n"
    s += "River Crossing Riddle Simulation\n"
    s += "-------------------------------------------------------------------------------\n"
    s += "The farmer wants to move the wolf, the goat and the cabbage across the river,\n"
    s += "but he can only carry one thing at a time on his boat. if you leave the goat \n"
    s += "alone with the cabbage the goat will eat the cabbage and the wolf will eat \n"
    s += "the goat if it gets the chance alone with it. \n"
    s += (
        "The farmer always moves move other characters or by himself. Each character \n"
    )
    s += "can only move to the other bank if they are on the same bank as the farmer."
    print(s)


def show_game_state(actors):
    """
    This function displays the current state of the game, showing which characters are on which bank of the river. It uses the list of booleans to determine the position of each character and prints a visual representation of the two banks and the river in between.
    """

    bank0 = ""
    bank1 = ""
    line = "\n----------------------------------------\n"
    if actors[0]:
        bank1 = bank1 + "        H"
    else:
        bank0 = bank0 + "        H"
    if actors[1]:
        bank1 = bank1 + "        W"
    else:
        bank0 = bank0 + "        W"
    if actors[2]:
        bank1 = bank1 + "        G"
    else:
        bank0 = bank0 + "        G"
    if actors[3]:
        bank1 = bank1 + "        C"
    else:
        bank0 = bank0 + "        C"
    river = "\n ~~~~       ~~~~~~~\n       ~~~~    ~~~\n"
    print("\nGAME STATE:")
    print(bank0 + line + river + line + bank1 + "\n")


def change_state(actors, char):
    """
    This function changes the state of the game based on the user's input. It toggles the position of the characters in the list of booleans according to the rules of the game. The farmer can move alone or with one of the other characters, but only if they are on the same bank as the farmer.
    """

    index_map = {"h": 0, "w": 1, "g": 2, "c": 3}

    farmer_pos = actors[0]
    chosen_index = index_map[char.lower()]

    if char.lower() == "h":
        actors[0] = not actors[0]
        return

    if actors[chosen_index] == farmer_pos:
        actors[0] = not actors[0]
        actors[chosen_index] = not actors[chosen_index]
    else:
        print("Invalid move: character is not on the same bank as the farmer.")


def has_reach_end_state(actors):
    """
    This function checks if the game has reached an end state, either a winning state where all characters are on the right bank, or a losing state where the wolf eats the goat or the goat eats the cabbage. It returns 1 if an end state is reached and 0 otherwise.
    """

    human, wolf, goat, cabbage = actors

    if all(actors):
        print("Congratulations! You successfully moved everyone across!")
        return 1

    if wolf == goat and human != wolf:
        print("Game Over: The wolf ate the goat!")
        return 1

    if goat == cabbage and human != goat:
        print("Game Over: The goat ate the cabbage!")
        return 1

    return 0


if __name__ == "__main__":
    river_crossing_simulation()
