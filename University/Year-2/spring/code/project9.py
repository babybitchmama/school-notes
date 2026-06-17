'''
Word Frequency Analysis
'''
import doctest


def load_and_clean_text(file_path):
    """
    Reads text from a file, converts it to lowercase,
    and removes punctuation.
    """
    punctuation = '!"#$%&\'()+,-./:;<=>?@[\\]^_`{|}~'

    file = open(file_path, "r")
    text = file.read().lower()
    file.close()

    cleaned_text = ""

    for char in text:
        if char not in punctuation:
            cleaned_text += char

    return cleaned_text


def count_words(text):
    """
    Counts the frequency of each word in the text.

    >>> count_words("hello world")
    {'hello': 1, 'world': 1}

    >>> count_words("this is a test this is only a test")
    {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}

    >>> count_words("Python python PYTHON")
    {'python': 3}

    >>> count_words("")
    {}

    >>> count_words("word")
    {'word': 1}
    """
    word_freq = {}

    words = text.split()

    for word in words:
        word = word.lower()

        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq


def save_counts_to_file(frequencies, output_file, top_n=10):
    """
    Saves the top N most common items in the dictionary to a file.
    :param frequencies: Dictionary with frequencies
    :param output_file: File to write the results to
    :param top_n: Number of top items to save
    """
    # Sort the dictionary by frequency (descending)
    sorted_items = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

    file = open(output_file, 'a')
    file.write(f"\nTop {top_n} word counts:\n")
    for item in sorted_items[:top_n]:
        file.write(f"{item[0]}: {item[1]}\n")
    file.close()


def main():
    """
    Main function to orchestrate text processing and save results to a file.
    """
    file_path = 'sample.txt'
    output_file = 'frequency_analysis_results.txt'

    # Load and clean the text
    text = load_and_clean_text(file_path)

    # Perform word counts
    word_counts = count_words(text)

    # Save results to file
    file = open(output_file, 'w')
    file.write("Frequency Analysis Results\n")
    file.write("=" * 30 + "\n")
    file.close()

    # append results to file
    save_counts_to_file(word_counts, output_file)


main()
#doctest.testmod(verbose = True)
