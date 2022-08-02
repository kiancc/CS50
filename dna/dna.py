import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py FILENAME.csv FILENAME.csv")

    database = []
    # TODO: Read database file into a variable
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            database.append(row)

    sequence = []
    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as file:
        sequence = file.read().strip()

    count = {}
    str_sequence = []
    # TODO: Find longest match of each STR in DNA sequence
    with open(sys.argv[1], "r") as file:
        str_sequence = file.readline().strip().split(",")
        str_sequence.remove("name")

    for i in range(0, len(str_sequence)):
        count[str_sequence[i]] = longest_match(sequence, str_sequence[i])

    match = ""
    # TODO: Check database for matching profiles
    for i in range(0, len(database)):
        checker = 0
        for key in count:
            if count[key] == int(database[i][key]):
                checker += 1
        if checker == len(count):
            match = database[i]["name"]

    if not match:
        print("No match")
    else:
        print(match)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
