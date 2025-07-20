import pygame
from pygame.locals import *
from constants import *
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snakes and Spiders Island")
    clock = pygame.time.Clock()
    game = Game(screen)
    running = True

    while running:
        dt = clock.tick(FPS) / 1000.0  # Delta time in seconds
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        game.update(dt)
        game.draw()

    pygame.quit()

if __name__ == "__main__":
    main()
