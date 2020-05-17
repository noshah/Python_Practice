import sys

import pygame

from settings import Settings
from drop import Drop

class Rain:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Steady Rain')

        self.drops = pygame.sprite.Group()

        self._create_rain()

    def run_game(self):
        while True:
            self._check_events()
            self._check_drops_edges()
            self._repeat_drop()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_rain(self):
        rain = Drop(self)
        rain_width, rain_height = rain.rect.size
        avalible_space_x = self.screen_width
        number_drop = avalible_space_x // (rain_width)

        avalible_space_y = self.screen_height
        number_rows = avalible_space_y // (rain_height)

        for row_number in range(number_rows):
            for drop_number in range(number_drop):
                self._create_steady_rain(row_number, drop_number)

    def _create_steady_rain(self, row_number, drop_number):
        rain = Drop(self)
        rain_width, rain_height = rain.rect.size
        rain.x = rain_width * drop_number
        rain.rect.x = rain.x
        rain.rect.y = rain_height * row_number
        self.drops.add(rain)

    def _rain_drop_line(self):
        for row_number in range(0, 1):
            for drop_number in range(0, 8):
                self._create_steady_rain(row_number, drop_number)


    def _repeat_drop(self):
        for drop in self.drops.sprites():
            if drop.repeat_rain():
                self._rain_drop_line()

    def _check_drops_edges(self):
        for drop in self.drops.sprites():
            if drop.check_edges():
                self._drop_down()
                break

    def _drop_down(self):
        for drop in self.drops.sprites():
            drop.rect.y += self.settings.drop_speed




    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    rn = Rain()
    rn.run_game()
