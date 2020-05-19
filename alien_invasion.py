import sys

import pygame
from pygame.sprite import Group

import game_functions
from alien import Alien
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        game_functions.check_events(ship, ai_settings, screen, bullets)
        ship.update()
        game_functions.update_bullets(aliens, bullets, ai_settings, screen, ship)
        game_functions.update_aliens(ai_settings, aliens)
        game_functions.update_screen(ai_settings, screen, ship, bullets, aliens)


run_game()
