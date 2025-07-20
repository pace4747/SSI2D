import pygame
import numpy as np
import os
from constants import *

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = np.zeros((self.width, self.height), dtype=int)  # 0: grass, 1: dirt
        self.generate_map()
        # Load tile images (fallback to colors if missing)
        self.grass_img = None
        self.dirt_img = None
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))  # Get absolute path to script dir
            grass_path = os.path.join(base_dir, ASSETS_PATH, 'tiles', 'grass.png')
            dirt_path = os.path.join(base_dir, ASSETS_PATH, 'tiles', 'dirt.png')
            self.grass_img = pygame.image.load(grass_path).convert()
            self.dirt_img = pygame.image.load(dirt_path).convert()
            print(f"Loaded tiles successfully from: {grass_path} and {dirt_path}")
        except Exception as e:  # Catch all issues
            print(f"Warning: Failed to load tile PNGs ({e}). Using color fallbacks. Check if files exist and are valid PNGs.")

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
                tile_type = self.tiles[x][y]
                if self.grass_img and self.dirt_img:  # Use images if loaded
                    img = self.grass_img if tile_type == 0 else self.dirt_img
                    screen.blit(img, adjusted_rect)
                else:  # Fallback to colors
                    color = COLORS['GREEN'] if tile_type == 0 else COLORS['BROWN']
                    pygame.draw.rect(screen, color, adjusted_rect)
