import pygame
from fighter import Fighter

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
CAPTION = "Brawler"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)

clock = pygame.time.Clock()
FPS = 60

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#player scores
round_over = False
ROUND_OVER_COOLDOWN = 2000

#define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

#load background
background_image = pygame.image.load("assets/images/background/background.png").convert_alpha()

#load fighter sprites
warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()

#load victory image
victory_img = pygame.image.load("assets/images/icons/victory.png").convert_alpha()

#animation steps
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

#define font
count_font = pygame.font.Font("assets/fonts/Turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/Turok.ttf", 30)

#draw text function
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_background():
    screen.blit(background_image, (0, 0))

def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, RED, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

fighter_1 = Fighter(1, 200, 400, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS)
fighter_2 = Fighter(2, 700, 400, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)

run = True
while run:
    clock.tick(FPS)
    draw_background()
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)
    draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
    draw_text("P1: " + str(score[1]), score_font, RED, 580, 60)

    if intro_count <= 0:
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
    else:
        draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()
    #update fighters
    fighter_1.update()
    fighter_2.update()

    fighter_1.draw(screen)
    fighter_2.draw(screen)

    if round_over == False:
        if fighter_1.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        screen.blit(victory_img, (360, 150))
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            round_over = False
            intro_count = 3
            fighter_1 = Fighter(1, 200, 400, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS)
            fighter_2 = Fighter(2, 700, 400, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
