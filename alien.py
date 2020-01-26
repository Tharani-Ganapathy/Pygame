import  pygame
from pygame.sprite import Sprite


image_resource = 'B:/PycharmPython/Pygame_Session/alien-space-ship.bmp'


class Alien(Sprite): # initialize the alien and the starting position
    def __init__(self, game_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # load the alien image and gets it rect
        self.image = pygame.image.load(image_resource)
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # print(self.rect.x)
        # print(self.rect.y)
        # store the aliens exact position
        self.x = self.rect.x

    def blitme(self): # draw the alien at the current location
        self.screen.blit(self.image, self.rect)

    def update(self): # move the alien left or right
        self.x += (self.game_settings.alien_speed_factor * self.game_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self): # return true if alien is at edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


