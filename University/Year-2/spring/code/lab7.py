def read_words(filename):
    """
    Read and return words in a file
    """
    words = []
    file = open(filename, 'r')
    for line in file:
        word = line.strip()
        words.append(word)
    return words

def find_longest_word(words):
    """
    Find and return the longest word in a list
    """
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def replace_a_with_double_at(words):
    """
    Replace all 'a' with '@@' in each word
    """
    modified_words = []

    for word in words:
        modified_word = word.replace("a", "@@")
        modified_words.append(modified_word)

    return modified_words

def read_and_print_longest_word(filename):
    """
    Read and print the longest word in a file
    """
    words = read_words(filename)
    modified_words = replace_a_with_double_at(words)
    longest = find_longest_word(modified_words)
    print(longest)

read_and_print_longest_word("animals.txt")
