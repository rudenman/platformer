import pygame


class Tile():
    def __init__(self, pos, size):
        self.image = pygame.surface.Surface((size, size))
        self.image.fill("Black") # "#151515"
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
