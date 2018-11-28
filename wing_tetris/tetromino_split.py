"""------------------------------
# main.00 - excute file
# location : ./tetrimono.py
#
#\n\n\n"""
print(__doc__)

import sys
import time
import random
import pygame

from _config import *
from pygame.locals import K_p, K_q, K_SPACE
from pygame.locals import K_w, K_a, K_s, K_d
from pygame.locals import K_UP, K_LEFT, K_DOWN, K_RIGHT
from pygame.locals import QUIT, KEYUP, KEYDOWN, K_ESCAPE



def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT

    pygame.init()

    FPSCLOCK    = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT   = pygame.font.Font('freesansbold.ttf', 25)
    BIGFONT     = pygame.font.Font('freesansbold.ttf', 85)
    pygame.display.set_caption('TETRO + DOMINO = TETROMINO!')

    showTextScreen('TETROMINO')

    while True:
        if random.randint(0, 1) == 0:
            pygame.mixer.music.load(SOURCE_DIR + 'tetrisb.mid')
        else:
            pygame.mixer.music.load(SOURCE_DIR + 'tetrisc.mid')

        pygame.mixer.music.play(-1, 0.0)
        runGame()

        time.sleep(5)

def runGame():
    # initial set-up when it get started
    board = getBlankBoard()             # Reset Blank board

    lastMoveDownTime = time.time()      # reset time
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()

    movingDown  = False                  # reset move = NO move
    movingLeft  = False
    movingRight = False

    score = 0                           # reset score

    level, fallFreq = calculateLevelAndFallFreq(score)  # depend on score

    fallingPiece    = getNewPiece()
    nextPiece       = getNewPiece()

    while True:
        if fallingPiece == None:
            # get New PIECES
            fallingPiece    = nextPiece
            nextPiece       = getNewPiece()
            lastFallTime    = time.time()   # reset lastFallTime AGAIN~!!

            if not isValidPosition(board, fallingPiece):
                return      # Not able to set New PIECES = GAME OVER.

        checkForQuit()

        for event in pygame.event.get():
            if event.type == KEYUP:             # Release - EVENT LOOP
                if (event.key == K_p):              # p-key is released
                    # PAUSE MODE = PRESS 'P'
                    DISPLAYSURF.fill(BGCOLOR)
                    pygame.mixer.music.stop()
                    showTextScreen('Paused')

                    pygame.mixer.music.play(-1, 0.0)

                    lastFallTime            = time.time()
                    lastMoveDownTime        = time.time()
                    lastMoveSidewaysTime    = time.time()

                elif (event.key == K_LEFT or event.key == K_a ):
                    movingLeft = False          # LEFT-key is released = STOP!

                elif (event.key == K_RIGHT or event.key == K_d):
                    movingRight = False         # RIGHT-key is released = STOP!

                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = False          # DOWN-key is released = STOP!

            elif event.type == KEYDOWN:     # Press-EVENT LOOP .. inc'l WASD-key

                if (event.key == K_LEFT or event.key == K_a )\
                and isValidPosition(board, fallingPiece, adjX = -1):
                    fallingPiece['x'] -=1
                    movingLeft = True
                    movingRight = False
                    lastMoveSidewaysTime = time.time()

                elif (event.key == K_RIGHT or event.key == K_d)\
                and isValidPosition(board, fallingPiece, adjX = +1):
                    fallingPiece['x'] +=1
                    movingLeft = False
                    movingRight = True
                    lastMoveSidewaysTime = time.time()

                # IF have Room to rotate, Do rotate , USING Q-W Key
                elif (event.key == K_UP or event.key == K_w):
                    fallingPiece['rotation'] = (fallingPiece['rotation']+1)%len(PIECES[fallingPiece['shape']])

                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation']-1)%len(PIECES[fallingPiece['shape']])

                elif (event.key == K_q):    # reverse rotation
                    fallingPiece['rotation'] = (fallingPiece['rotation']-1)%len(PIECES[fallingPiece['shape']])

                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation']+1)%len(PIECES[fallingPiece['shape']])

                # If DOWN-KEY or s = fast DOWN mode
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = True

                    if isValidPosition(board, fallingPiece, adjY = +1):
                        fallingPiece['y'] +=1

                    lastMoveDownTime = time.time()

                # If SPACE = DROP at the position
                elif event.key == K_SPACE:
                    movingDown  = False
                    movingLeft  = False
                    movingRight = False
                    for i in range(1, BOARDHEIGHT):
                        if not isValidPosition(board, fallingPiece, adjY = +i):
                            break
                    fallingPiece['y'] += i - 1

        # Moving Piece LEFT-RIGHT, according to User's KEY-IN
        if (movingLeft or movingRight)\
        and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:

            if movingLeft and isValidPosition(board, fallingPiece, adjX = -1):
                fallingPiece['x'] -= 1

            elif movingRight and isValidPosition(board, fallingPiece, adjX = +1):
                fallingPiece['x'] += 1

            lastMoveSidewaysTime = time.time()

        # Moving Down as time goes by
        if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ\
        and isValidPosition(board, fallingPiece, adjY = +1):

            fallingPiece['y'] += 1
            lastMoveSidewaysTime = time.time()

        # If time-out = Drop Piece
        if time.time() - lastFallTime > fallFreq:
            # check If Piece touch the surface(or ground)
            if not isValidPosition(board, fallingPiece, adjY = +1):
                # If Piece touch, Remaim as it is.
                addToBoard(board, fallingPiece)
                score += removeCompleteLines(board)

                level, fallFreq = calculateLevelAndFallFreq(score)
                fallingPiece = None

            else:
                # If Piece doesn't touch, Move DOWN
                fallingPiece['y'] += 1
                lastFallTime = time.time()

        # DRAW ALL on the SCREEN
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(board)
        drawStatus(score, level)
        drawNextPiece(nextPiece)

        if fallingPiece != None:
            drawPiece(fallingPiece)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def makeTextObjects(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()

def terminate():
    pygame.quit()
    sys.exit()

def checkForPress():
    # check for KEYUP event searching in Event_Que
    # check for KEYDOWN event and eliminate Event_Que
    checkForQuit()

    for event in pygame.event.get( [KEYUP,KEYDOWN,] ):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None

def showTextScreen(text):
    # SHADOW EFFECT on Title
    titleSurf, titleRect = makeTextObjects(text, BIGFONT, TEXTSHADOWCOLOR)
    titleRect.center = ( int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) )
    DISPLAYSURF.blit(titleSurf, titleRect)

    # Draw Title TEXT on the SHADOW
    titleSurf, titleRect = makeTextObjects(text, BIGFONT, TEXTCOLOR)
    titleRect.center = ( int(WINDOWWIDTH / 2) - 5, int(WINDOWHEIGHT / 2) - 5 )
    DISPLAYSURF.blit(titleSurf, titleRect)

    #'PRESS KEY TO PLAY' TEXT
    MESSAGE = 'Press a Key to Play!...'
    pressKeySurf, pressKeyRect = makeTextObjects(MESSAGE,BASICFONT,TEXTCOLOR)
    pressKeyRect.center = ( int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100 )
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    while checkForPress() == None:      # DO Loop while No-KEYUP & DOWN EVENT
        pygame.display.update()
        FPSCLOCK.tick()

