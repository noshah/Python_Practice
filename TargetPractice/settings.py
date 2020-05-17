class Settings:
    """this class give us information like screen width, hight etc."""
    def __init__(self):
        """information about game."""
        self.bg_color = (230, 230, 230)

        # settings of ship.


        # Settings of bullets.

        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Settings of target.
        self.target_width = 40
        self.target_height = 40
        self.target_color = (0, 230, 230)


        
        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throught the game."""
        self.ship_speed = 6.0
        self.target_speed = 10
        self.bullet_speed = 6.0

        # fleet_direction of 1 represents up; -1 represents down.
        self.target_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale