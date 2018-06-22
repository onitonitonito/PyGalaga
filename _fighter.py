from asset.config import *
from asset.sprite import *


FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption(
    'TEST SCREEN [%sx%s]' % (SCREEN_SIZE[0], SCREEN_SIZE[1]))

# FIGHTER = pygame.image.load(FILE_IMG_04)
FIGHTER = set_sprite(FILE_IMG_01, 50, 55)

# MAIN ROUTINE
while True:
    DISPLAYSURF.blit(FIGHTER, (SCREEN_SIZE[0] * 0.5, SCREEN_SIZE[1] * 0.7))
    pygame.display.update()
    FPSCLOCK.tick(FPS)
