import pygame
from pygame.locals import *
from constants import *
from game import Game

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snakes and Spiders Island")
    clock = pygame.time.Clock()
    game = Game(screen)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        game.update()
        game.draw()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
