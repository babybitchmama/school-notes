import random

def load_words(filename):
    """
    Reads a text file line by line and stores each line in a list.

    Parameters:
    filename (str): The name of the file to read.

    Returns:
    list: A list of strings, each representing a line from the file.
    """
    words = []
    fin = open(filename)
    for line in fin:
        word = line.strip()  # Use .strip() to remove any trailing newline characters
        words.append(word)  
    return words

def return_hangman_ASCII(tries):
    """Return the hangman ASCII art based on remaining tries."""
    stages = [
            """
===========
    |    |
    O    |
   /|\\   |
    |    |
   / \\   |
         |
===========""",
"""
===========
    |    |
    O    |
   /|\\   |
    |    |
   /     |
         |
===========""",
"""
===========
    |    |
    O    |
   /|\\   |
    |    |
         |
         |
===========""",
"""
===========
    |    |
    O    |
   /|    |
    |    |
         |
         |
===========""",
"""
===========
    |    |
    O    |
    |    |
    |    |
         |
         |
===========""",
"""
===========
    |    |
    O    |
         |
         |
         |
         |
===========""",
        """
===========
    |    |
         |
         |
         |
         |
         |
==========="""]
    return stages[tries]

def display_game_state(word, guessed_letters, tries):
    """Display the current game state. This function prints to the console."""

    print(return_hangman_ASCII(tries))
    print()

    # Display the word with guessed letters revealed
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Guessed letters:", guessed_letters)
    print("Tries remaining:", tries)


def get_valid_guess(guessed_letters):
    """Get a valid letter guess from the player. This is a fruitful function."""

    while True:
        guess = input("Enter a letter: ").upper()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Please enter an alphabetical character.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess

def is_subset(word, guessed_letters):
    """
    Checks if all letters in a given word have been guessed.

    Args:
        word (str): The word to check.
        guessed_letters (list or set): The letters that have been guessed.

    Returns:
        bool: True if every letter in the word is in guessed_letters, False otherwise.
    """
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True


def play_game(word):
    """Play one game of hangman."""
    word = word.upper()
    guessed_letters = list()
    tries = 6

    print("\nWelcome to Hangman!")
    print("Try to guess the word one letter at a time.")

    while tries > 0:
        display_game_state(word, guessed_letters, tries)

        # Check if word is completed
        if is_subset(word, guessed_letters):
            print("\nCongratulations! You won! The word was: " + word)
            return True

        # Get player's guess
        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        # Check if guess is incorrect
        if guess not in word:
            tries -= 1
            print("\nSorry, '" + guess + "' is not in the word!")
            if tries == 0:
                display_game_state(word, guessed_letters, tries)
                print("\nGame Over! The word was: " + word)
                return False
        else:
            print("\nGood guess! '" + guess + "' is in the word!")

def play_again():
    """Ask if player wants to play another game."""
    while True:
        response = input("\nWould you like to play again? (yes/no): ").lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'")

def main():
    """Main game loop"""
    words = load_words("vocab.txt")

    print("=" * 40) #create 40 ='s and print
    print("Welcome to Hangman!")
    print("=" * 40) #create 40 ='s and print

    while True:
        word = random.choice(words)
        play_game(word)
        if not play_again():
            print("\nThanks for playing!")
            return

main()
