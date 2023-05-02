import random

from waitMenu import WaitMenu, LossMenu, StartMenu
from settings import *
from level import Level
from statusBar import StatusBar
from menu import Menu
import pygame
from educationalGames.calc import Calc
from educationalGames.textTask import TextTask
from background import Background


def close():
    pygame.quit()
    exit()


pygame.init()

screen = pygame.display.set_mode((window_width, window_height))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

menu_font = pygame.font.Font("font/5.ttf", 120)
status_font = pygame.font.Font("font/5.ttf", 60)
calc_font = pygame.font.Font("font/5.ttf", 80)
edu_font1 = pygame.font.Font("font/5.ttf", 80)
edu_font2 = pygame.font.Font("font/5.ttf", 60)

# menu_font = pygame.font.Font("font/3.ttf", 150)
# status_font = pygame.font.Font("font/3.ttf", 60)
# edu_font = pygame.font.Font("font/3.ttf", 80)

active_background = Background(screen)

start_menu = StartMenu(screen, menu_font, " Начать", active_background)
pause_menu = WaitMenu(screen, menu_font, " Продолжить", active_background)

transition_menu = Menu(screen, menu_font, " Нажмите Enter для продолжения", active_background)

loss_menu = LossMenu(screen, menu_font, " Повторить", active_background)

game_active = False
game_upgrade_level = False
game_pause = False
game_loss = False

level = Level(screen)
level_number = 1

status_bar = StatusBar(screen, status_font)

#####################
calc_active = False
calc_created = False

#####################

#####################
text_task_active = False
text_task_created = False

#####################


while True:
    if game_active:
        if not game_upgrade_level and not game_pause and not game_loss and not calc_active and not text_task_active:
            pause_menu.active = False
            loss_menu.active = False

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        game_pause = True

            if random.randint(0, 10) > 1:
                text_task_active = level.run()
            else:
                calc_active = level.run()

            counter_of_lives = level.get_counter_of_lives()
            status_bar.update(level_number, counter_of_lives)

            if counter_of_lives == -1:
                game_loss = True

        elif game_pause:
            if pause_menu.active:
                close()
            game_pause = not pause_menu.update()

        elif calc_active:
            if not calc_created:
                calc = Calc(screen, calc_font, active_background)
                calc_created = True
            calc.update()
            if calc.right:
                calc_active = False
                calc_created = False
                game_upgrade_level = True
            elif calc.active:
                calc_active = False
                calc_created = False
                game_loss = True
        elif text_task_active:
            if not text_task_created:
                text_task = TextTask(screen, edu_font1, edu_font2, active_background)
                text_task_created = True
            text_task.update()
            if text_task.right:
                text_task_active = False
                text_task_created = False
                game_upgrade_level = True
            elif text_task.active:
                text_task_active = False
                text_task_created = False
                game_loss = True
        elif game_upgrade_level:
            if transition_menu.update(level_number):
                level = Level(screen)
                level_number += 1
                game_upgrade_level = False

        elif game_loss:
            if loss_menu.active:
                close()
            game_loss = loss_menu.update_data(level_number)
            if not game_loss:
                level = Level(screen)
                level_number = 1

    elif not game_active:
        if start_menu.active:
            close()
        game_active = start_menu.update_data()

    pygame.display.update()

    clock.tick(60)
