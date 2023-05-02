import random
from random import shuffle
import pygame

from settings import *
from educationalGames.taskStrings import tasks


class TextTask:
    def __init__(self, screen, font1, font2, active_background):
        self.screen = screen
        self.color = [203, 203, 203]

        self.live_background = active_background

        self.font1 = font1
        self.font2 = font2

        shuffle(tasks)

        self.task = tasks[random.randint(0, len(tasks) - 1)]
        self.task_split = self.task[0].split("\n")
        self.task_text = []
        self.task_text_rect = []
        for i in range(len(self.task_split)):
            self.task_text.append(font1.render(f"{self.task_split[i]}", False, self.color))
            self.task_text_rect.append(
                self.task_text[i].get_rect(center=(window_width / 2, window_height / 4 + i * 100)))


        self.answers = []
        self.answers_text = []
        self.answers_text_rect = []

        self.result = None

        for i in range(4):
            if "true" in self.task[i + 1]:
                self.result = self.task[i + 1][4:]
                self.answers.append(self.result)
                # self.answers_text.append(font.render(f"{self.result}", False, self.color))
                # self.answers_text_rect.append(self.answers_text[i].get_rect(
                #     center=(window_width * (i + 1) / 5, window_height * 7 / 8)))
            else:
                self.answers.append(self.task[i + 1])
                # self.answers_text.append(font.render(f"{self.answers[i]}", False, self.color))
                # self.answers_text_rect.append(self.answers_text[i].get_rect(
                #     center=(window_width * (i + 1) / 5, window_height * 7 / 8)))

        shuffle(self.answers)

        for i in range(4):
            self.answers_text.append(font2.render(f"{self.answers[i]}", False, self.color))
            if i < 2:
                self.answers_text_rect.append(self.answers_text[i].get_rect(
                    center=(window_width / 3, window_height * (i + 6) / 8)))
            else:
                self.answers_text_rect.append(self.answers_text[i].get_rect(
                    center=(window_width * 2 / 3, window_height * (i + 4) / 8)))

        self.current_option_index = 0
        self.active = False
        self.right = False

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.current_option_index -= 1
                    if self.current_option_index < 0:
                        self.current_option_index = 3
                elif event.key == pygame.K_s:
                    self.current_option_index += 1
                    if self.current_option_index > 3:
                        self.current_option_index = 0
                elif event.key == pygame.K_d:
                    self.current_option_index += 2
                    if self.current_option_index == 4:
                        self.current_option_index = 0
                    elif self.current_option_index == 5:
                        self.current_option_index = 1
                elif event.key == pygame.K_a:
                    self.current_option_index -= 2
                    if self.current_option_index == -1:
                        self.current_option_index = 3
                    elif self.current_option_index == -2:
                        self.current_option_index = 2
                elif event.key == pygame.K_RETURN:
                    self.active = True

    def animate_answer(self):
        for i in range(len(self.answers_text_rect)):
            if i == self.current_option_index:
                pygame.draw.rect(self.screen, "#151515", self.answers_text_rect[i])
                break

    def draw_answers(self):
        for i in range(len(self.task_text)):
            self.screen.blit(self.task_text[i], self.task_text_rect[i])

        for i in range(len(self.answers)):
            self.screen.blit(self.answers_text[i], self.answers_text_rect[i])

    def update(self):
        self.input()

        self.live_background.update()
        self.animate_answer()

        self.draw_answers()
        if self.result == self.answers[self.current_option_index] and self.active:
            self.right = True
