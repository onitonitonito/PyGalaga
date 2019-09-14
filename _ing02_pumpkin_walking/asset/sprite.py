"""------------------------------
# module.02 - class MySprite(pygame.sprite.Sprite)
# location : ./asset/_class.py
#
#
"""
print(__doc__)

import pygame



class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        """ make image array & make rect """
        super(MySprite, self).__init__()
        # adding all the images to sprite array

        self.images = []
        for i in range(10):
            self.images.append(pygame.image.load(
                    f"./static/img/walk_{i+1:02d}.png"
                )
            )

        self.index = 0
        self.image = pygame.transform.smoothscale(
                            self.images[self.index], (600, 400))

        self.rect = self.image.get_rect()
        self.rect.topleft = (0,200)


        # self.rect = pygame.Rect(
        #         50,            # left=50,
        #         100,           # top=100,
        #         80,            # width=150,
        #         90,            # height=198,
        #     )


    def update(self):
        """ image update when it is called """
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]


if __name__ == '__main__':

    from pygame.locals import *

    pygame.init()
    screen = pygame.display.set_mode((400,600))

    array_key_strokes = [
        (KEYUP and K_ESCAPE),
        (KEYUP and K_SPACE),
        (KEYUP and K_w),
        (KEYUP and K_a),
        (KEYUP and K_s),
        (KEYUP and K_d),
    ]

    while True:
        for event in pygame.event.get(KEYUP):
            print(event)
            if event in array_key_strokes:
                pygame.quit()
                sys.exit()


        pygame.display.update()
