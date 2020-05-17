import sys

import pygame

from random import randint


from star_info import StarInfo


class Stars:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption('Star Grid')

        self.stars = pygame.sprite.Group()

        self._create_star()


    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_star(self):
        star = StarInfo(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)
        number = randint(0, number_stars_x)

        available_space_y = (self.screen_height)

        number_rows = available_space_y // (2 * star_height)
        number1 = randint(0, number_rows)

        self._create_stars(number1, number)

    def _create_stars(self, number1, number):
        star = StarInfo(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * number
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star_height * number1
        self.stars.add(star)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    st = Stars()
    st.run_game()





