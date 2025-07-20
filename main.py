import pygame
from main_loop import GameLoop
from configuration import ConfigManager
from logging_module import LoggingModule
from input_manager import InputManager

# Simple Entity class for test player
class Entity:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5  # Pixels per frame

    def update(self, actions, delta_time):
        self.x += (actions.get('right', False) - actions.get('left', False)) * self.speed
        self.y += (actions.get('down', False) - actions.get('up', False)) * self.speed

    def render(self, screen, camera_x, camera_y):
        pygame.draw.rect(screen, self.color, (self.x - camera_x, self.y - camera_y, self.width, self.height))

# Dummy classes for now
class DummyRendering:
    def render(self, screen, entities, camera_x, camera_y):
        screen.fill((0, 0, 255))  # Blue background
        for entity in entities:
            entity.render(screen, camera_x, camera_y)

class DummyPhysics:
    def update(self, entities, delta_time):
        actions = input_manager.get_actions()
        for entity in entities:
            entity.update(actions, delta_time)

# Start Pygame
pygame.init()

# Create modules
config_manager = ConfigManager()
logging_module = LoggingModule()

screen = pygame.display.set_mode(config_manager.get('resolution'))  # Uses config resolution

input_manager = InputManager(config_manager, logging_module)  # Real InputManager
rendering_module = DummyRendering()
physics_module = DummyPhysics()

# Create test player entity
player = Entity(100, 100, 50, 50, (255, 0, 0))  # Red square
entities = [player]

# Create and run the loop
game_loop = GameLoop(screen, config_manager)
game_loop.run(entities, input_manager, rendering_module, physics_module, logging_module)