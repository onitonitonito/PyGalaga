"""
# 히어로 클래스 (정의)
# 위치: asset/class_hero.py
#
#\n\n\n"""
print(__doc__)
import random
import pygame
from .config import *

class Hero(object):
    def __init__(self, filename, width, height, posx, posy):
        self.filename = filename
        self.width = width
        self.height = height
        self.posx = posx
        self.posy = posy
        self.x_move = 10
        self.y_move = 10


    def get_move(self,key):
        if key == 'up':
            self.posy -= self.y_move
            return self.posy
        elif key == 'down':
            self.posy += self.y_move
            return self.posy

        elif key == 'left':
            self.posx -= self.x_move
            return self.posx
        elif key == 'right':
            self.posx += self.x_move
            return self.posx
        return False

"""  CALCULATE """
# DISPLAYSURF is defined in py_galaga.py
def draw_socre(count):
    global DISPLAYSURF
    # font = pygame.font.SysFont(None, 20)
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("Enemy Kills: "+ str(count), True, WHITE)
    DISPLAYSURF.blit(text, (5, 5))

def draw_passed(count):
    global DISPLAYSURF
    # font = pygame.font.SysFont(None, 20)
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("Enemy Passed: "+ str(count), True, RED)
    DISPLAYSURF.blit(text, (310, 5))

def display_message(text, font_size=45, font_color=RED, delay_time=2):
    global DISPLAYSURF
    textfont = pygame.font.Font("freesansbold.ttf", font_size)
    text = textfont.render(text, True, font_color)
    text_pos = text.get_rect()
    text_pos.center = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
    DISPLAYSURF.blit(text, text_pos)
    pygame.display.update()
    time.sleep(delay_time)
    # run_game()

def crash_display():
    global DISPLAYSURF, lives_count
    lives_count -= 1
    display_message("...Crashed!!...", 45, RED, delay_time=2)

def game_over_display():
    global DISPLAYSURF
    display_message("GAME OVER", 55, WHITE, delay_time=8)
    pygame.quit()
    sys.exit()

def draw_object(obj, x, y):
    global DISPLAYSURF
    DISPLAYSURF.blit(obj, (x, y))

def get_reset_enemy():
    return random.randrange(0, SCREEN_SIZE[0] - ENEMY_WIDTH), 15
