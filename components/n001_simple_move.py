import sys
import pygame
import _parent_path                     # SET FOR ASSET

from asset.config import *
from asset.sprite import *

pygame.init()

FIGHTER = set_sprite(FILE_IMG_01, 50, 53)

DISPLAYSURF = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
pygame.display.set_caption('MOVE TEST SCREEN (%sx%s)' % (SCREEN_SIZE[0],SCREEN_SIZE[1]))
FPS_CLK = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X_MOVE = -5
            elif event.key == pygame.K_RIGHT:
                X_MOVE = +5
            elif event.key == pygame.K_UP:
                Y_MOVE = -5
            elif event.key == pygame.K_DOWN:
                Y_MOVE = +5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                X_MOVE = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                Y_MOVE = 0

        POS_X += X_MOVE
        POS_Y += Y_MOVE

        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(FIGHTER,(POS_X, POS_Y))

        pygame.display.update()
        FPS_CLK.tick(FPS)
