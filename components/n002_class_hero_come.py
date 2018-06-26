
import pygame
import _parent_path                     # SET FOR ASSET

from asset.config import *
from asset.sprite import *
from asset.class_hero import *


fpsClock = pygame.time.Clock()

pygame.init()

DISPLAYSURF = pygame.display.set_mode((480, 640), 0, 32)
pygame.display.set_caption('Animation')

fighter = Hero(FILE_IMG_01, 40, 45, 200, 500)       #create a Hero
ship = set_sprite(FILE_IMG_01, 40, 45, 0)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = fighter.get_move('left')
                print("x=", x)
            elif event.key == pygame.K_RIGHT:
                x = fighter.get_move('right')
                print("x=", x)
            elif event.key == pygame.K_UP:
                y = fighter.get_move('up')
                print("y=", y)
            elif event.key == pygame.K_DOWN:
                y = fighter.get_move('down')
                print("y=", y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or\
            event.key == pygame.K_UP   or event.key == pygame.K_DOWN :
                pass

    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(ship, (fighter.posx, fighter.posy))    # draw object

    pygame.display.update()
    fpsClock.tick(FPS)
