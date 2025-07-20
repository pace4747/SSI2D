import pygame

TILE_SIZE = 16
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCALE = 4  # For pixel art crispness
FPS = 60

COLORS = {
    'BLACK': (0, 0, 0),
    'GREEN': (255, 255, 255),  # Placeholder for tiles
}

BIOME_RATIOS = {'jungle': 0.4, 'swamp': 0.2, 'desert': 0.25, 'mountain': 0.15}
