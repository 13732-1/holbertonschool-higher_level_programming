#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name
    count = len(argv)

    # Determine the correct pluralization and punctuation
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(count))

    # Print each argument with its index
    for i in range(count):
        print("{:d}: {:s}".format(i + 1, argv[i]))
