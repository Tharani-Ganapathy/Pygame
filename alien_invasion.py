import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # make the play button
    play_button = Button(game_settings, screen, "Start")
    # create an instance to store game statistics and create a score board
    stats = GameStats(game_settings)
    sb = Scoreboard(game_settings, screen, stats)

    stats.reset_stats()
    # Make a ship
    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()

    # create the fleet  of aliens
    gf.create_fleet(game_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(game_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(game_settings, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(game_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()