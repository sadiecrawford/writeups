#!/usr/bin/env python3
import string

def encode(msg):
    output = ''

    for i in range(len(msg)):
        temp = ord(msg[i]) * 0x40
        temp = temp >> 4
        if 0xc0 <= temp < 0xe8:
            output = str(int(msg[i]) * 0x1234) + output
        else:
            output = chr(ord(msg[i]) * 0x10) + output

    return output


# TODO implement the decode function
def decode(msg):
    output = ''

    # Create encoded -> decoded dictionaries
    encoded_numbers = {
        '4660' : '1',
        '9320' : '2',
        '13980' : '3',
        '18640' : '4',
        '23300' : '5',
        '27960' : '6',
        '32620' : '7',
        '37280' : '8',
        '41940' : '9',
        '0' : '0'
    }
    keys = string.printable
    encoded_chars = {}
    for key in keys:
        encoded_chars[encode(key)] = key

    print(msg)
    for i in range(len(msg)):
        if not msg[i].isnumeric():
            output = encoded_chars[msg[i]] + output
        else:
            output = msg[i] + output

    output = output[::-1]
    for key, val in encoded_numbers.items():
        output = output.replace(key, val)
    output = output[::-1]

    return output


def shift(msg):
    j = len(msg) - 1
    output = ''

    for i in range(len(msg)//2):
        output += msg[i] + msg[j]
        j -= 1

    return output


# TODO implement the unshift function
def unshift(msg):
    output = ''

    i = 0
    while i < len(msg):
        output += msg[i]
        i += 2

    i = len(msg) - 1
    while i >= 0:
        output += msg[i]
        i -= 2

    return output


if __name__ == '__main__':
    # shifted = shift('<REDACTED>')
    # hashed = encode(shifted)
    hashed = '4660۠ܰ4660ڀ٠װװސ23300۰ސݐ18640ܠݰװۀڠ18640۰ްؠѠȐՀȐа4660ѠȐѠߐА'
    # CODE HERE
    unhashed = decode(hashed)
    print(unhashed)
    print(unshift(unhashed))
