import pygame
from pygame.sprite import Sprite

class Target(Sprite):
    """information about target."""
    def __init__(self, tp_game):
        """"attribute about target."""
        super().__init__()
        self.screen = tp_game.screen
        self.screen_rect = tp_game.screen.get_rect()
        self.settings = tp_game.settings
        self.color = self.settings.target_color

        # Create Target.
        self.rect = pygame.Rect(0, 0, self.settings.target_width, self.settings.target_height)
        self.rect.midright = self.screen_rect.midright

        self.y = float(self.rect.y)

    def update(self):
        """this method use for target move up and down."""

        self.y += (self.settings.target_speed *
                   self.settings.target_direction)

        self.rect.y = self.y

    def check_edges(self):
        """return True if rect is at edge of the screen."""
        screen_rect = self.screen.get_rect()

        if self.rect.top <= screen_rect.top or self.rect.bottom >= screen_rect.bottom:
            return True

    def draw_target(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


