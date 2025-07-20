import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE * 2))  # 16x32 placeholder
        self.image.fill((0, 0, 255))  # Blue rect for player
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 2  # Adjusted for virtual scale (pixels per frame)
        self.stamina = 100
        self.direction = pygame.Vector2(0, 0)

    def update_movement(self, keys, dt):
        self.direction.x = (keys[pygame.K_d] - keys[pygame.K_a])
        self.direction.y = (keys[pygame.K_s] - keys[pygame.K_w])
        if self.direction.length() > 0:
            self.direction.normalize_ip()
        self.direction *= self.speed

        is_sprinting = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]  # Use either shift
        if is_sprinting and self.stamina > 0:
            self.direction *= 1.5
            self.stamina -= 5 * dt  # Drain 5 per second (dt in seconds)
        else:
            if self.stamina < 100:
                self.stamina += 5 * dt  # Regen 5 per second

        self.rect.move_ip(int(self.direction.x), int(self.direction.y))
        # Optional grid snap: self.rect.x = round(self.rect.x / TILE_SIZE) * TILE_SIZE
        # self.rect.y = round(self.rect.y / TILE_SIZE) * TILE_SIZE
        self.stamina = max(0, min(100, self.stamina))  # Clamp
