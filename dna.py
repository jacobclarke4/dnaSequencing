import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py CSVNAME TXTNAME")

    # TODO: Read database file into a variable
    csv_file = open(sys.argv[1], "r")
    csv_reader = csv.reader(csv_file, delimiter=",")
    row1 = next(csv_reader)
    subsequence_data = row1[1:]

    # TODO: Read DNA sequence file into a variable
    txt_file = open(sys.argv[2], "r")
    txt_reader = txt_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    longest_seq_num = 0
    longest_seq = ""
    my_dict = {key: None for key in subsequence_data}
    for subs in subsequence_data:
        long = longest_match(txt_reader, subs)
        my_dict[subs] = long

    # TODO: Check database for matching profiles
    for row in csv_reader:
        num_matches = 0
        for i in range(1, len(row), 1):
            # print(f"{row[i]} == {my_dict[subsequence_data[i-1]]} ")
            if int(row[i]) == int(my_dict[subsequence_data[i - 1]]):
                num_matches += 1
        if num_matches == len(subsequence_data):
            print(row[0])
            csv_file.close()
            txt_file.close()
            exit(1)
    print("No match")
    csv_file.close()
    txt_file.close()
    return


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
