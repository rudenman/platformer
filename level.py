import random

import pygame.draw
from tile import Tile
from player import Player
from enemy import *
from reward import Reward
from lighting import Lighting
from settings import *
from playerTrace import PlayerTrace


class Level:
    def __init__(self, screen, level_number):
        # init_images()

        if level_number < 5:
            self.level_number = level_number
        else:
            self.level_number = 5

        self.reward = None
        self.reward_lighting = None

        self.enemies = []
        self.enemies_lighting = []

        self.tiles = []

        self.player = None
        self.player_lighting = None
        self.player_trace = []

        self.screen = screen

        self.create_level()

        self.map_shift = 0

        self.current_x = 0

    def create_level(self):
        delta_x = 0
        level = [map_start]

        for i in range(self.level_number):
            random.shuffle(map_parts)
            level.append(map_parts[random.randint(0, len(map_parts) - 1)])
        level.append(map_end)

        for part in level:
            for i, row in enumerate(part):
                for j, element in enumerate(row):
                    x = (delta_x + j) * tile_size
                    y = i * tile_size
                    if element == 'X':
                        tile_sprite = Tile((x, y), tile_size)
                        self.tiles.append(tile_sprite)
                    elif element == 'H':
                        enemy_sprite = HorizontalEnemy((x, y), enemy_size)
                        self.enemies.append(enemy_sprite)
                        enemy_lighting = Lighting(enemy_sprite)
                        self.enemies_lighting.append(enemy_lighting)
                    elif element == 'V':
                        enemy_sprite = VerticalEnemy((x, y), enemy_size)
                        self.enemies.append(enemy_sprite)
                        enemy_lighting = Lighting(enemy_sprite)
                        self.enemies_lighting.append(enemy_lighting)
                    elif element == 'S':
                        enemy_sprite = StaticEnemy((x, y), enemy_size)
                        self.enemies.append(enemy_sprite)
                        enemy_lighting = Lighting(enemy_sprite)
                        self.enemies_lighting.append(enemy_lighting)
                    elif element == 'P':
                        self.player = Player((x, y))
                        self.player_lighting = Lighting(self.player)
                        self.player_trace = [PlayerTrace(self.player)] * 10
                    elif element == 'F':
                        self.reward = Reward((x, y), tile_size)
                        self.reward_lighting = Lighting(self.reward)
            delta_x += map_width

    def get_counter_of_lives(self):
        return self.player.counter_of_lives

    def scroll_x(self):
        player_x = self.player.rect.centerx
        direction_x = self.player.direction.x

        if player_x < window_width / 3 and direction_x < 0:
            self.map_shift = object_speed
            self.player.speed = 0
        elif player_x > window_width - window_width / 3 and direction_x > 0:
            self.map_shift = -object_speed
            self.player.speed = 0
        else:
            self.map_shift = 0
            self.player.speed = object_speed

    def horizontal_movement_collision(self):
        self.player.rect.x += self.player.direction.x * self.player.speed

        for tile in self.tiles:
            if tile.rect.colliderect(self.player.rect):
                if self.player.rect.centerx < tile.rect.centerx:
                    self.player.rect.right = tile.rect.left
                else:
                    self.player.rect.left = tile.rect.right

    def vertical_movement_collision(self):
        self.player.apply_gravity()

        for tile in self.tiles:
            if tile.rect.colliderect(self.player.rect):
                if self.player.rect.centery < tile.rect.centery:
                    self.player.rect.bottom = tile.rect.top
                    self.player.on_ground = True
                else:
                    self.player.rect.top = tile.rect.bottom
                    self.player.on_ground = False
                self.player.direction.y = 0

        if self.player.on_ground and self.player.direction.y < 0 or self.player.direction.y > 0:
            self.player.on_ground = False

    def check_position(self):
        if self.player.rect.bottom >= window_height:
            self.player.direction.y = -jump_speed * 3 / 2
            self.player.get_damage()

    def check_enemy_collisions(self):
        for enemy in self.enemies:
            if enemy.rect.colliderect(self.player.rect):
                self.player.direction.y = -15
                self.player.get_damage()
                return

    def check_reward_collision(self):
        if self.reward.rect.colliderect(self.player.rect):
            return True
        return False

    def draw_light(self, object_rect):
        pygame.draw.circle(self.screen, "White", object_rect.center, object_rect.width)

    def draw(self):
        for tile in self.tiles:
            self.screen.blit(tile.image, tile.rect)

        i = 0
        for enemy in self.enemies:
            self.screen.blit(self.enemies_lighting[i].image, self.enemies_lighting[i].rect)
            self.screen.blit(enemy.image, enemy.rect)
            i += 1

        self.screen.blit(self.reward_lighting.image, self.reward_lighting.rect)
        self.screen.blit(self.reward.image, self.reward.rect)

        self.screen.blit(self.player_lighting.image, self.player_lighting.rect)
        for trace in self.player_trace:
            self.screen.blit(trace.image, trace.rect)
        self.screen.blit(self.player.image, self.player.rect)

    def run(self):
        self.screen.fill("#202020")

        # reward
        self.reward.update(self.map_shift)
        self.reward_lighting.update(self.reward.rect.center)

        # tile
        for tile in self.tiles:
            tile.update(self.map_shift)

        self.scroll_x()

        # enemy
        i = 0
        for enemy in self.enemies:
            enemy.update(self.map_shift)
            self.enemies_lighting[i].update(enemy.rect.center)
            i += 1

        # player

        self.player.update()

        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player_lighting.update(self.player.rect.center)

        for index in range(len(self.player_trace) - 1):
            self.player_trace[index] = self.player_trace[index + 1]
            self.player_trace[index].update(self.map_shift)
        self.player_trace[len(self.player_trace) - 1] = PlayerTrace(self.player)

        ###################

        self.check_position()
        self.check_enemy_collisions()

        self.draw()

        return self.check_reward_collision()
