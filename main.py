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

background_image = pygame.image.load("assets/images/background/background.png").convert_alpha()
def draw_background():
    screen.blit(background_image, (0, 0))

def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, RED, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

fighter_1 = Fighter(200, 400)
fighter_2 = Fighter(700, 400)

run = True
while run:
    clock.tick(FPS)
    draw_background()
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)

    fighter_1.draw(screen)
    fighter_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
