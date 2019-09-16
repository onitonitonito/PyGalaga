"""
#
#
#
#\n\n\n"""
print(__doc__)

import os
import sys
from os.path import dirname

sys.path.append(dirname(dirname(__file__)))
#---- ADD Parent folder ----------------------
# C:\Users\...\Documents\Github\PyGalaga\components ... HERE!
# C:\Users\...\Documents\Github\PyGalaga            ... PARENT!



if __name__ == '__main__':
    # Test if dir exist in sys-path
    _as = sys.path

    for _a in _as:
        if _a.find("Github") == -1:
            continue
        else:
            print(_a)
