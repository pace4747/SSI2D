import pygame
import numpy as np
from constants import *

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = np.zeros((height, height), dtype=int)  # 0: grass, etc.
        self.generate_map()

    def generate_map(self):
        # Simple random "procedural" for prototype; use Perlin later
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[x][y] = np.random.choice([0, 1], p=[0.7, 0.3])  # 70% grass, 30% dirt

    def draw(self, screen, camera_pos):
        for x in range(self.width):
            for y in range(self.height):
                tile_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                adjusted_rect = tile_rect.move(-camera_pos[0], -camera_pos[1])
                if adjusted_rect.colliderect(screen.get_rect()):
                    color = COLORS['GREEN'] if self.tiles[x][y] == 0 else (139, 69, 69, 19)  # Brown for dirt
                    pygame.draw.rect(screen, color, adjusted_rect.scale_by(SCALE))
