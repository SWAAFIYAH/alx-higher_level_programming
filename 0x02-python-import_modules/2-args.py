#!/usr/bin/python3
if __name__ == "__main__":
    """print number and list of arguments"""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    else
        print("{} arguments:".format(count))
        for i in range(count):
            print("{}:{}".format(i + 1, sys.argv[1 + 1]))
