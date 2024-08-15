from math import sin

import pygame

from settings import *


class Player:
    def __init__(self, pos):
        # цвет
        self.color = [203, 203, 203]
        self.light_k = 11

        self.image_stop = pygame.image.load("graphics/stopNew.png").convert_alpha()
        self.image_stop = pygame.transform.scale(self.image_stop, (player_size, player_size))

        self.image_run = pygame.image.load("graphics/runNew.png").convert_alpha()
        self.image_run = pygame.transform.scale(self.image_run, (player_size, player_size))

        self.image = self.image_stop

        self.rect = self.image.get_rect(topleft=pos)

        # Движение персонажа
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = object_speed
        self.gravity = gravity  # 0.8
        self.jump_speed = -jump_speed  # -22

        # Состояние персонажа
        self.on_ground = False

        # Здоровье персонажа
        self.counter_of_lives = 3
        self.invisibility = False
        self.invisibility_duration = 1500
        self.hurt_time = 0

    def get_damage(self):
        if not self.invisibility:
            self.counter_of_lives -= 1
            self.invisibility = True
            self.hurt_time = pygame.time.get_ticks()

    def invisibility_timer(self):
        if self.invisibility:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.invisibility_duration:
                self.invisibility = False
        else:
            self.image.set_alpha(255)

    @staticmethod
    def wave_value():
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.image = self.image_run
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.image = pygame.transform.flip(self.image_run, True, False)
        else:
            self.direction.x = 0
            self.image = self.image_stop

        if keys[pygame.K_w] and self.on_ground:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.input()
        self.invisibility_timer()
