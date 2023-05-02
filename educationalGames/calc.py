import random
import pygame

from settings import *


class Calc:
    def __init__(self, screen, font, active_background):
        self.screen = screen
        self.color = [203, 203, 203]

        self.live_background = active_background

        self.font = font

        self.task = "Cколько будет "

        self.number1 = random.randint(0, 30)
        self.task += str(self.number1)
        self.number2 = random.randint(0, 30)
        self.operation = random.randint(0, 2)
        self.result = None

        if self.operation == 0:
            self.result = self.number1 + self.number2
            self.task += " + "
        elif self.operation == 1:
            self.result = self.number1 - self.number2
            self.task += " - "
        elif self.operation == 2:
            self.result = self.number1 * self.number2
            self.task += " * "
        self.task += str(self.number2)
        self.task += "?"

        self.task_text = font.render(f"{self.task}", False, self.color)
        self.task_text_rect = self.task_text.get_rect(center=(window_width / 2, window_height / 4))

        self.answers = []
        self.answers_text = []
        self.answers_text_rect = []

        self.result_index = random.randint(0, 3)

        for i in range(4):
            if i != self.result_index:
                self.answers.append(self.result + random.randint(-200, 200))
            else:
                self.answers.append(self.result)
            self.answers_text.append(font.render(f"{self.answers[i]}", False, self.color))
            self.answers_text_rect.append(self.answers_text[i].get_rect(
                center=(window_width / 2, window_height / 2 + i * 100)))

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
                elif event.key == pygame.K_RETURN:
                    self.active = True

    def animate_answer(self):
        for i in range(len(self.answers_text_rect)):
            if i == self.current_option_index:
                pygame.draw.rect(self.screen, "#151515", self.answers_text_rect[i])
                break

    def draw_answers(self):
        self.screen.blit(self.task_text, self.task_text_rect)
        for i in range(len(self.answers)):
            self.screen.blit(self.answers_text[i], self.answers_text_rect[i])

    def update(self):
        self.input()

        self.live_background.update()
        self.animate_answer()

        self.draw_answers()
        if self.result == self.answers[self.current_option_index] and self.active:
            self.right = True
