"""-------------------------
# 02.함수정의
# 위치: ./_functions.py
#
#\n\n\n"""
# print(__doc__)

import numpy as np
from pprint import pprint
from _config import *


def get_blank_fields(rows, cols):
    # OUT(1): 빈 어레이 (필드)를 반납한다.
    return [[0 for i in range(cols)] for n in range(rows)]


def get_key_start(str_2digits):
    # IN(1) : key-in = 2 digits
    # input = a4 --> split into 'A' & 4
    # return ... name='A', start=4
    (name,  start) = str_2digits[0], int(str_2digits[1])
    return name, start


def get_block_array(key):
    # IN (1): 블록네임 키값을 받는다 = "a"
    # OUT(2): 블록 어레이 반환 / 디맨전(행,렬) 반환 함
    key = key.upper()
    shape = rows, cols = np.shape(np.array(BLOCKS[key]))
    return BLOCKS[key], shape


def show_block_array(*keys):
    # IN (1): 블록네임 키값을 받는다 = "A" or "ADE.."
    # DIS: 블록네임 / 블록어레이 보여줌
    for _key in keys:
        _key = _key.upper()
        print(_key)
        for bit in BLOCKS[_key]:
            print(bit)


def show_all_block_arrays():
    # DIS: key, block_array
    # show all block_dict array
    for _key in BLOCKS.keys():
        shape = np.shape(np.array(BLOCKS[_key]))
        print("[{}]:{} = {}".format(_key, shape, BLOCKS[_key]))


def get_vertical_array(array):
    # 버티칼 order 로 쪼개서, 1열로 세우고 (concatenate)
    # 다시 행열을 바꿔서 Reshape 한다. (수직방향 order)
    # 그냥 Reshape 는 수평방향 순서로 concatenate
    array = np.array(array)
    x, y = splits = np.shape(array)
    concat = np.split(np.concatenate(np.split(array, y, axis=1)), x * y)
    return np.reshape(a=concat, newshape=(y, x)).tolist()


def get_cut_fields(fields, row=2, posy=0):
    cut_arrays = []
    if row > 1:
        for i in range(row):
            cut_arrays.append(fields[posy + i])
    else:
        cut_arrays.append(fields[posy])
    return cut_arrays


def chk_no_empty_arrays(arrays):
    n_arrays = np.array(arrays)
    return np.sum(n_arrays)


def pos_modified_block_arrays(key, start):
    b_arrays, shape = get_block_array(key)
    row = shape[0]

    modif_b_arrays = []
    if row > 0:
        for i in range(row):
            _a = [0] * start   # [0, 0, 0] or []
            _a.extend(b_arrays[i])
            _a.extend([0] * (8 - (start + shape[0] + 1)))
            modif_b_arrays.append(_a)
    else:
            _a = [0] * start   # [0, 0, 0] or []
            _a.extend(b_arrays)
            _a.extend([0] * (8 - (start + shape[0] + 1)))
            modif_b_arrays.append(_a)
    return modif_b_arrays


def block_placed_fields(fields, arrays, posy=0):
    # IN(3) = 변환할 필드, 블록키, 시작위치
    # OUT(1) = 변환된 필드 어레이를 반환
    n_arrays = np.array(arrays)
    row, col = shape = np.shape(n_arrays)

    cut_fields = get_cut_fields(fields, row, posy)
    n_cut_fields = np.array(cut_fields)
    return np.add(n_cut_fields, n_arrays).tolist()


def get_mixed_array(array1, array2):
    # retuen add value.
    np_array3 = (np.add(np.array(array1), np.array(array2)))
    return list(np_array3)


def _chk_noblock_foward(fields, key, start):
    arrays, shape = get_block_array(key)
    conv_start = 8 - start   # start=1 .. conv = 7
    rows = shape[0]          # 4

    array_sum = 0
    for i in range(rows):
        array_sum += sum(fields[conv_start - rows])

    if array_sum > 0:
        return False
    return True


def _go_bottom_fields(fields, key, start):
    arrays, shape = get_block_array(key)
    conv_start = 8 - start   # start=1 .. conv = 7
    rows = shape[0]          # 4

    for i in range(rows):
        fields[conv_start - rows] = arrays[rows - i]
    return fields


if __name__ == '__main__':
    pass
