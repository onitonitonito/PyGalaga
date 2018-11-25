"""------------------------------
# module.01 - variable setting : configuration
# location : ./_config.py
#
#\n\n\n"""
print(__doc__)

# block dimension = max.[2x4]
blocks = [
    ['1111',
     '0000', ],
    ['111',
     '010', ],
    ['11',
     '11', ],
    ['110',
     '011', ],
    ['011',
     '110', ],
    ['111',
     '001', ],
    ['001',
     '111', ],
]

# block dimensions
dimensions = [(2, 4), (2, 3), (2, 2), (2, 3), (2, 3), (2, 3), (2, 3)]

# block names
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# mix 3 into dic together
DICT_BLOCK = {names[i]: [dimensions[i], blocks[i]] for i in range(len(blocks))}

# define fields
fields = ['0' * 8 for i in range(12)]

# resets blocks - 2 lines.
resets = ['00000000', '00000000']
