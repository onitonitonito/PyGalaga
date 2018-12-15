"""-------------------------
# 01.메인 - 앱,런
# 위치: ./run_app.py
#
#\n\n\n"""
# print(__doc__)

from pprint import pprint
from _config import *
from _functions import *

FIELDS = get_blank_fields(8, 12)


def main(fields):
    # global FIELDS
    # _key = "a", start=4
    _key, start = get_input()

    b_array, dimension = get_block_array(_key)

    fields = block_placed_fields(
        fields=FIELDS,
        b_array=b_array,
        dimension=dimension,
        start=start
    )

    show_block_array(_key)
    print("\n", dimension, "\n")

    show_raw_fields(FIELDS)
    print()

    rot_fields = rotate_90(FIELDS)
    show_raw_fields(rot_fields)

    print()
    show_conv_fields(rot_fields)


if __name__ == '__main__':
    while 1:
        main(FIELDS)

    pass
