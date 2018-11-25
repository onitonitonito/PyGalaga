"""------------------------------
# main.00 - excute file
# location : ./_ing_test_tetris.py
#
#\n\n\n"""
print(__doc__)

from pprint import pprint
from _config import *
from _functions import *


while 1:
    # making 2 rows list = [replaces]
    (name, start) = get_input()
    replaces = make_replaces(name, start)

    reset_2line(fields, *replaces, line=0)
    show_field(fields)
    print("-"*20,"\n")


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
