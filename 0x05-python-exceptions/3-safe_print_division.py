#!/usr/bin/python3
def safe_print_division(a, b):
    """
    This function divides 2 integers and prints the result
    """
    try:
        x = a / b
    except ZeroDivisionError:
        x = None
    finally:
        print("Inside result: {}".format(x))
        return x
