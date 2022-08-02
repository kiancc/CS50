# TODO
from cs50 import get_string


def main():

    string = get_string('Text: ')

    # Assigns various counts to variables
    letter_count = letters(string)
    word_count = words(string)
    sentence_count = sentences(string)

    # Calculates average letters and sentences per 100 words
    L = (letter_count/word_count) * 100
    S = (sentence_count/word_count) * 100

    # Calculates grade
    index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(index)

    # Returns grade based on score
    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print("Grade {}".format(grade))

# Counts number of letters in text


def letters(string):

    count = 0

    for i in range(0, len(string)):
        if string[i].isalpha():
            count += 1

    return count

# Counts number of words in text


def words(string):

    word_counter = len(string.split(" "))

    return word_counter

# Counts number of sentences in text


def sentences(string):

    count = 0

    for i in range(0, len(string)):
        if string[i] == '.' or string[i] == '!' or string[i] == '?':
            count += 1

    return count


main()

