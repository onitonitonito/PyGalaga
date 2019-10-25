"""
# assets/sprite.py - 기본 스프라이트를 처리하기 위한 함수들
"""
print(__doc__)
import pygame


# DEFINE FUNCTION : 3 HELPERS to 1 COMBINE
def set_load(filename):
    """HELPER() to set_sprite()"""
    return pygame.image.load(filename)


def set_size(obj, width, height):
    """HELPER() to set_sprite()"""
    return pygame.transform.scale(obj, (width, height))


def set_rotate(obj, angle):
    """HELPER() to set_sprite()"""
    return pygame.transform.rotate(obj, angle)


def set_sprite(width, height, angle, filename):
    """# GETHER ALL ABOVES: load, size, rotate"""
    sprite = set_load(filename)

    if (width * height) is not 0:
        sprite = set_size(sprite, width, height)

    if angle is not 0:
        sprite = set_rotate(sprite, angle)

    return sprite