def checkForQuit():
    for event in pygame.event.get( QUIT ):
        terminate()

    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)    # return KEY-UP event OBJECT to Event_Que

def calculateLevelAndFallFreq(score):
    level = int(score / 10) + 1
    fallFreq = 0.27 - (level * 0.02)
    return level, fallFreq

def getNewPiece():
    # return Randomly get random colored Piece
    shape = random.choice(list(PIECES.keys(), ))    # KEY of PIECES_DICT (Z,L,O,S...)

    newPiece = {
        'shape'     : shape,
        'rotation'  : random.randint(0, len(PIECES[shape]) - 1 ),    # SET = Start shape
        'x'         : int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
        'y'         : -2,    # Top of the BOARD Y-position
        'color'     :  random.randint(0, len(COLORS)-1),
    }
    return newPiece

def addToBoard(board, piece):
    # fill up board, according to position, shape, rotation
    for x in range(TEMPLATEWIDTH):                      # TEMPLATEWIDTH = 5
        for y in range(TEMPLATEHEIGHT):                 # TEMPLATEHEIGHT = 5
            if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']

def getBlankBoard():
    # RESET blank board
    # Retern 20 x 10 array filled with '.'
    # board = [ '.........','........','........',..]
    board = []                      # Array of vertical sections
    for i in range(BOARDWIDTH):                 # BOARDWIDTH    = 10
        board.append([BLANK] * BOARDHEIGHT )    # BOARDHEIGHT   = 20

    return board

