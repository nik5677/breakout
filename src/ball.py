import math

import pygame


class Ball(pygame.sprite.Sprite):
    """This class represents a ball. It derives from the "Sprite" class in Pygame."""
    def __init__(self, image, speed=7):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = 393
        self.rect.y = 450

        self.speed = speed
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self):
        """Update ball position"""
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

    def start(self):
        """Start the ball (if it is not moving)"""
        if self.velocity_x == 0 and self.velocity_y == 0:
            self.velocity_y = self.speed

    def bounce(self, obstacle):
        """Bounce the ball off the obstacle"""
        offset = ((self.rect.centerx - obstacle.rect.centerx) / obstacle.rect.width) / 2
        bounce_angle = (offset - 0.5) * math.pi

        self.velocity_x = self.speed * math.cos(bounce_angle)
        self.velocity_y = self.speed * math.sin(bounce_angle)

        if obstacle.rect.centery - self.rect.centery < 0:
            self.velocity_y = -self.velocity_y

    def bounce_x(self):
        """Bounce the ball off the left/right wall"""
        self.velocity_x = -self.velocity_x

    def bounce_y(self):
        """Bounce the ball off the floor/ceiling"""
        self.velocity_y = -self.velocity_y

    def reset(self):
        """Move the ball to it's initial position and stop it"""
        self.rect.x = 393
        self.rect.y = 450
        self.velocity_x = 0
        self.velocity_y = 0
