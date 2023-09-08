import pygame

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
CAPTION = "Brawler"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)

background_image = pygame.image.load("assets/images/background/background.png").convert_alpha()
def draw_background():
    screen.blit(background_image, (0, 0))

run = True
while run:
    draw_background()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
