import pygame
from pygame.sprite import Sprite


class StarInfo(Sprite):
    """A class to represent a star."""

    def __init__(self, star):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = star.screen

        self.image = pygame.image.load('images/Capture.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)



