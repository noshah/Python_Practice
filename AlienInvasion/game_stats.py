class GameStats:
    """Track statistics for Alien Inavasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings

        # High score should never be reset.
        self.high_score = 0
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initilze stastics that can change during the game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
