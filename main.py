import pygame
from constants import *


def main():
    print("Starting Asteroids!")
    pygame.init()
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.display.set_mode(screen_size)
    surface = pygame.Surface(screen_size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        surface.fill(color=(255, 255, 255, 1))

        pygame.display.flip()


if __name__ == "__main__":
    main()
