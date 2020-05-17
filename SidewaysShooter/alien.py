import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """ Initialize the alien and set its starting posiotin."""
        super().__init__()
        self.scren = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top right of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at edge if screen."""
        screen_rect = self.scren.get_rect()

        if self.rect.top <= screen_rect.top or self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        """Move the alien to the up or down."""
        self.y += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.y = self.y


