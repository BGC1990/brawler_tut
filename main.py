import pygame

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200
CAPTION = "Brawler"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
