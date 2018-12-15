"""-------------------------
# 02.함수정의
# 위치: ./_functions.py
#
#\n\n\n"""
# print(__doc__)

from pprint import pprint
from _config import *


def get_blank_fields(rows, cols):
    # OUT(1): 빈 어레이 (필드)를 반납한다.
    return [[0 for i in range(cols)] for n in range(rows)]


def get_input():
    # input = a4 --> split into 'A' & 4
    # return ... name='A', start=4
    input_str = input('NEXT=').upper()
    (name,  start) = input_str[0], int(input_str[1])
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


def chk_noblock_foward(start):
    # if '1' in _strings return 'Fasle'
    # '1' Not exist,  True -- 'no block'
    _string = ""
    for n in range(10):
        _string += fields[n + 2]
    return _string.find("1") == -1


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
    # # show blank fields
    # pprint(get_blank_fields())
    #
    # # show all block dict
    # show_all_block_arrays()
    #
    # # show a single block
    # _keys = "ace"
    # show_block_array(*_keys)

    dimensions = get_shape([1, 2, 1])
    print(dimensions)

    pass
