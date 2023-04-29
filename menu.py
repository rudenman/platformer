import random
import pygame

from background import Background
from settings import *


class Menu:
    def __init__(self, screen, font, text, active_background):
        self.level_data_rect = None
        self.level_data = None
        self.screen = screen
        self.font = font

        self.live_background = active_background

        self.win_text = font.render("Победа", False, [203, 203, 203])
        self.win_text_rect = self.win_text.get_rect(center=(window_width / 2, window_height * 2 / 6))

        self.continue_point = font.render(f"{text}", False, [203, 203, 203])
        self.continue_point_rect = self.continue_point.get_rect(center=(window_width / 2, window_height * 4.5 / 6))

    def update_level_data(self, level):
        self.level_data = self.font.render(f"Пройдено уровней: {level}", False, [203, 203, 203])
        self.level_data_rect = self.level_data.get_rect(center=(window_width / 2, window_height * 2.5 / 6))

    def input(self):
        flag = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    flag = True
        return flag

    def draw(self):
        self.screen.blit(self.level_data, self.level_data_rect)
        self.screen.blit(self.continue_point, self.continue_point_rect)
        self.screen.blit(self.win_text, self.win_text_rect)

    def update(self, level):
        self.update_level_data(level)
        self.live_background.update()
        self.draw()
        return self.input()
