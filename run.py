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

""" VARIABLES """
bullet_xy = []
is_hit = False
lives_count = 3
(shot_count, shot_count_limit) = (0, 3)
(enemy_passed, enemy_pass_limit) = (0, 3)

"""  CALCULATE : DISPLAYSURF is defined in main()"""
def display_message(text, size, posxy, font_color, delay_time=0):
    """HELPER(): for display_*() """
    textfont = pygame.font.Font("freesansbold.ttf", size)
    text = textfont.render(text, True, font_color)

    if posxy == (0, 0): # center
        text_pos = text.get_rect()
        text_pos.center = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
    else:               # other position (x,y)
        text_pos = posxy

    DISPLAYSURF.blit(text, text_pos)

    if delay_time:
        pygame.display.update()
        time.sleep(delay_time)

def display_socre(count):
    display_message(f"Enemy Kills: {str(count)}", 20, (5,5), WHITE)

def display_passed(count):
    display_message(f"Enemy Passed: {str(count)}", 20, (310,5), RED)

def display_crash():
    global lives_count
    lives_count -= 1
    display_message("...Crashed!!...", 45, (0,0), RED, delay_time=2)

def display_gameover():
    display_message("GAME OVER", 55, (0, 0), WHITE, delay_time=5)
    print(f"You have killed {shot_count} enemies!")
    pygame.quit()
    sys.exit()

def get_reset_enemy():
    return random.randrange(0, SCREEN_SIZE[0] - ENEMY_WIDTH * 2), 15

def get_enemy_img():
    """randomly select enemy's sprite object"""
    img_enemies = [
        img_bee,
        img_pheonix,
        img_gremlin,
        img_scorpion,
        img_catcher_g,
        img_catcher_b,
        img_mosquito,
        img_airplane,
        ]
    return img_enemies[random.randint(0, len(img_enemies))-1]

def set_screen(caption="CAPTION HERE"):
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(caption)


if __name__ == '__main__':
    img_enemy = get_enemy_img()

    pygame.init()
    set_screen('My GALAGA!!')

    ongame = True

    while ongame:
        """이벤트 키값에 대응하는 event_dict로 키 이벤트 입력 판단"""
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
            """# IF - Keybinding State = keydown-stroke"""
            for key in event_dict.keys():

                if True in [*event_dict[key]]:    # 키-이벤트가 발생판단
                    # print(f'----[{key.upper()}]----')  # for TEST

                    if key == 'quit':
                        ongame = False

                    if key == 'shoot':
                        if len(bullet_xy) < 3:
                            BULL_X = int(POSX + FIGHTER_WIDTH/2)
                            BULL_Y = int(POSY - FIGHTER_HEIGHT)
                            bullet_xy.append([BULL_X, BULL_Y])

                    if key == 'up':
                        Y_MOVE = -5

                    elif key == 'down':
                        Y_MOVE = +5

                    if key == 'left':
                        X_MOVE = -5

                    elif key == 'right':
                        X_MOVE = +5

            """# IF - Keybinding State = keyup-stroke"""
            for key in event_dict.keys():
                if True in [*event_dict[key]]:    # 키-이벤트가 발생판단
                    if key == 'x_stop':
                        X_MOVE = 0

                    if key == 'y_stop':
                        Y_MOVE = 0

        """ # IF - Cross the Limit (X,Y) = stop there! """
        if POSX < 0:
            POSX = 0
        elif POSX > SCREEN_SIZE[0] - FIGHTER_WIDTH:
            POSX = SCREEN_SIZE[0] - FIGHTER_WIDTH

        if POSY < 0:
            POSY = 0
        elif POSY > SCREEN_SIZE[1] - FIGHTER_HEIGHT * 1.7:
            POSY = SCREEN_SIZE[1] - FIGHTER_HEIGHT * 1.7

        """ IF CRASHED .. (!) TODO: HAVE TO BE MODIFIED (!) """
        if POSY < ENEMY_Y + ENEMY_HEIGHT:
            if(ENEMY_X > POSX and ENEMY_X < POSX + FIGHTER_WIDTH) or\
                (ENEMY_X +ENEMY_WIDTH > POSX and ENEMY_X +
                ENEMY_WIDTH < POSX + FIGHTER_WIDTH):
                    if lives_count < 1:
                        display_gameover()
                    display_crash()
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
        POSX += X_MOVE
        POSY += Y_MOVE

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

        if ENEMY_X < 0:
            ENEMY_X = 0

        elif ENEMY_X > SCREEN_SIZE[0] - ENEMY_WIDTH:
            ENEMY_X = SCREEN_SIZE[0] - ENEMY_WIDTH

        if ENEMY_Y > (SCREEN_SIZE[1] - FIGHTER_HEIGHT + 30):
            ENEMY_X, ENEMY_Y = get_reset_enemy()
            img_enemy = get_enemy_img()
            enemy_passed += 1
            print(enemy_passed)

        if enemy_passed >= enemy_pass_limit:
            display_gameover()

        """ IS SHOOT? = SPEED++ """
        if is_hit:
            ENEMY_SPEED += 1

            if ENEMY_SPEED >= 20:
                ENEMY_SPEED = 20

            ENEMY_X, ENEMY_Y = get_reset_enemy()
            img_enemy = get_enemy_img()

            is_hit = False

        DISPLAYSURF.fill(BLACK)
        display_passed(enemy_passed)
        display_socre(shot_count)

        for n in range(1, lives_count):
            DISPLAYSURF.blit(
                img_lives,
                (
                    SCREEN_SIZE[0] - (FIGHTER_WIDTH * 0.5 * n) - 10,
                    SCREEN_SIZE[1] - FIGHTER_HEIGHT
                ))

        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                DISPLAYSURF.blit(img_bullet, (bx, by))

        DISPLAYSURF.blit(img_fighter, (POSX, POSY))
        DISPLAYSURF.blit(img_enemy, (ENEMY_X, ENEMY_Y))

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

    pygame.quit()
    sys.exit()
