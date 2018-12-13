"""------------------------------
# MAIN -
# location : pumpkin_walk.py
# ----------------
# PyGame Sprite Animation Tutorial – Simple Walk Loop
# June 8, 2018 by Belal Khan Leave a Comment
# https://www.simplifiedpython.net/pygame-sprite-animation-tutorial/
# ?fbclid=IwAR24REc-FAR72Ymh-JPq037rdIXZKGsavVLwyDG-U5Kf8VNk0NQOmhgtUrs
#
#\n\n\n"""
print(__doc__)


import pygame

from _config import *
from _class import MySprite


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    # creating a group with our sprite
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        """
        # https://stackoverflow.com/questions/44983710/python-event-has-not-key-attribute
        # I think the problem is if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH -1: is outside of the forloop so the event doesn't have a key attribute.
        # the event inside the forloop has a key attribute because of pygame.event.get(): move that line inside of the forloop and that should solve your problem.
        """
        # event have to be in for-loop! -- I changed.
        # if user wants to quit
        # if event.type == pygame.locals.QUIT:
        # if event.type == QUIT:
        """
        event = pygame.event.get()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        """

        # updating the sprite
        my_group.update()

        # filling the screen with background color
        screen.fill(BACKGROUND_COLOR)

        # drawing the sprite
        my_group.draw(screen)

        # updating the display
        pygame.display.update()

        # finally delaying the loop to with clock tick for 10fps
        CLOCK.tick(10)

# [in.04] The final Code


if __name__ == '__main__':
    main()
