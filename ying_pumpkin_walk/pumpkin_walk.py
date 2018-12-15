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

    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(BACKGROUND_COLOR)
        my_group.update()
        my_group.draw(screen)

        # for test
        for sprite in my_group:
            print(sprite, sprite.image)


        pygame.display.update()

        # final delaying
        CLOCK.tick(10)


if __name__ == '__main__':
    print(SIZE)
    main()
    pass
