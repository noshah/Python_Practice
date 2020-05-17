import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')

        self.image1 = pygame.image.load('images/nova.bmp')
        self.rect = self.image.get_rect()
        self.rect1 = self.image1.get_rect()

        self.rect1.midleft = self.screen_rect.midleft

        self.y = float(self.rect1.y)

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.up = False
        self.down = False

    def update(self):
        if self.up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def blita(self):
        self.screen.blit(self.image1, self.rect1)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)





