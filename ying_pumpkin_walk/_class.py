"""------------------------------
# module.02 - class MySprite(pygame.sprite.Sprite)
# location : ./_class.py
#
#\n\n\n"""
print(__doc__)

import pygame



class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        # adding all the images to sprite array

        self.images = []
        for i in range(1, 11, 1):
            self.images.append(pygame.image.load(
                    "./sources/walk_{:02d}.png".format(i)
                )
            )

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(50, 100, 150, 198)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
