"""------------------------------
# main.00 - excute file
# location : ./_ing_test_tetris.py
#
#\n\n\n"""
print(__doc__)

from pprint import pprint       # for test
from _config import *
from _functions import *



while 1:
    # making 2 rows list = [replaces]
    print("=" * 25)
    (name, start) = get_input()
    replaces = make_replaces(name, start)

    # get set on the start
    reset_2line(fields, *replaces, line=0)
    show_field(fields)
    print("-"*20,"\n")

    pass
