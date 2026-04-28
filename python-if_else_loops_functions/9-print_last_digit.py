#!/usr/bin/python3
def print_last_digit(number):
    """Function that prints and returns the last digit of a number."""
    if number < 0:
        last_digit = (number * -1) % 10
    else:
        last_digit = number % 10
    print("{:d}".format(last_digit), end="")
    return last_digit
