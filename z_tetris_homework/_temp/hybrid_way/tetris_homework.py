from pprint import pprint
from _config import *
from _functions import *


fields = get_blank_fields(12, 8)

key, start = ('b', 0 )
b_arrays, shape = get_block_array(key)   # 'b' = ([[1, 1, 1], [0, 1, 0]], (2, 3))

first_2line = get_cut_fields(fields, row=2, posy=0)

block_arrays = pos_modified_block_arrays(key='g', start=2)
row, col = shape = np.shape(np.array(block_arrays))

if __name__ == '__main__':
    print(first_2line)
    print(block_arrays)
    print(pos_modified_block_arrays(key='g', start=2))
