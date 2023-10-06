!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    """Returns length of string and its 1st char"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

