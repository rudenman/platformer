import pygame


class Lighting:
    def __init__(self, object):
        radius = object.rect.width * object.light_k
        self.image = pygame.Surface((radius, radius), pygame.SRCALPHA)

        self.rect = self.image.get_rect(center=object.rect.center)

        start_vis = 1
        for i in range(40):
            pygame.draw.circle(self.image, (object.color[0], object.color[1], object.color[2], start_vis),
                               (self.rect.width / 2, self.rect.width / 2), radius / 2)
            start_vis += 1
            radius -= object.rect.width * (object.light_k - 1) / 40

    def update(self, pos):
        self.rect.center = pos
