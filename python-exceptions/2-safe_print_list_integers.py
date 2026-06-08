#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list, skipping non-integers.

    Args:
        my_list (list): The list containing various types of data.
        x (int): The number of elements to access in my_list.

    Returns:
        int: The number of integers successfully printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
