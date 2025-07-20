import pygame
from pygame.locals import *
from player import Player
from world import World

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.world = World(100, 50)  # Small map
        self.player = Player((0, 0))
        self.camera_pos = [0, 0]  # Follow player
        self.all_sprites = pygame.sprite.Group(self.player)

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update_movement(keys)
        # Update camera to center player
        self.camera_pos[0] = self.player.rect.x - (SCREEN_WIDTH // 2)
        self.camera_pos[1] = self.player.rect.y - (SCREEN_HEIGHT // 2)

    def draw(self):
        self.screen.fill(COLORS['BLACK'])
        self.world.draw(self.screen, self.camera_pos)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
