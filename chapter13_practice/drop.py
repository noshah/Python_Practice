import pygame
from pygame.sprite import Sprite


class Drop(Sprite):

    def __init__(self, rain):
        super().__init__()
        self.screen = rain.screen
        self.settings = rain.settings

        self.image = pygame.image.load('images/waterdrop.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def repeat_rain(self):
        screen_rect = self.screen.get_rect()

        if self.rect.bottom >= screen_rect.bottom:
            return True



