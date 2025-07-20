import pygame
import sys

class GameLoop:
    def __init__(self, screen, config_manager):
        self.screen = screen
        self.config_manager = config_manager
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = self.config_manager.get('fps', 60)

    def run(self, entities, input_manager, rendering_module, physics_module, logging_module):
        camera_x = 0  # Dummy camera for test
        camera_y = 0
        while self.running:
            try:
                delta_time = self.clock.tick(self.fps) / 1000.0

                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    input_manager.handle_event(event)

                # Get actions
                actions = input_manager.get_actions()

                # Update
                physics_module.update(entities, delta_time)

                # Render with camera
                rendering_module.render(self.screen, entities, camera_x, camera_y)

                pygame.display.flip()
            except Exception as e:
                logging_module.log_error(f"Error in game loop: {e}")
                self.running = False

        logging_module.log_info("Game loop exited.")
        pygame.quit()
        sys.exit()