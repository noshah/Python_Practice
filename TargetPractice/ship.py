import pygame

class Ship:
    """information about ship."""
    def __init__(self, tp_game):
        """attribute about ship."""
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.up = False
        self.down = False

    def update(self):
        """This method helpfull for ship up and down on screen."""
        if self.up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def blitme(self):
        """this method combine image and screen."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
