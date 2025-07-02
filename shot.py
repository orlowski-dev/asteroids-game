import pygame
from constants import *
from circleshape import CircleShape
from pygame.draw import circle


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        circle(
            surface=surface,
            color=(255, 255, 255, 1),
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt
