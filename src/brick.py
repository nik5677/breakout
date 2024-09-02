import pygame


class Brick(pygame.sprite.Sprite):
    """This class represents a brick. It derives from the "Sprite" class in Pygame."""
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
