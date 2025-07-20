import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE * 2))  # 16x16 placeholder
        self.image.fill((0, 0, 255))  # Blue rect for player
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 4  # Pixels per frame
        self.stamina = 100
        self.direction = pygame.Vector2(0, 0)

    def update_movement(self, keys):
        self.direction.x = (keys[pygame.K_d] - keys[pygame.K_a]) * self.speed
        self.direction.y = (keys[pygame.K_s] - keys[pygame.K_w]) * self.speed
        if keys[pygame.K_SHIFT] and self.stamina > 0:
            self.direction *= 1.5
            self.stamina -= 1
        else:
            if self.stamina < 100:
                self.stamina += 1
        self.rect.move_ip += (self.direction)  # Grid snap later: self.rect.x = round(self.rect.x / TILE_SIZE) * TILE_SIZE
