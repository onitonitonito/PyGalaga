"""
# 메인 앱 - 실행
# 위치: root
"""
import sys
import time
import random
import pygame

from pygame.locals import *         # 키값
from assets.config import *

# from assets.class_hero import Hero

print(__doc__)


"""  CALCULATE """
# DISPLAYSURF is defined in py_galaga.py
def draw_socre(count):
    # font = pygame.font.SysFont(None, 20)
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("Enemy Kills: "+ str(count), True, WHITE)
    DISPLAYSURF.blit(text, (5, 5))

def draw_passed(count):
    # font = pygame.font.SysFont(None, 20)
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("Enemy Passed: "+ str(count), True, RED)
    DISPLAYSURF.blit(text, (310, 5))

def display_message(text, font_size=45, font_color=RED, delay_time=2):
    textfont = pygame.font.Font("freesansbold.ttf", font_size)
    text = textfont.render(text, True, font_color)
    text_pos = text.get_rect()
    text_pos.center = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
    DISPLAYSURF.blit(text, text_pos)
    pygame.display.update()
    time.sleep(delay_time)

def crash_display():
    global lives_count
    lives_count -= 1
    display_message("...Crashed!!...", 45, RED, delay_time=2)

def game_over_display():
    print(f"You have killed {count} enemies!")
    display_message("GAME OVER", 55, WHITE, delay_time=8)

    pygame.quit()
    sys.exit()

def draw_object(obj, x, y):
    DISPLAYSURF.blit(obj, (x, y))

def get_reset_enemy():
    return random.randrange(0, SCREEN_SIZE[0] - ENEMY_WIDTH * 2), 15

def get_enemy_img():
    img_enemies = [img_bee, img_pheonix, img_gremlin, img_scorpion]
    return img_enemies[random.randint(0, 3)]


