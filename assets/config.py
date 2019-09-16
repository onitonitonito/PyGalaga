"""
# 초기 변수값 정의
# 위치: assets/config.py
#
#\n\n\n"""
print(__doc__)
import os

# WORKING DIR. SET
DIRNAME = "PyGalaga"
DIRS = os.path.dirname(__file__).partition(DIRNAME)
ROOT = "".join(DIRS[:2]) + '\\'

# FILE IMG /W DIR. --- BIG ICON for TEST
FILE_IMG_LOGO = ROOT + 'statics\\big\\mobygames_logo.png'
FILE_IMG_01 = ROOT + 'statics\\big\\galaga_fighter.png'
FILE_IMG_02 = ROOT + 'statics\\big\\galaga_pheo.png'
FILE_IMG_03 = ROOT + 'statics\\big\\galaga_enter.png'

# FILE IMG /W DIR. --- PRACTIAL SMALL ICON
FILE_IMG_FIGHTER = ROOT + 'statics\\sprite\\Ship_White.png'
FILE_IMG_BEE = ROOT + 'statics\\sprite\\Fly_0001.png'
FILE_IMG_BULLET = ROOT + 'statics\\sprite\\rocket_0001.png'
FILE_IMG_LIVES = ROOT + 'statics\\sprite\\Ship_White.png'

# COLOR TABLE
BLACK = (0, 0, 0)     # fill black
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# SET INITIAL VARI.
SCREEN_SIZE = (480, 640)            # screen size = 480 x 640 default
FPS = 30

# FIGHTER'S POSITION
POS_X = (480-50)/2
POS_Y = (640-(53+20))

FIGHTER_WIDTH = 36
FIGHTER_HEIGHT = 38

ENEMY_WIDTH = 36
ENEMY_HEIGHT = 38


# KEY INCREASEMENT
X_MOVE = 0
Y_MOVE = 0


# OBJECT DICTIONARY
DICT_OBJ = {            # SIZE x,y   POS x,y   file_name
    'g_catcher' : [36, 38, 200, 100,'Green_Catcher.png'],
    'gremlin'   : [36, 38, 200, 150,'gremlin_0001.png'],
    'bee'       : [36, 38, 200, 50,'Fly_0001.png'],
    'scorpion'  : [36, 38, 200, 250,'scorpion_0001.png'],
    'pheonix'   : [36, 38, 200, 300,'pheonix_0001.png'],
    'bullet'    : [13, 22, 200, 550,'rocket_0001.png'],
    'boom_01'   : [26, 26, 200, 200,'Ship_explosion_0001.png'],
    'boom_02'   : [26, 26, 200, 200,'Ship_explosion_0002.png'],
    'boom_03'   : [26, 26, 200, 200,'Ship_explosion_0003.png'],
    'boom_04'   : [26, 26, 200, 200,'Ship_explosion_0004.png'],
    }

# INSERT A NEW OBJ into DICTIONARY
DICT_OBJ['fighter'] = [
    FIGHTER_WIDTH,
    FIGHTER_HEIGHT,
    (SCREEN_SIZE[0] - FIGHTER_WIDTH)/2,
    SCREEN_SIZE[1] - (FIGHTER_HEIGHT + 10),
    'Ship_White.png']

DICT_OBJ['lives'] = [
    int(FIGHTER_WIDTH * 0.7),
    int(FIGHTER_HEIGHT * 0.7),
    (SCREEN_SIZE[0] - FIGHTER_WIDTH)/2,
    SCREEN_SIZE[1] - (FIGHTER_HEIGHT + 10),
    'Ship_White.png']
