import pygame


class Paddle(pygame.sprite.Sprite):
    """This class represents a paddle. It derives from the "Sprite" class in Pygame."""
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 525

    def move(self, x):
        """Move the paddle in an x dimension"""
        self.rect.x = x

        # stop the paddle if x is off-screen
        if self.rect.x > 700:
            self.rect.x = 700
        if self.rect.x < 0:
            self.rect.x = 0
