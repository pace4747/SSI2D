import json
import os
import pygame

class ConfigManager:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        # Default settings if no file exists
        default_config = {
            'fps': 60,
            'resolution': (800, 600),
            'key_bindings': {
                'up': 'w',
                'down': 's',
                'left': 'a',
                'right': 'd',
                'shoot': 'f'
            },
            'volume': 1.0
        }
        # Load from file if it exists
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                # Ensure all required keys exist
                for key, value in default_config.items():
                    if key not in config:
                        config[key] = value
                return config
            except json.JSONDecodeError as e:
                print(f"Error reading config file: {e}. Using defaults.")
                return default_config
        else:
            self.save_config(default_config)
            return default_config

    def save_config(self, config=None):
        if config is None:
            config = self.config
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=4)
        except Exception as e:
            print(f"Error saving config: {e}")

    def get(self, key, default=None):
        if key == 'key_bindings':
            # Convert string keys to pygame constants
            bindings = self.config.get(key, {})
            return {k: getattr(pygame, f'K_{v}') for k, v in bindings.items()}
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()