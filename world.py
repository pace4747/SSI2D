import pygame
import numpy as np
from constants import *

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = np.zeros((self.width, self.height), dtype=int)  # Fixed: (width, height)
        self.generate_map()

    def generate_map(self):
        # Simple random "procedural" for prototype; use Perlin later
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[x][y] = np.random.choice([0, 1], p=[0.7, 0.3])  # 70% grass, 30% dirt

    def draw(self, screen, camera_pos):
        start_x = max(0, camera_pos[0] // TILE_SIZE)
        start_y = max(0, camera_pos[1] // TILE_SIZE)
        end_x = min(self.width, start_x + (VIRTUAL_WIDTH // TILE_SIZE) + 1)
        end_y = min(self.height, start_y + (VIRTUAL_HEIGHT // TILE_SIZE) + 1)

        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                tile_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                adjusted_rect = tile_rect.move(-camera_pos[0], -camera_pos[1])
                color = COLORS['GREEN'] if self.tiles[x][y] == 0 else COLORS['BROWN']
                pygame.draw.rect(screen, color, adjusted_rect)
