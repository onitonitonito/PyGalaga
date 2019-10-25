"""
# _parent_path.py - 상위 디렉토리를 참조하기 위한 화일
"""
print(__doc__)

import os
import sys
from os.path import dirname


sys.path.insert(0, dirname(dirname(__file__)))

if __name__ == '__main__':
    # Test if dir exist in sys-path
    _as = sys.path

    for _a in _as:
        if _a.find("GitHub") == -1:
            print("*", _a)
            # continue
        else:
            print(_a)
