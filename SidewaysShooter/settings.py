class Settings:
    """ Initialize the game's static settings."""

    def __init__(self):
        """details like width,height and color etc."""
        # Screen settings.
        self.screen_width = 700
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Setteings of ship.

        self.ship_limit = 3

        # Settings of bullets.
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 4

        # Settings of aliens.
        self.fleet_drop_speed = 60

        # How quickly the game speeds up
        self.speed_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throught the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of -1 represents up; 1 represents down.
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale
        self.alien_points = int(self.alien_points * self.speed_scale)





