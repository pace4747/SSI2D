import pygame

class InputManager:
    def __init__(self, config_manager, logging_module):
        self.config_manager = config_manager
        self.logging_module = logging_module
        self.actions = {}  # Tracks current actions (e.g., {'up': True})
        self.logging_module.log_info("InputManager initialized.")

    def handle_event(self, event):
        """Process Pygame events (e.g., key presses)."""
        key_bindings = self.config_manager.get('key_bindings', {})
        
        if event.type == pygame.KEYDOWN:
            for action, key in key_bindings.items():
                if event.key == key:
                    self.actions[action] = True
                    self.logging_module.log_debug(f"Key pressed: {action} ({pygame.key.name(event.key)})")
        
        elif event.type == pygame.KEYUP:
            for action, key in key_bindings.items():
                if event.key == key:
                    self.actions[action] = False
                    self.logging_module.log_debug(f"Key released: {action} ({pygame.key.name(event.key)})")

    def get_actions(self):
        """Return the current state of actions (e.g., {'up': True, 'down': False})."""
        return self.actions