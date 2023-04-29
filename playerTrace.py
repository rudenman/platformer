import pygame

from settings import *
from math import sin


class PlayerTrace:
    def __init__(self, player):
        self.image = pygame.surface.Surface((player.rect.width, player.rect.height), pygame.SRCALPHA)
        self.image.fill(player.color)
        self.image.set_alpha(60)
        self.rect = self.image.get_rect(center=player.rect.center)

    def update(self, map_shift):
        self.rect.left += map_shift
