#!/usr/bin/python3
def safe_print_integer(value):
    """
    The function prints an integer with string format
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
