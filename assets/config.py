"""
# assets/config.py - 초기 변수값 정의
"""
print(__doc__)

import os
from assets.sprite import set_sprite


# WORKING DIR. SET
TOP = "PyGalaga"
DIRS = os.path.dirname(__file__).partition(TOP)
ROOT = "".join(DIRS[:2]) + '\\'

# BASIC
ENEMY_SPEED = 5

dir_big = ROOT + 'statics\\big\\'
dir_sprite = ROOT + 'statics\\sprite\\'

# OBJECT DICTIONARY
IMGS = {        # SIZE x, y, angle, file_name
    'img_fighter'  : [15, 16, 0, dir_sprite + 'Ship_White.png'],
    'img_lives'    : [15 * 0.6, 16 * 0.6, 0, dir_sprite + 'Ship_White.png'],
    'img_boom_01'  : [26, 26, 0, dir_sprite + 'Ship_explosion_0001.png'],
    'img_boom_02'  : [34, 32, 0, dir_sprite + 'Ship_explosion_0002.png'],
    'img_boom_03'  : [36, 35, 0, dir_sprite + 'Ship_explosion_0003.png'],
    'img_boom_04'  : [34, 32, 0, dir_sprite + 'Ship_explosion_0004.png'],
    'img_bullet'   : [ 5, 10, 0, dir_sprite + 'rocket_0001.png'],

    'img_bee'      : [15, 12, 180, dir_sprite + 'Fly_0001.png'],
    'img_pheonix'  : [13, 13, 180, dir_sprite + 'pheonix_0001.png'],
    'img_gremlin'  : [14, 14, 180, dir_sprite + 'gremlin_0001.png'],
    'img_scorpion' : [13, 13, 180, dir_sprite + 'scorpion_0001.png'],
    'img_catcher'  : [19, 18, 180, dir_sprite + 'Green_Catcher.png'],

    'img_logo'     : [679, 312, 0, dir_big + 'mobygames_logo.png'],
    'img_big_ship' : [200, 213, 0, dir_big + 'galaga_fighter.png'],
    'img_big_pheo' : [240, 240, 0, dir_big + 'galaga_pheo.png'],
    'img_enter'    : [240, 240, 0, dir_big + 'galaga_enter.png'],
    }


# SET SPRITE
scale_sprite = 4

for key in IMGS.keys():
    args = [int(IMGS[key][0] * scale_sprite),
            int(IMGS[key][1] * scale_sprite),
            IMGS[key][2], IMGS[key][3]]
    globals()[key] = set_sprite(*args)

# COLOR TABLE
BLACK = (0, 0, 0)     # fill black
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# SET INITIAL VARI.
SCREEN_SIZE = (480, 800)            # screen size = 480 x 640 default
FPS = 30

# FIGHTER'S POSITION
POS_X = (480-50)/2
POS_Y = (640-(53+20))

FIGHTER_WIDTH = IMGS['img_fighter'][0] * scale_sprite
FIGHTER_HEIGHT = IMGS['img_fighter'][1] * scale_sprite

ENEMY_WIDTH = IMGS['img_fighter'][0] * scale_sprite
ENEMY_HEIGHT = IMGS['img_fighter'][1] * scale_sprite


# KEY INCREASEMENT
X_MOVE = 0
Y_MOVE = 0
