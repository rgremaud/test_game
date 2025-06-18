class GameStats:
    """Track stats for ninja"""

    def __init__(self, the_game):
        """Initialize statistics"""
        self.settings = the_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.badguy_life_left = self.settings.badguy_life