"""------------------------------
# MAIN -
# location : pumpkin_walk.py
# ----------------
# PyGame Sprite Animation Tutorial – Simple Walk Loop
# June 8, 2018 by Belal Khan Leave a Comment
#
# https://www.simplifiedpython.net/pygame-sprite-animation-tutorial/
# ?fbclid=IwAR24REc-FAR72Ymh-JPq037rdIXZKGsavVLwyDG-U5Kf8VNk0NQOmhgtUrs
#
"""
# print(__doc__)

import sys
import pygame

from pygame.locals import *
from asset.config import *
from asset.sprite import MySprite


pygame.init()


def main():
    """
    # for test
    # <MySprite sprite(in 1 groups)> <Surface(150x198x32 SW)>
    # for sprite in my_group:
    #     print(sprite, sprite.image)
    """
    screen = pygame.display.set_mode(WINDOW_SIZE)

    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)

    while True:
        key_check_exit()

        screen.fill(BACKGROUND_COLOR)
        my_group.update()
        my_group.draw(screen)

        pygame.display.update()
        CLOCK.tick(FPS)


def key_check_exit():
    for event in pygame.event.get():
        # print(event.type)   # for test
        # print(event)

        event_dict = {
            'quit': [
                    (event.type == QUIT),
                    (event.type == KEYUP and event.key == K_ESCAPE), ],
            'move_up': [(event.type == KEYUP and event.key == K_UP), ],
            'move_down': [(event.type == KEYUP and event.key == K_DOWN), ],
            'move_left': [(event.type == KEYUP and event.key == K_LEFT), ],
            'move_right': [(event.type == KEYUP and event.key == K_RIGHT), ],
        }

        movings = event_dict.keys()

        # elif True in [*event_dict['move_up']]:
        #     print("----MOVE_UP!----")
        #
        # elif True in [*event_dict['move_down']]:
        #     print("----MOVE_DOWN!----")
        #
        # elif True in [*event_dict['move_left']]:
        #     print("----MOVE_LEFT!----")
        #
        # elif True in [*event_dict['move_right']]:
        #     print("----MOVE_RIGHT!----")

        # show key-event on console
        for move in movings:
            if True in [*event_dict[move]]:
                print(f'----{move.upper()}!----')

        if True in [*event_dict['quit']]:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    print(WINDOW_SIZE)

    main()
    pass
