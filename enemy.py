import random

from settings import *
import pygame


class Enemy:
    def __init__(self, pos, size):
        # цвет
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]  # [226, 136, 249]
        self.light_k = 16

        self.image = pygame.surface.Surface((size, size))
        self.rect = self.image.get_rect(center=(pos[0] + tile_size / 2, pos[1] + tile_size / 2))

        self.image.fill(self.color)

        self.speed = enemy_speed
        self.distance = tile_size * 6
        self.current_distance = 0
        self.to_right = True

    def update(self, x_shift):
        self.run()
        self.rect.x += x_shift


class HorizontalEnemy(Enemy):
    def __init__(self, pos, size):
        super().__init__(pos, size)

    def run(self):
        if self.current_distance < self.distance and self.to_right:
            self.rect.x += self.speed
        elif self.current_distance < self.distance and not self.to_right:
            self.rect.x -= self.speed
        self.current_distance += self.speed
        if self.current_distance >= self.distance:
            self.current_distance = 0
            self.to_right = not self.to_right


class VerticalEnemy(Enemy):
    def __init__(self, pos, size):
        super().__init__(pos, size)

    def run(self):
        if self.current_distance < self.distance and self.to_right:
            self.rect.y += self.speed
        elif self.current_distance < self.distance and not self.to_right:
            self.rect.y -= self.speed
        self.current_distance += self.speed
        if self.current_distance >= self.distance:
            self.current_distance = 0
            self.to_right = not self.to_right


class StaticEnemy(Enemy):
    def __init__(self, pos, size):
        super().__init__(pos, size)

    def run(self):
        pass
