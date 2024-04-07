#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    The function prints the first x elements of a list
    and only integers
    """
    try:
        number = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                number += 1
                print("{:d}".format(my_list[i]), end="")
    except TypeError as err:
        print(err)
        return number
    else:
        print("")
        return number
