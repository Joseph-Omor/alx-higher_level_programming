#!/usr/bin/python3
def safe_function(fct, *args):
    """
    This function executes a function safely
    """
    try:
        d_result = fct(*args)
    except Exception as err:
        d_result = None
        print("Exception: {}".format(err), file=sys.stderr)
    finally:
        return d_result
