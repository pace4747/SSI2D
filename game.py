import pygame
from pygame.locals import *
from player import Player
from world import World
from constants import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
        self.world = World(100, 50)  # Small map
        self.player = Player((VIRTUAL_WIDTH // 2, VIRTUAL_HEIGHT // 2))  # Start center
        self.camera_pos = [0, 0]
        self.all_sprites = pygame.sprite.Group(self.player)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.player.update_movement(keys, dt)
        # Clamp player to world boundaries (fixes sprinting out)
        self.player.rect.x = max(0, min(self.player.rect.x, self.world.width * TILE_SIZE - self.player.rect.width))
        self.player.rect.y = max(0, min(self.player.rect.y, self.world.height * TILE_SIZE - self.player.rect.height))
        # Update camera to center player
        self.camera_pos[0] = self.player.rect.centerx - (VIRTUAL_WIDTH // 2)
        self.camera_pos[1] = self.player.rect.centery - (VIRTUAL_HEIGHT // 2)
        # Clamp camera
        self.camera_pos[0] = max(0, min(self.camera_pos[0], self.world.width * TILE_SIZE - VIRTUAL_WIDTH))
        self.camera_pos[1] = max(0, min(self.camera_pos[1], self.world.height * TILE_SIZE - VIRTUAL_HEIGHT))

    def draw(self):
        self.virtual_screen.fill(COLORS['BLACK'])
        self.world.draw(self.virtual_screen, self.camera_pos)
        self.all_sprites.draw(self.virtual_screen)
        scaled_surf = pygame.transform.scale(self.virtual_screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(scaled_surf, (0, 0))
        pygame.display.flip()
