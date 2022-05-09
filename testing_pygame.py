import sys
import pygame

pygame.init()
image_resources = 'B:/PycharmPython/Pygame_Session/fighter_ship.bmp'

screen_width = 10000
screen_height = 6000

screen = pygame.display.set_mode((screen_width, screen_height))
image1 = pygame.image.load(image_resources)
image2 = pygame.image.load(image_resources)
rect1 = image1.get_rect()
rect2 = image2.get_rect()
screen_rect = screen.get_rect()

rect1.centerx = screen_rect.centerx
rect1.bottom = screen_rect.bottom

rect2.centerx = screen_rect.centerx + 100
rect2.bottom = screen_rect.bottom

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rect1.centerx -= 10
            elif event.key == pygame.K_z:
                rect2.centerx += 10

    screen.blit(image1, rect1)
    screen.blit(image2, rect2)


    pygame.display.flip()

