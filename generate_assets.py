import pygame
import os
import random
from constants import TILE_SIZE, ASSETS_PATH  # Reuse your constants

pygame.init()

def generate_grass():
    surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
    surf.fill((0, 128, 0))  # Base dark green
    # Add simple "grass blades" for texture
    for _ in range(50):  # Random pixels
        x, y = random.randint(0, TILE_SIZE-1), random.randint(0, TILE_SIZE-1)
        shade = random.randint(0, 50)  # Lighter greens
        surf.set_at((x, y), (0 + shade, 255 - shade, 0 + shade))
    return surf

def generate_dirt():
    surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
    surf.fill((139, 69, 19))  # Base brown
    # Add speckles for texture
    for _ in range(30):
        x, y = random.randint(0, TILE_SIZE-1), random.randint(0, TILE_SIZE-1)
        shade = random.randint(-20, 20)  # Variations
        surf.set_at((x, y), (139 + shade, 69 + shade, 19 + shade))
    return surf

# Create folder if needed
tiles_path = os.path.join(ASSETS_PATH, 'tiles')
os.makedirs(tiles_path, exist_ok=True)

# Save PNGs
pygame.image.save(generate_grass(), os.path.join(tiles_path, 'grass.png'))
pygame.image.save(generate_dirt(), os.path.join(tiles_path, 'dirt.png'))

print("Placeholder PNGs generated in assets/tiles/")
