import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from target import Target


class TargetPractice:
    """ This class is work for all aspects of game."""

    def __init__(self):

        """In this method we make helpful attributes and create a instance of class which is usefull for our GAME."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Target Practice')

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)
        self.i = 0

        # Make the play button.
        self.play_button = Button(self, 'Play')


    def run_game(self):
        """this method collects all methods and helper methods to make run_GAME."""
        while True:

            # Watch for keyword and mouse events.
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._target_increase()
                self._update_target()
            self._update_screen()

    def _check_events(self):
        """This method for checking keyword events and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game stastics.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True

            # Get rid of any remaining bullets.
            self.bullets.empty()

            # Create a center ship.
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """ check keyboard and mouse click."""
        if event.key == pygame.K_UP:
            self.ship.up = True
        elif event.key == pygame.K_DOWN:
            self.ship.down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ check keyword and mouse up."""
        if event.key == pygame.K_UP:
            self.ship.up = False
        elif event.key == pygame.K_DOWN:
            self.ship.down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left > 1350:
                self.i += 1
                self.bullets.remove(bullet)
            elif self.i == 3:
                self.stats.game_active = False
                pygame.mouse.set_visible(True)
        print(len(self.bullets))

    def _update_target(self):
        """allow target to move."""
        self._check_target_edges()
        self.target.update()

        if pygame.sprite.spritecollideany(self.target, self.bullets) or self.i == 3:
            self._target_hit()

    def _target_increase(self):
        """target speed and ship speed increase."""
        if pygame.sprite.spritecollideany(self.target, self.bullets):

            sleep(2.0)
            self.bullets.empty()
            self.settings.increase_speed()

    def _target_hit(self):
        self.i = 0

        self.bullets.empty()
        self.ship.center_ship()

        sleep(0.5)
        self.stats.game_active = False
        pygame.mouse.set_visible(True)

    def _check_target_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        if self.target.check_edges():
            self.settings.target_direction *= -1

    def _update_screen(self):
        """ this method to draw on screen and flip."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.draw_target()
        # Draw the play button if the is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    target = TargetPractice()
    target.run_game()




