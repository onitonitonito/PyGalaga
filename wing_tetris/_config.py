"""------------------------------
# module.01 - variable setting : configuration
# location : ./_config.py
#
#\n\n\n"""
print(__doc__)


FPS = 25
SOURCE_DIR = '../resources/sound/'
WINDOWWIDTH = 640       # 640 x 480 px SCREEN WINDOW
WINDOWHEIGHT = 480

BOXSIZE = 20            # 1-unit box size = 20 x 20
BOARDWIDTH = 10         # width = 10 EA
BOARDHEIGHT = 20        # height = 20 EA

BLANK = '.'

MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.1

XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2) # Left & Right = 220 each
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5  # Top = 40

#               R       G       B
BLACK       = (   0,     0,   0)        #000000
WHITE       = ( 255,   255, 255)        #ffffff

DARKGRAY    = ( 90,    90,   90)        #5a5a5a
GRAY        = ( 185,   185, 185)        #b9b9b9

BRIGHTRED   = ( 255,   0,     0)        #ff0000
LIGHTRED    = ( 175,  20,    20)        #af1414
RED         = ( 155,   0,     0)        #9b0000

BRIGHTGREEN = ( 0,   255,     0)        #00ff00
LIGHTGREEN  = ( 20,  175,    20)        #14af14
GREEN       = ( 0,   155,     0)        #009b00

BRIGHTBLUE  = ( 0,      0,  255)        #0000ff
LIGHTBLUE   = (20,     20,  175)        #1414af
BLUE        = ( 0,      0,  155)        #00009b

BRIGHTYELLOW= ( 255,   255,   0)        #ffff00
LIGHTYELLOW = ( 175,   175,  20)        #afaf14
YELLOW      = ( 155,   155,   0)        #9b9b00

BORDERCOLOR = BLUE
BGCOLOR = BLACK

TEXTCOLOR = WHITE
TEXTSHADOWCOLOR = GREEN

COLORS      = (BLUE,           GREEN,      RED,      YELLOW,)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW,)

TEMPLATEWIDTH = 5       # Template = 5 x 5 dimension
TEMPLATEHEIGHT = 5

assert len(COLORS) == len(LIGHTCOLORS)      # each colors must have 1 lighter colors

S_SHAPE_TEMPLATE = [
                    ['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],

                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....'],
                     ]

Z_SHAPE_TEMPLATE = [
                    ['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],

                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....'],
                     ]

I_SHAPE_TEMPLATE = [
                    ['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],

                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....'],
                     ]

O_SHAPE_TEMPLATE = [
                    ['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....'],
                     ]

J_SHAPE_TEMPLATE = [
                    ['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],

                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],

                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],

                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....'],
                     ]

L_SHAPE_TEMPLATE = [
                    ['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],

                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],

                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],

                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....'],
                     ]

T_SHAPE_TEMPLATE = [
                    ['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],

                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],

                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],

                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....'],
                     ]

PIECES = {
          'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE,
          }



if __name__ == '__main__':
    pass
