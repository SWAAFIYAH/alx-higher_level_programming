#!/usr/bin/python3
#excutes a functoin safely
import sys
def safe_function(fct, *args):
    try:
        final = fct(*args)
        return (final)
    except Exception as i:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
