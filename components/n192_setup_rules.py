import os
import sys
import time
import pygame
import random

FPS = 30

WORK_DIR = os.path.dirname(__file__)
ROOT_WORD = 'PyGalaga'                 # root directory
ROOT_DIR = WORK_DIR.partition(ROOT_WORD)[0] + WORK_DIR.partition(ROOT_WORD)[1]

DESTIN_DIR = os.path.join(ROOT_DIR, '_static' ,'pygame_sprites', 'Galaga\\')
print(DESTIN_DIR)

""" # COLOR TABLE """
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

PAD_WIDTH = 480
PAD_HEIGHT = 640

FIGHTER_WIDTH = 36
FIGHTER_HEIGHT = 38

ENEMY_WIDTH = 36
ENEMY_HEIGHT = 38

DICT_OBJ = {            # SIZE x,y   POS x,y   file_name
    'g_catcher' : [36, 38, 200, 100,'Green_Catcher.png'],
    'gremlin'   : [36, 38, 200, 150,'gremlin_0001.png'],
    'bee'       : [36, 38, 200, 50,'Fly_0001.png'],
    'scorpion'  : [36, 38, 200, 250,'scorpion_0001.png'],
    'pheonix'   : [36, 38, 200, 300,'pheonix_0001.png'],
    'bullet'    : [13, 22, 200, 550,'rocket_0001.png'],
    'boom_01'   : [26, 26, 200, 200,'Ship_explosion_0001'],
    'boom_02'   : [26, 26, 200, 200,'Ship_explosion_0002'],
    'boom_03'   : [26, 26, 200, 200,'Ship_explosion_0003'],
    'boom_04'   : [26, 26, 200, 200,'Ship_explosion_0004'],
    }

DICT_OBJ['fighter'] = [
    FIGHTER_WIDTH,
    FIGHTER_HEIGHT,
    (PAD_WIDTH - FIGHTER_WIDTH)/2,
    PAD_HEIGHT - (FIGHTER_HEIGHT + 10),
    'Ship_White.png']

DICT_OBJ['lives'] = [
    int(FIGHTER_WIDTH * 0.7),
    int(FIGHTER_HEIGHT * 0.7),
    (PAD_WIDTH - FIGHTER_WIDTH)/2,
    PAD_HEIGHT - (FIGHTER_HEIGHT + 10),
    'Ship_White.png']


"""  CALCULATE """
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
    text_pos.center = (PAD_WIDTH/2, PAD_HEIGHT/2)
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

def set_image(filename):
    return pygame.image.load(filename)

def set_size(obj, width, height):
    return pygame.transform.scale(obj, (width, height))

def set_rotate(obj, angle):
    return pygame.transform.rotate(obj, angle)

def set_obj(dict_key, f_name_wdir, rotate=0):
    """ MAKING IMAG_OBJ Using dict_key as OBJ_name """
    size_x = DICT_OBJ[dict_key][0]
    size_y = DICT_OBJ[dict_key][1]

    obj_name = set_image(f_name_wdir)
    obj_name = set_size(obj_name, size_x, size_y)
    obj_name = set_rotate(obj_name, rotate)
    return obj_name

def draw_object(obj, x, y):
    global DISPLAYSURF
    DISPLAYSURF.blit(obj, (x, y))

def get_reset_enemy():
    return random.randrange(0, PAD_WIDTH - ENEMY_WIDTH), 15

ENEMY_X, ENEMY_Y = get_reset_enemy()
ENEMY_SPEED = 5

fighter = set_obj('fighter', DESTIN_DIR+'Ship_White.png', rotate=0 )
bee = set_obj('bee', DESTIN_DIR+'Fly_0001.png', rotate=180)
bullet = set_obj('bullet', DESTIN_DIR+'rocket_0001.png', rotate=0)
lives = set_obj('lives', DESTIN_DIR+'Ship_White.png', rotate=0 )


if __name__ == '__main__':
    """ INITIALIZE GAME """
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((PAD_WIDTH, PAD_HEIGHT))
    pygame.display.set_caption('My GALAGA!!')
    FPS_CLK = pygame.time.Clock()   # FPS_CLK.tick(FPS)

    is_shot = False
    lives_count = 3
    shot_count = 0
    enemy_passed = 0

    bullet_xy = []

    x = PAD_WIDTH * 0.45                      # 45% start fighter X-point
    y = PAD_HEIGHT - (FIGHTER_HEIGHT * 1.7)   # 95% start fighter Y-point

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
        elif x > PAD_WIDTH - FIGHTER_WIDTH:
            x = PAD_WIDTH - FIGHTER_WIDTH

        if y < 0:
            y = 0
        elif y > PAD_HEIGHT - FIGHTER_HEIGHT * 1.7:
            y = PAD_HEIGHT - FIGHTER_HEIGHT * 1.7

        if ENEMY_Y > (PAD_HEIGHT - FIGHTER_HEIGHT * 1.7):
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

        if ENEMY_Y > PAD_HEIGHT - (FIGHTER_HEIGHT + 30):
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
                lives,
                PAD_WIDTH - (DICT_OBJ['lives'][0]*n),
                PAD_HEIGHT- DICT_OBJ['lives'][1])

        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                draw_object(bullet, bx, by)

        draw_object(fighter, x, y)
        draw_object(bee, ENEMY_X, ENEMY_Y)

        pygame.display.update()
        FPS_CLK.tick(FPS)

    pygame.quit()
    sys.exit()