def isOnBoard(x, y):
    return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT

def isValidPosition(board, piece, adjX=0, adjY=0):
    # If Piece isn't crushed, and on-board, Retern True
    for x in range(TEMPLATEWIDTH):          # TEMPLATEWIDTH = 5
        for y in range(TEMPLATEHEIGHT):     # TEMPLATEHEIGHT = 5
            isAboveBoard = y + piece['y'] + adjY < 0

            if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue

            if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                return False

            if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                return False
    return True

def isCompleteLine(board, y):
    # return True, when there's no blank on the line
    for x in range(BOARDWIDTH):  # BOARDWIDTH = 10
        if board[x][y] == BLANK:
            return False
    return True

def removeCompleteLines(board):
    # remove complete line and return how many lines are completed, under upper line.
    numLinesRemoved = 0
    y = BOARDHEIGHT - 1         # BOARDHEIGHT = 20, start from far bottom line
    while y >= 0:
        if isCompleteLine(board, y):

            # eliminate 1 line and move down 1 line
            for pullDownY in range(y, 0, -1):
                for x in range(BOARDWIDTH):
                    board[x][pullDownY] = board[x][pullDownY-1]

            # Set Top line as Blank after moving all.
            for x in range(BOARDWIDTH):
                board[x][0] = BLANK

            numLinesRemoved += 1
        else:
            y -= 1
    return numLinesRemoved

def convertToPixelCoords(boxx, boxy):
    # change real coords x, y --> LC_coords x,y
    return (XMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))

def drawBox(boxx, boxy, color, pixelx=None, pixely=None):
    # draw 1 box at LC-Coords system (1 block consists of 4 Boxes)
    if color == BLANK:
        return

    if pixelx == None and pixely == None:
        pixelx, pixely = convertToPixelCoords(boxx, boxy)

    pygame.draw.rect(DISPLAYSURF, COLORS[color],        (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1,))
    pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS[color],   (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4,))

def drawBoard(board):
    # draw border around board
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (XMARGIN - 3, TOPMARGIN - 7,
        (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)

    # fill bgColor
    pygame.draw.rect(DISPLAYSURF, BGCOLOR, (XMARGIN, TOPMARGIN, BOXSIZE*BOARDWIDTH, BOXSIZE*BOARDHEIGHT))

    # Draw board BOX
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            drawBox(x, y, board[x][y], )

def drawStatus(score, level):
    # Draw score TEXT
    scoreSurf = BASICFONT.render('SCORE: %s'%score, True, TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()    # Auto rect
    scoreRect.topleft = (WINDOWWIDTH - 150, 20)     # WINDOWWIDTH = 640
    DISPLAYSURF.blit(scoreSurf, scoreRect)

    # Draw level TEXT
    levelSurf = BASICFONT.render('LEVEL: %s'%level, True, TEXTCOLOR)
    levelRect = levelSurf.get_rect()    # Auto rect
    levelRect.topleft = (WINDOWWIDTH - 610, 20)     # WINDOWWIDTH = 640
    DISPLAYSURF.blit(levelSurf, levelRect)

def drawPiece(piece, pixelx=None, pixely=None):
    shapeToDraw = PIECES[piece['shape']][piece['rotation']]
    if pixelx == None and pixely == None:
        # If x,y are not assigned, refer own Piece data
        pixelx,pixely = convertToPixelCoords(piece['x'], piece['y'])

    # draw each of the boxes that make up the piece
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if shapeToDraw[y][x] != BLANK:
                drawBox(None, None, piece['color'],
                    pixelx + ( x * BOXSIZE ),
                    pixely + ( y * BOXSIZE ), )

def drawNextPiece(piece):
    # draw 'NEXT' piece
    nextSurf = BASICFONT.render('NEXT:', True, TEXTCOLOR)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = ( WINDOWWIDTH - 120, 130 )

    DISPLAYSURF.blit(nextSurf, nextRect)

    drawPiece(piece, pixelx=WINDOWWIDTH-120, pixely=150, )


if __name__ == '__main__':
    main()

# Pygame.org : TETROMINO = http://www.pygame.org/project-Tetromino+(Tetris+clone)-1852-.html
