import os

# WORKING DIR. SET
DIRNAME = "PyGalaga"
DIRS = os.path.dirname(__file__).partition(DIRNAME)
ROOT = DIRS[0] + DIRS[1] + '\\'

# FILE IMG /W DIR.
FILE_IMG_LOGO = ROOT + 'resources/big/mobygames_logo.png'
FILE_IMG_01 = ROOT + 'resources/big/galaga_fighter.png'
FILE_IMG_02 = ROOT + 'resources/big/galaga_pheo.png'
FILE_IMG_03 = ROOT + 'resources/big/galaga_enter.png'

# SET INITIAL VARI.
SCREEN_SIZE = (480, 640)            # screen size = 480 x 640 default
BLACK = (0,0,0)     # fill black
FPS = 30

# FIGHTER'S POSITION
POS_X = (480-50)/2
POS_Y = (640-(53+20))

# KEY INCREASEMENT
X_MOVE = 0
Y_MOVE = 0
