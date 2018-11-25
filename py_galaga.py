"""
# 메인 앱 - 실행
# 위치: root
#
#\n\n\n"""
print(__doc__)
import time
import pygame

from asset.config import *
from asset.sprite import *
from asset.class_hero import *


ENEMY_X, ENEMY_Y = get_reset_enemy()
ENEMY_SPEED = 5

if __name__ == '__main__':
    """ INITIALIZE GAME """
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
    pygame.display.set_caption('My GALAGA!!')
    FPS_CLK = pygame.time.Clock()   # FPS_CLK.tick(FPS)

    is_shot = False
    lives_count = 3
    shot_count = 0
    enemy_passed = 0

    bullet_xy = []

    x = SCREEN_SIZE[0] * 0.45                      # 45% start fighter X-point
    y = SCREEN_SIZE[1] - (FIGHTER_HEIGHT * 1.7)   # 95% start fighter Y-point

    x_change = 0                             # not moving
    y_change = 0

    ongame = False

    while not ongame:
        # IF - Keybinding State
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = +5

                elif event.key == pygame.K_UP:
                    y_change = -5

                elif event.key == pygame.K_DOWN:
                    y_change = +5

                elif event.key == pygame.K_LCTRL:
                    if len(bullet_xy) < 3:
                        BULL_X = int(x + FIGHTER_WIDTH/2)
                        BULL_Y = int(y - FIGHTER_HEIGHT)
                        bullet_xy.append([BULL_X, BULL_Y])

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
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

        if ENEMY_Y > (SCREEN_SIZE[1] - FIGHTER_HEIGHT * 1.7):
            ENEMY_X, ENEMY_Y = get_reset_enemy()

        """ IF CRASHED .. (!) HAVE TO BE MODIFIED (!) """
        if y < ENEMY_Y + ENEMY_HEIGHT:
            if(ENEMY_X > x and ENEMY_X < x + FIGHTER_WIDTH) or\
                (ENEMY_X +ENEMY_WIDTH > x and ENEMY_X +
                ENEMY_WIDTH < x + FIGHTER_WIDTH):
                    crash_display()
                    if lives_count < 1:
                        game_over_display()
                    ENEMY_Y = 0

        # print("!:", bullet_xy)
        """ IF ENEMY IS SHOT """
        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[1] -= 10
                bullet_xy[i][1] = bxy[1]

                """ IF SHOT HITS THE ENEMY """
                if bxy[1] < ENEMY_Y:
                    if bxy[0] > ENEMY_X and bxy[0] < ENEMY_X + ENEMY_WIDTH:
                        bullet_xy.remove(bxy)
                        is_shot = True
                        shot_count += 1

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

        # [POS] Give BULLIT a move
        # BULL_Y -= 10
        # if BULL_Y <= 10:
        #     BULL_X = x + (FIGHTER_WIDTH/2 - DICT_OBJ['bullet'][0]/2)
        #     BULL_Y = y

        """ IS SHOOT? = SPEED++ """
        if is_shot:
            ENEMY_SPEED += 1

            if ENEMY_SPEED >= 20:
                ENEMY_SPEED = 20

            ENEMY_X, ENEMY_Y = get_reset_enemy()
            is_shot = False

        DISPLAYSURF.fill(BLACK)
        draw_passed(enemy_passed)
        draw_socre(shot_count)

        for n in range(1, lives_count):
            draw_object(
                OBJ_LIVES,
                SCREEN_SIZE[0] - (DICT_OBJ['lives'][0]*n),
                SCREEN_SIZE[1]- DICT_OBJ['lives'][1])

        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                draw_object(OBJ_BULLET, bx, by)

        draw_object(OBJ_FIGHTER, x, y)
        draw_object(OBJ_BEE, ENEMY_X, ENEMY_Y)

        pygame.display.update()
        FPS_CLK.tick(FPS)

    pygame.quit()
    sys.exit()
