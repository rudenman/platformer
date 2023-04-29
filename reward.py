import pygame


class Reward:
    def __init__(self, pos, size):
        # цвет
        self.color = [222, 246, 116]
        self.light_k = 21

        self.image = pygame.surface.Surface((size, size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
