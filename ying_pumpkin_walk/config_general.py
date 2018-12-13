"""
General Configuration in PyGame
screen size, working dir, color, etc
"""

import os
import sys

HOME = "PyGalaga"        # repository ROOT
DIRS = os.path.dirname(__file__).partition(HOME)
ROOT = DIRS[0] + DIRS[1] + "\\"


#               R       G       B
BLACK       = (   0,     0,   0)    #000000
WHITE       = ( 255,   255, 255)    #ffffff

DARKGRAY    = ( 90,    90,   90)    #5a5a5a
GRAY        = ( 185,   185, 185)    #b9b9b9

BRIGHTRED   = ( 255,   0,     0)    #ff0000
LIGHTRED    = ( 175,  20,    20)    #af1414
RED         = ( 155,   0,     0)    #9b0000

BRIGHTGREEN = ( 0,   255,     0)    #00ff00
LIGHTGREEN  = ( 20,  175,    20)    #14af14
GREEN       = ( 0,   155,     0)    #009b00

BRIGHTBLUE  = ( 0,      0,  255)    #0000ff
LIGHTBLUE   = (20,     20,  175)    #1414af
BLUE        = ( 0,      0,  155)    #00009b

BRIGHTYELLOW= ( 255,   255,   0)    #ffff00
LIGHTYELLOW = ( 175,   175,  20)    #afaf14
YELLOW      = ( 155,   155,   0)    #9b9b00
