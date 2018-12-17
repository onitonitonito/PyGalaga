"""-------------------------
# 01.메인 - 앱,런
# 위치: ./run_app.py
#
#\n\n\n"""
# print(__doc__)

from pprint import pprint
from _config import *
from _functions import *

# generate Empty fields array
fields = get_blank_fields(8, 12)


if __name__ == '__main__':
    in_pos = 0
    while 1:
        print('in_pos =', in_pos)

        _2str = INPUTS[in_pos]
        _key, start = get_key_start(_2str)

        print('NEXT= {}'.format(_2str.upper()))
        input()

        if in_pos < len(INPUTS) - 1:
            in_pos += 1
        else:
            in_pos = 0

        b_array, dimension = get_block_array(_key)
        fields = block_placed_fields(fields, b_array, dimension, start)

        show_block_array(_key)
        print("\n", dimension, "\n")

        show_raw_fields(fields)
        print()

        # rot_fields = rotate_90(fields)
        # show_raw_fields(rot_fields)

        # print()
        # show_conv_fields(rot_fields)
    pass
