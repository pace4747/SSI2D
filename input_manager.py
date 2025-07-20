import pygame

class InputManager:
    def __init__(self, config_manager):
        self.bindings = config_manager.get('key_bindings')

    def handle_event(self, event):
        pass  # Handle specific events like shoot later

    def get_actions(self):
        keys = pygame.key.get_pressed()
        actions = {
            'up': keys[self.bindings.get('up')],
            'down': keys[self.bindings.get('down')],
            'left': keys[self.bindings.get('left')],
            'right': keys[self.bindings.get('right')],
            'shoot': keys[self.bindings.get('shoot')]
        }
        return actions