if __name__ == '__main__':
    img_enemy = get_enemy_img()
    ENEMY_X, ENEMY_Y = (0, int(SCREEN_SIZE[0]/2))

    pygame.init()

    DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('My GALAGA!!')
    FPS_CLK = pygame.time.Clock()   # FPS_CLK.tick(FPS)

    is_hit = False
    lives_count = 3
    shot_count = 0
    enemy_passed = 0

    bullet_xy = []

    x = SCREEN_SIZE[0] * 0.45                     # 45% start fighter X-point
    y = SCREEN_SIZE[1] - (FIGHTER_HEIGHT * 1.7)   # 95% start fighter Y-point

    x_change = 0                             # not moving
    y_change = 0

    ongame = True

    while ongame:
        """
        # 이벤트 키값에 대응하는 event_dict 인덱스값=0,1,2,3,4 를 반환.
        # print(event.type)   # for test ... 2-KeyDown / 3-KeyUp
        # print(event)        # for test ... event object
        """
        for event in pygame.event.get():
            event_dict = {
                'quit' : [(event.type == QUIT),
                         (event.type == KEYDOWN and event.key == K_ESCAPE), ],

                'up'   : [(event.type == KEYDOWN and event.key == K_UP), ],
                'down' : [(event.type == KEYDOWN and event.key == K_DOWN), ],
                'left' : [(event.type == KEYDOWN and event.key == K_LEFT), ],
                'right': [(event.type == KEYDOWN and event.key == K_RIGHT), ],

                'shoot': [(event.type == KEYDOWN and event.key == K_LCTRL), ],

                'x_stop': [(event.type == KEYUP and event.key == K_LEFT),
                           (event.type == KEYUP and event.key == K_RIGHT),],

                'y_stop': [(event.type == KEYUP and event.key == K_UP),
                           (event.type == KEYUP and event.key == K_DOWN),],
            }

            # show key-event on console
            """# IF - Keybinding State = down-stroke"""
            for key in event_dict.keys():

                if True in [*event_dict[key]]:
                    print(f'----[{key.upper()}]----')

                    if key == 'quit':
                        ongame = False

                    if key == 'shoot':
                        if len(bullet_xy) < 3:
                            BULL_X = int(x + FIGHTER_WIDTH/2)
                            BULL_Y = int(y - FIGHTER_HEIGHT)
                            bullet_xy.append([BULL_X, BULL_Y])

                    if key == 'up':
                        y_change = -5

                    elif key == 'down':
                        y_change = +5

                    elif key == 'left':
                        x_change = -5

                    elif key == 'right':
                        x_change = +5


            """# IF - Keybinding State = up-stroke"""
            for key in event_dict.keys():
                if True in [*event_dict[key]]:
                    if key == 'x_stop':
                        x_change = 0

                    if key == 'y_stop':
                        y_change = 0



        """ # IF - Cross the Limit (X,Y) = stop there! """
        if x < 0:
            x = 0
        elif x > SCREEN_SIZE[0] - FIGHTER_WIDTH:
            x = SCREEN_SIZE[0] - FIGHTER_WIDTH

        if y < 0:
            y = 0
        elif y > SCREEN_SIZE[1] - FIGHTER_HEIGHT * 1.7:
            y = SCREEN_SIZE[1] - FIGHTER_HEIGHT * 1.7

        if ENEMY_X < 0:
            ENEMY_X = 0
        elif ENEMY_X > SCREEN_SIZE[0] - ENEMY_WIDTH:
            ENEMY_X = SCREEN_SIZE[0] - ENEMY_WIDTH


        if ENEMY_Y > (SCREEN_SIZE[1] - FIGHTER_HEIGHT * 1.7):
            img_enemy = get_enemy_img()
            ENEMY_X, ENEMY_Y = get_reset_enemy()


        """ IF CRASHED .. (!) TODO: HAVE TO BE MODIFIED (!) """
        if y < ENEMY_Y + ENEMY_HEIGHT:
            if(ENEMY_X > x and ENEMY_X < x + FIGHTER_WIDTH) or\
                (ENEMY_X +ENEMY_WIDTH > x and ENEMY_X +
                ENEMY_WIDTH < x + FIGHTER_WIDTH):
                    if lives_count < 1:
                        game_over_display()
                    crash_display()
                    ENEMY_X, ENEMY_Y = get_reset_enemy()
                    img_enemy = get_enemy_img()


        """ IF ENEMY IS SHOT """
        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[1] -= 10
                bullet_xy[i][1] = bxy[1]


                """ IF SHOT HITS THE ENEMY """
                if bxy[1] < ENEMY_Y:
                    if bxy[0] > ENEMY_X and bxy[0] < ENEMY_X + ENEMY_WIDTH:
                        bullet_xy.remove(bxy)
                        is_hit = True
                        shot_count += 1
                        img_enemy = get_enemy_img()


                if bxy[1] <= 0:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass

        # [POS] Give Fight a move
        x += x_change
        y += y_change

        # [POS] Give ENEMY a BUMBLE(togo) move
        togo = random.randint(0,12)
        if togo % 3 == 0:
            for n in range(random.randint(0,20)):
                ENEMY_X += 1
        elif togo % 3 == 1:
            for n in range(random.randint(0,20)):
                ENEMY_X += 0
        elif togo % 3 == 2:
            for n in range(random.randint(0,20)):
                ENEMY_X -= 1

        ENEMY_Y += ENEMY_SPEED
        # print(ENEMY_Y)

        if ENEMY_Y > SCREEN_SIZE[1] - (FIGHTER_HEIGHT + 30):
            enemy_passed += 1
            ENEMY_Y = 0
            print(enemy_passed)

        if enemy_passed >= 3:
            game_over_display()

        """ IS SHOOT? = SPEED++ """
        if is_hit:
            ENEMY_SPEED += 1

            if ENEMY_SPEED >= 20:
                ENEMY_SPEED = 20

            ENEMY_X, ENEMY_Y = get_reset_enemy()
            img_enemy = get_enemy_img()

            is_hit = False

        DISPLAYSURF.fill(BLACK)
        draw_passed(enemy_passed)
        draw_socre(shot_count)

        for n in range(1, lives_count):
            draw_object(
                img_lives,
                SCREEN_SIZE[0] - (FIGHTER_WIDTH * 0.5 * n) - 10,
                SCREEN_SIZE[1] - FIGHTER_HEIGHT)

        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                draw_object(img_bullet, bx, by)

        draw_object(img_fighter, x, y)
        draw_object(img_enemy, ENEMY_X, ENEMY_Y)

        pygame.display.update()
        FPS_CLK.tick(FPS)

    pygame.quit()
    sys.exit()
