import pygame

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.tile_size = 16  # Tile size for the game world
        self.tile_images = {}  # To store loaded tile images
        self.load_tile_images()

    def load_tile_images(self):
        # Biome tile types and fallback colors
        tile_types = {
            'grass': (0, 255, 0),  # Green
            'dirt': (139, 69, 19),  # Brown
            'sand': (244, 164, 96),  # Sandy
            'rock': (128, 128, 128),  # Gray
            'vine': (0, 100, 0),  # Dark green
            'water': (0, 0, 255)  # Blue
        }
        for tile_type, fallback_color in tile_types.items():
            try:
                img = pygame.image.load(f"{tile_type}.png").convert_alpha()
                self.tile_images[tile_type] = pygame.transform.scale(img, (self.tile_size, self.tile_size))
                print(f"Loaded {tile_type}.png")
            except pygame.error as e:
                print(f"Warning: Could not load {tile_type}.png ({e}). Using fallback color.")
                surf = pygame.Surface((self.tile_size, self.tile_size))
                surf.fill(fallback_color)
                self.tile_images[tile_type] = surf

    def render(self, screen, entities, camera_x, camera_y):
        self.screen.fill((0, 0, 0))  # Clear screen to black
        
        # Simple test tilemap (20x20 grid with repeating biomes for testing)
        tilemap = [
            ['grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt'],
            ['dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand'],
            ['sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock'],
            ['rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine'],
            ['vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water'],
            ['water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass'],
            ['grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt'],
            ['dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand'],
            ['sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock'],
            ['rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine'],
            ['vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water'],
            ['water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass'],
            ['grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt'],
            ['dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand'],
            ['sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock'],
            ['rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine'],
            ['vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water'],
            ['water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass'],
            ['grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt'],
            ['dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand', 'rock', 'vine', 'water', 'grass', 'dirt', 'sand']
        ]
        
        # Draw tiles (with camera offset)
        for y, row in enumerate(tilemap):
            for x, tile_type in enumerate(row):
                self.screen.blit(self.tile_images[tile_type], (x * self.tile_size - camera_x, y * self.tile_size - camera_y))
        
        # Draw entities
        for entity in entities:
            entity.render(self.screen, camera_x, camera_y)

        # Health bar (with colors defined here)
        GREEN = (0, 255, 0)
        YELLOW = (255, 255, 0)
        RED = (255, 0, 0)
        health_ratio = 0.75  # Test value; replace with player.health / 100 later
        health_color = GREEN if health_ratio > 0.5 else YELLOW if health_ratio > 0.25 else RED
        pygame.draw.rect(self.screen, health_color, (10, 10, 200 * health_ratio, 20))  # Filled bar
        pygame.draw.rect(self.screen, (0, 0, 0), (10, 10, 200, 20), 2)  # Outline