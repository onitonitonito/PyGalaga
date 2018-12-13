"""------------------------------
# module.02 - main functions
# location : ./_functions.py
#
#\n\n\n"""
if __name__ != '__main__':
    print(__doc__)

from _config import *
from pprint import pprint


def get_input():
    # input = a4 --> split into 'A' & 4
    # return ... name='A', start=4
    input_str = input('NEXT=').upper()
    (name,  start) = input_str[0], int(input_str[1])
    return name, start


def mix_2_lines(line_a, line_b):
    # mix 2 lines(str) by adding : str -> int -> str(return)
    # return mixed new lines (8bits) = str
    (collided, bit, mixed_line) = (0, 0, "")
    for i in range(8):
        bit = int(line_a[i]) + int(line_b[i])
        if bit > 1:
            collided = 1
        mixed_line += str(bit)
    return (mixed_line, collided)


def make_replaces(name, start):
    # input = 'A', 4 / output = block shape array
    # make array of 2 str-lines -- _replaces['str-1', 'str-2']
    _replaces = []
    _11 = "0" * (start - 1)
    _12 = DICT_BLOCK[name][1][0]
    _13 = "0" * (8 - DICT_BLOCK[name][0][1] - start + 1)
    _replaces.append(_11 + _12 + _13)

    _21 = "0" * (start - 1)
    _22 = DICT_BLOCK[name][1][1]
    _23 = "0" * (8 - DICT_BLOCK[name][0][1] - start + 1)
    _replaces.append(_21 + _22 + _23)
    return _replaces


def reset_2line(fields, *replaces, line):
    for replace in replaces:
        fields[line] = replace
        line += 1
    return fields


def chk_no_block_foward(start):
    # if '1' in _strings return 'Fasle'
    # '1' Not exist,  True -- 'no block'
    _string = ""
    for n in range(10):
        _string += fields[n + 2]
    return _string.find("1") == -1


def show_field(fields):
    # show fields
    for i in range(12):
        print(fields[i])


if __name__ == '__main__':

    (name, start) = ('A', 1)
    replaces = make_replaces(name, start)

    reset_2line(fields, *replaces, line=0)
    show_field(fields)
    print("-" * 20, "\n\n")

    collid = 0
    bumper_line = 0

    for i in range(10):
        bumper_line += 1
        new_line, collid = mix_2_lines(
            fields[bumper_line],
            fields[bumper_line + 1],
        )

        if collid:      # stop changing procedure!
            break

        else:
            fields[bumper_line - 1] = "00000000"
            fields[bumper_line] = replaces[0]
            fields[bumper_line + 1] = new_line

        if name == 'A':
            fields[i], fields[i-1] =  fields[i-1], fields[i]

    show_field(fields)
    pass
