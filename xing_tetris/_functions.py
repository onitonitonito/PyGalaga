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
    print("=" * 25)
    _input = input('\nNEXT=').upper()
    name,  start = _input[0], int(_input[1])
    return name, start


def make_replaces(name, start):
    # make input block in 2 lines -- _replaces[0],[1]
    # return 2 rows list
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


def mix_2_lines(line_a, line_b):
    # mix 2 lines(str) : str -> int -> str(return)
    # return mixed new lines (8bits) = str
    _collided, _bit, _mixed_line, = (0, 0, "")
    for i in range(8):
        _bit = int(line_a[i]) + int(line_b[i])
        if _bit > 1:
            _collided = 1
        _mixed_line += str(_bit)
    return (_mixed_line, _collided)


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
        _string += fields[n+2]
    return _string.find("1") == -1


def show_field(fields):
    # show fields
    for i in range(12):
        print(fields[i])


if __name__ == '__main__':
    replaces = make_replaces('B', 1)

    reset_2line(fields, *replaces, line=0)
    show_field(fields)
    print("-"*20,"\n\n")


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
            fields[bumper_line-1] = "00000000"
            fields[bumper_line] = replaces[0]
            fields[bumper_line+1] = new_line

    show_field(fields)
    pass
