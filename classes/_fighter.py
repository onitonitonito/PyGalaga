import _parent_path                     # SET FOR assets
from assets.config import *
from assets.sprite import *


FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption(
    'TEST SCREEN [%sx%s]' % (SCREEN_SIZE[0], SCREEN_SIZE[1]))

# FIGHTER = pygame.image.load(FILE_IMG_04)
LOGO = set_sprite(FILE_IMG_LOGO, 350, 155)
FIGHTER = set_sprite(FILE_IMG_01, 53, 55)

# MAIN ROUTINE
while True:
    DISPLAYSURF.blit(LOGO, (SCREEN_SIZE[0] * 0.13, SCREEN_SIZE[1] * 0.2))
    DISPLAYSURF.blit(FIGHTER, (SCREEN_SIZE[0] * 0.4, SCREEN_SIZE[1] * 0.7))
    pygame.display.update()
    FPSCLOCK.tick(FPS)
