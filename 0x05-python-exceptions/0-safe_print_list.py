#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    The Function prints x elements of a list
    """
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
    except IndexError:
        return i
    else:
        return x
    finally:
        print("")
