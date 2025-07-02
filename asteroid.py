from circleshape import CircleShape
import pygame
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(
            surface=surface,
            color=(255, 255, 255, 1),
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius < ASTEROID_MIN_RADIUS:
            self.kill()
            return

        random_angle = random.uniform(20, 50)
        vector1 = pygame.Vector2(self.position.x, self.position.y).rotate(random_angle)
        vector2 = pygame.Vector2(self.position.x, self.position.y).rotate(-random_angle)

        asteroid_one = Asteroid(
            self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS
        )
        asteroid_two = Asteroid(
            self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS
        )

        asteroid_one.velocity = vector1
        asteroid_two.velocity = vector2

        self.kill()
