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

background_image = pygame.image.load("assets/images/background/background.png").convert_alpha()
def draw_background():
    screen.blit(background_image, (0, 0))

fighter_1 = Fighter(200, 400)
fighter_2 = Fighter(700, 400)

run = True
while run:
    clock.tick(FPS)
    draw_background()
    fighter_1.move()
    fighter_2.move()
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
