import pygame
from pygame.sprite import Sprite

image_resources = 'B:/PycharmPython/Pygame_Session/fighter_ship.bmp'


class Ship(Sprite):

    def __init__(self, game_settings, screen): # initialize the ship and set its starting position
        super(Ship, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # load the ship image and gets it rect
        self.image = pygame.image.load(image_resources)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # store a decimal value for ship's centre
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self): # Update the ship's position based on the movement flags

        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Move the ship to the right
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # Move the ship to the left
            self.center -= self.game_settings.ship_speed_factor

        # update the rect object from self.center
        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
