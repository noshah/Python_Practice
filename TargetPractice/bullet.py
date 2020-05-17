import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """this class is usefull for making bullets."""
    def __init__(self, tp_game):
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = tp_game.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """this method useful for moving bullet horizontal."""
        self.x += self.settings.bullet_speed

        self.rect.x = self.x

    def draw_bullet(self):
        """deaw bullet on screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

