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


def get_shape(arrays):
    try:
        rows, cols = len(arrays), len(arrays[0])
    except:
        rows, cols = 1, len(arrays)
    return rows, cols


def get_block_array(key):
    # IN (1): 블록네임 키값을 받는다 = "a"
    # OUT(2): 블록 어레이 반환 / 디맨전(행,렬) 반환 함
    key = key.upper()
    shape = rows, cols = get_shape(BLOCKS[key])
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
        print("{} = {}".format(_key, BLOCKS[_key]))


def show_raw_fields(fields):
    # DIS: raw_fields as array
    for row_ints in fields:
        print(row_ints)


def block_placed_fields(fields, b_array, dimension, start=1):
    # IN(3) = 변환할 필드, 블록키, 시작위치
    # OUT(1) = 변환된 필드 어레이를 반환
    (rows, cols) = dimension
    conv_start = 8 - (start + rows - 1)
    for i in range(rows):
        fields[i + conv_start] = \
            b_array[i] + fields[i + conv_start][cols:]
    return fields


def get_mixed_array(array1, array2):
    # retuen add value.
    np_array3 = (np.add(np.array(array1), np.array(array2)))
    return list(np_array3)


def get_evens_zerofill(array1, array2, order=1):
    _na, _nb = np.array(array1), np.array(array2)
    _col1, _col2 = np.shape(_na)[0], np.shape(_nb)[0]

    if _col1 == _col2:
        return array1, array2
    else:
        if _col1 > _col2:
            _rest = _col1 - _col2
            _nc = np.zeros(_rest)
            if order == 1:
                return array1, list(np.append(_nb, _nc).astype(int))
            else:
                return array1, list(np.append(_nc, _nb).astype(int))

        else:
            _rest = _col2 - _col1
            _nc = np.zeros(_rest)
            if order == 1:
                return list(np.append(_na, _nc).astype(int)), array2
            else:
                return list(np.append(_nc, _na).astype(int)), array2


def chk_noblock_foward(fields, key, start):
    arrays, shape = get_block_array(key)
    conv_start = 8 - start   # start=1 .. conv = 7
    rows = shape[0]          # 4

    array_sum = 0
    for i in range(rows):
        array_sum += sum(fields[conv_start - rows])

    if array_sum > 0 :
        return False
    return True

def go_bottom_fields(fields, key, start):
    arrays, shape = get_block_array(key)
    conv_start = 8 - start   # start=1 .. conv = 7
    rows = shape[0]          # 4

    for i in range(rows):
        fields[conv_start - rows] = arrays[rows-i]
    return fields

def rotate_90(fields):
    rot_fields = get_blank_fields(12, 8)
    for i in range(7, -1, -1):
        # print(arrays[i])
        for j in range(12):
            rot_fields[j][7 - i] = fields[i][j]
    return rot_fields


def show_conv_fields(fields):
    # 이것은 보류 .... PENDING .....!
    # IN: 하나 이상의 어레이 / 컨버트값(Value)
    # OUT: 스트링-라인으로 변경된 어레이를 반환
    # -- 컨버트값 : 0=. / ABCDEFG = 1
    # -- TODO: 최종적으로 90도 회전시켜 결과 보여줌
    conv_fields = []
    for i in range(8):
        fields_strs = [str(bit) for bit in fields[i]]
        _a = "".join(fields_strs)
        _b = _a.replace('0', '.')
        conv_fields.append(_b)

    for line in conv_fields:
        print(line)


if __name__ == '__main__':
    _a = [1,2,3,4,5,6,7,8,9]
    _b = [1,2,3]
    _na, _nb = get_evens_zerofill(_a, _b, order=1)
    print(_na)
    print(_nb)


    fields = get_blank_fields(8,12)
    _ = chk_noblock_foward(fields, "A", start=6)
    print(_)
    show_raw_fields(fields)

    # fields = go_bottom_fields(fields, "A", 1)
    # show_raw_fields(fields)

    # # show blank fields
    # pprint(get_blank_fields())
    #
    # # show all block dict
    # show_all_block_arrays()
    #
    # # show a single block
    # _keys = "ace"
    # show_block_array(*_keys)

    # dimensions = get_shape([1, 2, 1])
    # print(dimensions)

    pass
