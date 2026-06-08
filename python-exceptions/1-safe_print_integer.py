#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer using the "{:d}".format() syntax.

    Args:
        value: The value to be printed, can be any type.

    Returns:
        bool: True if value was successfully printed as an integer,
              False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
