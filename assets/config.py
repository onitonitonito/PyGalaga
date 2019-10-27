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

# SET INITIAL VARI.
FPS = 30
SCALE_SPRITE = 4
SCREEN_SIZE = (480, 800)            # screen size = 480 x 640 default

DIR_BIG = ROOT + 'statics\\big\\'
DIR_SPRITE = ROOT + 'statics\\sprite\\'

# OBJECT DICTIONARY
IMGS = {        # SIZE x, y, angle, file_name
    'img_fighter'  : [15, 16, 0, DIR_SPRITE + 'Ship_White.png'],
    'img_lives'    : [15 * 0.6, 16 * 0.6, 0, DIR_SPRITE + 'Ship_White.png'],
    'img_boom_01'  : [26, 26, 0, DIR_SPRITE + 'Ship_explosion_0001.png'],
    'img_boom_02'  : [34, 32, 0, DIR_SPRITE + 'Ship_explosion_0002.png'],
    'img_boom_03'  : [36, 35, 0, DIR_SPRITE + 'Ship_explosion_0003.png'],
    'img_boom_04'  : [34, 32, 0, DIR_SPRITE + 'Ship_explosion_0004.png'],
    'img_bullet'   : [ 5, 10, 0, DIR_SPRITE + 'rocket_0001.png'],

    'img_bee'      : [15, 12, 180, DIR_SPRITE + 'Fly_0001.png'],
    'img_pheonix'  : [13, 13, 180, DIR_SPRITE + 'pheonix_0001.png'],
    'img_gremlin'  : [14, 14, 180, DIR_SPRITE + 'gremlin_0001.png'],
    'img_scorpion' : [13, 13, 180, DIR_SPRITE + 'scorpion_0001.png'],
    'img_catcher_g': [19, 18, 180, DIR_SPRITE + 'Green_Catcher.png'],
    'img_catcher_b': [19, 18, 180, DIR_SPRITE + 'catcher_blue.png'],
    'img_mosquito' : [15, 12, 180, DIR_SPRITE + 'mosquito_0002.png'],
    'img_airplane' : [17, 14, 180, DIR_SPRITE + 'airplane_0001.png'],
    'img_bam_01'   : [38, 38, 180, DIR_SPRITE + 'enemy_explosion_0001.png'],
    'img_bam_02'   : [38, 38, 180, DIR_SPRITE + 'enemy_explosion_0002.png'],
    'img_bam_03'   : [38, 38, 180, DIR_SPRITE + 'enemy_explosion_0003.png'],
    'img_bam_04'   : [38, 38, 180, DIR_SPRITE + 'enemy_explosion_0004.png'],

    'img_logo'     : [679, 312, 0, DIR_BIG + 'mobygames_logo.png'],
    'img_big_ship' : [200, 213, 0, DIR_BIG + 'galaga_fighter.png'],
    'img_big_pheo' : [240, 240, 0, DIR_BIG + 'galaga_pheo.png'],
    'img_enter'    : [240, 240, 0, DIR_BIG + 'galaga_enter.png'],
    }

# FIGHTER'S POSITION & MOVES
FIGHTER_WIDTH = IMGS['img_fighter'][0] * SCALE_SPRITE
FIGHTER_HEIGHT = IMGS['img_fighter'][1] * SCALE_SPRITE
POSX = int((SCREEN_SIZE[0] - FIGHTER_WIDTH) / 2)
POSY = int((SCREEN_SIZE[1] - (FIGHTER_HEIGHT + 20)))
(X_MOVE, Y_MOVE) = (0, 0)

# ENEMY'S POSITION & SPEED (INITIAL)
ENEMY_WIDTH = IMGS['img_fighter'][0] * SCALE_SPRITE
ENEMY_HEIGHT = IMGS['img_fighter'][1] * SCALE_SPRITE
ENEMY_SPEED = 5
ENEMY_X, ENEMY_Y = (0, int(SCREEN_SIZE[0]/2))

# SET SPRITES
for key in IMGS.keys():
    args = [int(IMGS[key][0] * SCALE_SPRITE),
            int(IMGS[key][1] * SCALE_SPRITE),
            IMGS[key][2], IMGS[key][3]]
    globals()[key] = set_sprite(*args)

# COLOR TABLE
BLACK = (0, 0, 0)           # BACK GROUND COLOR
RED = (255, 0, 0)           # FONT COLOR
WHITE = (255, 255, 255)     # FONT COLOR
