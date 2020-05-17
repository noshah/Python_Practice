class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initilaze statistics."""
        self.settings = ai_game.settings
        # High score should never be reset.
        filname = 'highscore.txt'

        with open(filname, 'r') as objects:
            num = objects.read()

        self.high_score = int(num)
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False

    def reset_stats(self):
        """Initilize stastics that can change during the game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1