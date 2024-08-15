import sys

import pygame

from background import Background
from level import Level
from menu import Menu
from settings import *
from statusBar import StatusBar
from waitMenu import WaitMenu, LossMenu, StartMenu


def close():
    pygame.quit()
    sys.exit()


pygame.init()

screen = pygame.display.set_mode((window_width, window_height))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

menu_font = pygame.font.Font("font/5.ttf", menu_font_size)
status_font = pygame.font.Font("font/5.ttf", status_font_size)

active_background = Background(screen)

start_menu = StartMenu(screen, menu_font, " Начать", active_background)
pause_menu = WaitMenu(screen, menu_font, " Продолжить", active_background)

transition_menu = Menu(screen, menu_font, " Нажмите Enter для продолжения", active_background)

loss_menu = LossMenu(screen, menu_font, " Повторить", active_background)

game_active = False
game_upgrade_level = False
game_pause = False
game_loss = False

level_number = 3
level = Level(screen, level_number)

status_bar = StatusBar(screen, status_font)

#####################
calc_active = False
calc_created = False

#####################


while True:
    if game_active:
        if not game_upgrade_level and not game_pause and not game_loss:  # and not calc_active and not text_task_active:
            pause_menu.active = False
            loss_menu.active = False

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        game_pause = True

            game_upgrade_level = level.run()

            counter_of_lives = level.get_counter_of_lives()
            status_bar.update(level_number, counter_of_lives)

            if counter_of_lives == -1:
                game_loss = True

        elif game_pause:
            if pause_menu.active:
                close()

            game_pause = not pause_menu.update()

        elif game_upgrade_level:
            if transition_menu.update(level_number):
                level = Level(screen, level_number + 1)
                level_number += 1
                game_upgrade_level = False

        elif game_loss:
            if loss_menu.active:
                close()
            game_loss = loss_menu.update_data(level_number)
            if not game_loss:
                level = Level(screen, 1)
                level_number = 1

    elif not game_active:
        if start_menu.active:
            close()
        game_active = start_menu.update_data()

    pygame.display.update()

    clock.tick(60)
