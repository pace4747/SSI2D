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
        r = max(0, min(255, 0 + shade))
        g = max(0, min(255, 255 - shade))
        b = max(0, min(255, 0 + shade))
        surf.set_at((x, y), (r, g, b))
    return surf

def generate_dirt():
    surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
    surf.fill((139, 69, 19))  # Base brown
    # Add speckles for texture
    for _ in range(30):
        x, y = random.randint(0, TILE_SIZE-1), random.randint(0, TILE_SIZE-1)
        shade = random.randint(-20, 20)  # Variations
        r = max(0, min(255, 139 + shade))
        g = max(0, min(255, 69 + shade))
        b = max(0, min(255, 19 + shade))
        surf.set_at((x, y), (r, g, b))
    return surf

# Create folder if needed
tiles_path = os.path.join(ASSETS_PATH, 'tiles')
os.makedirs(tiles_path, exist_ok=True)

# Save PNGs
pygame.image.save(generate_grass(), os.path.join(tiles_path, 'grass.png'))
pygame.image.save(generate_dirt(), os.path.join(tiles_path, 'dirt.png'))

print("Placeholder PNGs generated successfully in assets/tiles/")
