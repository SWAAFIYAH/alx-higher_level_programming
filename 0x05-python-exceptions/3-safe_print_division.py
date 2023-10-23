#!/usr/bin/python3
#divides two integers
def safe_print_division(a, b):
    try:
        division = a / b
    except (TypeError, ZeroDivisionError):
        division = None
    finally:
        print("Inside result: {}".format(division))
    return (division)
