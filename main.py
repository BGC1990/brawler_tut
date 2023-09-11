import pygame
from fighter import Fighter

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
CAPTION = "Brawler"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)

background_image = pygame.image.load("assets/images/background/background.png").convert_alpha()
def draw_background():
    screen.blit(background_image, (0, 0))

fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

run = True
while run:
    draw_background()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
