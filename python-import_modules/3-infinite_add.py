#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    # sys.argv[1:] contains all arguments except the script name
    for arg in sys.argv[1:]:
        total += int(arg)
    print("{:d}".format(total))
