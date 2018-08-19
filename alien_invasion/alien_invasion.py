import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    #Inicjalizacja gry i utworzenie obiektu ekranu
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    #Utworzenie egzemplarza przeznaczonego do przechowywania danych statystycznych dotyczacych gry.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Zdefiniowanie koloru tła
    bg_color = (230, 230, 230)

    #Utworzenie statku kosmicznego
    ship = Ship(ai_settings,screen)


    #Utworzenie grupy przeznaczonej do przecowywania pocisków
    bullets = Group()
    #Utworzenie floty obcych
    aliens = Group()

    #Utworzenie floty obcych
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Utworzenie przycisku wygenerowanym
    play_button = Button(ai_settings, screen, "Gra")

    #Rozpoczecie petli glownej gry:
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats,  sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
