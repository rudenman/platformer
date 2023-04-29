import random
import pygame

from background import Background
from settings import *


class WaitMenu:
    def __init__(self, screen, font, text, active_background):
        self.screen = screen

        # self.background = pygame.surface.Surface((window_width, window_height))
        # self.background_rect = self.background.get_rect(topleft=(0, 0))
        self.live_background = active_background

        self.font = font

        self.point_1 = font.render(f"{text}", False, [203, 203, 203])
        self.point_1_rect = self.point_1.get_rect(center=(window_width / 2, window_height / 2))
        self.point_2 = font.render(" Выход", False, [203, 203, 203])
        self.point_2_rect = self.point_2.get_rect(
            center=(window_width / 2, window_height / 2 + self.point_1_rect.height + 50))

        self.current_option_index = 0
        self.active = False

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.current_option_index += 1
                    if self.current_option_index > 1:
                        self.current_option_index = 0
                elif event.key == pygame.K_s:
                    self.current_option_index -= 1
                    if self.current_option_index < 0:
                        self.current_option_index = 1
                elif event.key == pygame.K_RETURN:
                    self.active = True

    def animate_point(self):
        if self.current_option_index == 0:
            pygame.draw.rect(self.screen, "#151515", self.point_1_rect)
        else:
            pygame.draw.rect(self.screen, "#151515", self.point_2_rect)

    def draw_points(self):
        self.screen.blit(self.point_1, self.point_1_rect)
        self.screen.blit(self.point_2, self.point_2_rect)

    def update(self):
        self.input()
        self.live_background.update()
        self.animate_point()
        self.draw_points()
        if self.active and self.current_option_index == 0:
            return True
        return False


class LossMenu(WaitMenu):
    def __init__(self, screen, font, text, active_background):
        super().__init__(screen, font, text, active_background)
        self.loss_text = self.font.render("Поражение", False, [203,203,203])
        self.loss_text_rect = self.loss_text.get_rect(center=(window_width / 2, window_height / 5))

        self.level_data = None
        self.level_data_rect = None

    def update_level_data(self, level):
        self.level_data = self.font.render(f"Пройдено уровней: {level - 1}", False, [203, 203, 203])
        self.level_data_rect = self.level_data.get_rect(center=(window_width / 2, window_height / 3))

    def draw_level_data(self):
        self.screen.blit(self.level_data, self.level_data_rect)
        self.screen.blit(self.loss_text, self.loss_text_rect)

    def update_data(self, level):
        flag = not super().update()
        self.update_level_data(level)
        self.draw_level_data()
        return flag


class StartMenu(WaitMenu):
    def __init__(self, screen, font, text, active_background):
        super().__init__(screen, font, text, active_background)
        self.intro = self.font.render("Adventure time", False, [203, 203, 203])
        self.intro_rect = self.intro.get_rect(center=(window_width / 2, window_height / 4))

    def update_data(self):
        flag = super().update()
        self.screen.blit(self.intro, self.intro_rect)
        return flag
