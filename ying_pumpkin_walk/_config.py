"""------------------------------
# module.01 - variable setting : configuration
# location : ./_config.py
#
#\n\n\n"""
print(__doc__)

import pygame

SIZE = WIDTH, HEIGHT = 600, 400
BACKGROUND_COLOR = pygame.Color('darkgray')
FPS = 10                # Frames per second

# getting the pygame clock for handling fps
CLOCK = pygame.time.Clock()
