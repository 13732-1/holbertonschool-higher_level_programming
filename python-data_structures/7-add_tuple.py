#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples by their first two elements."""
    # Ensure each tuple has at least 2 elements by padding with (0, 0)
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Calculate the sum of the first two corresponding elements
    result = (a[0] + b[0], a[1] + b[1])

    return result
