class GameStats:
    """track statistics for target practice."""

    def __init__(self, tp_game):
        """initilize statistics."""
        self.settings = tp_game.settings
        self.reset_stats()

        self.game_active = False
    def reset_stats(self):
        """initialize stastics that can change during the game."""
        self.bullet_left = self.settings.bullet_allowed
