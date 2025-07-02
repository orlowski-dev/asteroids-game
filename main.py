import pygame
from constants import *
from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid


def main():
    print("Starting Asteroids!")
    pygame.init()
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    surface = pygame.Surface
    clock = pygame.time.Clock()
    dt = 0  # delta time

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_filed = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # surface.fill(color=(255, 255, 255, 1))
        surface.fill(screen, color=(0, 0, 0, 1))

        updatable.update(dt)
        # player.draw(screen)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")

        for thing_to_draw in drawable:
            thing_to_draw.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
