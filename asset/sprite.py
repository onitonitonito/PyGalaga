import pygame


# DEFINE FUNCTION : 3 HELPERS to 1 COMBINE
def set_load(filename):
    return pygame.image.load(filename)


def set_size(obj, width, height):
    return pygame.transform.scale(obj, (width, height))


def set_rotate(obj, angle):
    return pygame.transform.rotate(obj, angle)


# GETHER ABOVES
def set_sprite(filename, width=0, height=0, angle=0):
    sprite = set_load(filename)

    if (width * height) is not 0:
        sprite = set_size(sprite, width, height)

    if angle is not 0:
        sprite = set_rotate(sprite, angle)

    return sprite
