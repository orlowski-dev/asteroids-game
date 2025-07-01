import pygame
from constants import *
from player import Player


def main():
    print("Starting Asteroids!")
    pygame.init()
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    surface = pygame.Surface
    clock = pygame.time.Clock()
    dt = 0  # delta time
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # surface.fill(color=(255, 255, 255, 1))
        surface.fill(screen, color=(0, 0, 0, 1))

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
