from enemy import *
from lighting import Lighting


class Background:
    def __init__(self, surface):
        self.surface = surface
        self.image = pygame.surface.Surface((window_width, window_height))
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.image.fill("#202020")

        self.enemies = []
        self.enemies_lighting = []
        self.create()

    def create(self):
        for i, row in enumerate(map_background):
            for j, element in enumerate(row):
                x = j * tile_size
                y = i * tile_size
                if element == 'S':
                    enemy_sprite = StaticEnemy((x, y), enemy_size)
                    self.enemies.append(enemy_sprite)
                    enemy_lighting = Lighting(enemy_sprite)
                    self.enemies_lighting.append(enemy_lighting)

    def update(self):
        self.surface.blit(self.image, self.rect)
        i = 0
        for enemy in self.enemies:
            self.surface.blit(self.enemies_lighting[i].image, self.enemies_lighting[i].rect)
            self.surface.blit(enemy.image, enemy.rect)
            i += 1
