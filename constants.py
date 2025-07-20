import pygame

TILE_SIZE = 16
SCALE = 4
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
VIRTUAL_WIDTH = SCREEN_WIDTH // SCALE
VIRTUAL_HEIGHT = SCREEN_HEIGHT // SCALE
FPS = 60

COLORS = {
    'BLACK': (0, 0, 0),
    'GREEN': (0, 255, 0),  # Fixed to actual green
    'BROWN': (139, 69, 19)  # Fixed dirt color, no alpha
}

BIOME_RATIOS = {'jungle': 0.4, 'swamp': 0.2, 'desert': 0.25, 'mountain': 0.15}
