#!/usr/bin/python3
"""This scipt is the UTF-8 validation module.
"""


def validUTF8(data):
    """This site Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    skip = 0
    n = len(data)
    for z in range(n):
        if skip > 0:
            skip -= 1
            continue
        if type(data[z]) != int or data[z] < 0 or data[z] > 0x10ffff:
            return False
        elif data[z] <= 0x7f:
            skip = 0
        elif data[z] & 0b11111000 == 0b11110000:
            # The 4-byte utf-8 character encoding...
            span = 4
            if n - z >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[z + 1: z + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[z] & 0b11110000 == 0b11100000:
            # The 3-byte utf-8 character encoding
            span = 3
            if n - z >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[z + 1: z + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[z] & 0b11100000 == 0b11000000:
            # This is 2-byte utf-8 character encoding...
            span = 2
            if n - z >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[z + 1: z + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False
    return True
